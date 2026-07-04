"""
MyOdyssey Article Fetcher
Uses Crossref (primary) + OpenAlex (secondary) for bulletproof scientific article retrieval.
"""

import requests
from datetime import datetime, timedelta


RESEARCH_QUERIES = [
    "pulsed electric field protein extraction food",
    "pulsed electric field bioactive peptides food",
    "pulsed electric field food emulsion",
    "insect protein alternative food functional",
    "deep eutectic solvent protein bioactive extraction",
    "black soldier fly protein processing",
    "mealworm protein functional properties",
    "pulsed electric field microalgae extraction",
]

# High-weight keywords: must appear to be truly relevant
CORE_KEYWORDS = [
    "pulsed electric field", "PEF", "alternative protein", "insect protein",
    "bioactive peptide", "emulsion", "black soldier fly", "mealworm",
    "tenebrio", "hermetia illucens", "acheta", "cricket protein",
    "deep eutectic solvent", "chitosan", "astaxanthin", "phycocyanin",
    "protein extraction", "protein functionality", "protein hydrolysate",
    "antioxidant peptide", "ACE inhibitory", "food processing",
    "non-thermal", "electroporation", "cell disruption",
    "spray drying", "encapsulation", "microalgae protein",
]

# Minimum relevance threshold: articles below this score are discarded
MIN_RELEVANCE_SCORE = 40


def reconstruct_abstract(inverted_index: dict) -> str:
    """Reconstruct abstract from OpenAlex inverted index format."""
    if not inverted_index or not isinstance(inverted_index, dict):
        return ""
    try:
        max_pos = max(pos for positions in inverted_index.values() for pos in positions)
        words = [""] * (max_pos + 1)
        for word, positions in inverted_index.items():
            for pos in positions:
                words[pos] = word
        return " ".join(words)
    except (ValueError, TypeError):
        return ""


def fetch_from_crossref(query: str, from_date: str, rows: int = 15) -> list:
    """Fetch articles from Crossref API."""
    url = "https://api.crossref.org/works"
    params = {
        "query": query,
        "filter": f"from-pub-date:{from_date},type:journal-article",
        "rows": rows,
        "sort": "relevance",
    }
    try:
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        items = r.json().get("message", {}).get("items", [])
        articles = []
        for item in items:
            authors = item.get("author", [])
            last_author_obj = authors[-1] if authors else {}
            last_author = f"{last_author_obj.get('given', '')} {last_author_obj.get('family', '')}".strip()
            institution = ""
            if last_author_obj.get("affiliation"):
                institution = last_author_obj["affiliation"][0].get("name", "")

            pub_date_parts = item.get("published-print", item.get("published-online", {})).get("date-parts", [[]])
            date_parts = pub_date_parts[0] if pub_date_parts else []
            pub_date = "-".join(str(d) for d in date_parts) if date_parts else "N/A"

            articles.append({
                "title": item.get("title", ["N/A"])[0] if item.get("title") else "N/A",
                "senior_author": last_author or "N/A",
                "institution": institution or "N/A",
                "journal": item.get("container-title", ["N/A"])[0] if item.get("container-title") else "N/A",
                "publication_date": pub_date,
                "doi": item.get("DOI", ""),
                "doi_url": f"https://doi.org/{item.get('DOI', '')}",
                "abstract": item.get("abstract", ""),
                "source_api": "Crossref",
            })
        return articles
    except Exception as e:
        print(f"Crossref error for '{query}': {e}")
        return []


def fetch_from_openalex(query: str, per_page: int = 25) -> list:
    """Fetch articles from OpenAlex API (sorted by date, filtered in Python)."""
    url = "https://api.openalex.org/works"
    params = {
        "search": query,
        "per_page": per_page,
        "sort": "publication_date:desc",
        "mailto": "myodyssey@research.app",
    }
    try:
        r = requests.get(url, params=params, timeout=15)
        r.raise_for_status()
        results = r.json().get("results", [])
        articles = []
        for work in results:
            authorships = work.get("authorships", [])
            last_auth = authorships[-1] if authorships else {}
            last_author = last_auth.get("author", {}).get("display_name", "N/A")
            institution = ""
            country = ""
            if last_auth.get("institutions"):
                institution = last_auth["institutions"][0].get("display_name", "")
                country = last_auth["institutions"][0].get("country_code", "")

            source_loc = work.get("primary_location") or {}
            source_obj = source_loc.get("source") or {}

            abstract = reconstruct_abstract(work.get("abstract_inverted_index"))

            articles.append({
                "title": work.get("title", "N/A"),
                "senior_author": last_author,
                "institution": f"{institution}, {country}" if country else institution or "N/A",
                "journal": source_obj.get("display_name", "N/A"),
                "publication_date": work.get("publication_date", "N/A"),
                "doi": (work.get("doi") or "").replace("https://doi.org/", ""),
                "doi_url": work.get("doi") or "",
                "abstract": abstract,
                "cited_by_count": work.get("cited_by_count", 0),
                "source_api": "OpenAlex",
            })
        return articles
    except Exception as e:
        print(f"OpenAlex error for '{query}': {e}")
        return []


def calculate_relevance_score(article: dict) -> int:
    """Calculate relevance score (0-100) with strict filtering for PEF/protein research."""
    score = 0
    title = (article.get("title") or "").lower()
    abstract = (article.get("abstract") or "").lower()
    combined = title + " " + abstract

    # STRICT RELEVANCE CHECK: At least one core keyword must appear in title
    title_has_core = False
    for kw in CORE_KEYWORDS:
        if kw.lower() in title:
            title_has_core = True
            break
    
    if not title_has_core:
        # Check if at least 2 core keywords appear in abstract
        abstract_hits = sum(1 for kw in CORE_KEYWORDS if kw.lower() in combined)
        if abstract_hits < 2:
            return 0  # Not relevant at all

    # Keyword relevance (max 55 points)
    keyword_score = 0
    for kw in CORE_KEYWORDS:
        if kw.lower() in title:
            keyword_score += 7  # Title match is very strong signal
        elif kw.lower() in combined:
            keyword_score += 3
    score += min(55, keyword_score)

    # Recency (max 25 points)
    try:
        pub_date = article.get("publication_date", "2020-01-01")
        if pub_date and pub_date != "N/A":
            date_obj = datetime.strptime(pub_date[:10], "%Y-%m-%d")
            days_old = (datetime.now() - date_obj).days
            if days_old <= 7:
                score += 25
            elif days_old <= 14:
                score += 22
            elif days_old <= 30:
                score += 18
            elif days_old <= 90:
                score += 14
            elif days_old <= 180:
                score += 10
            elif days_old <= 365:
                score += 7
            else:
                score += 3
    except (ValueError, TypeError):
        score += 5

    # Journal quality (max 20 points)
    journal = (article.get("journal") or "").lower()
    tier1 = ["nature", "science", "food chemistry", "food hydrocolloids",
             "trends in food science", "comprehensive reviews in food",
             "journal of agricultural and food chemistry"]
    tier2 = ["lwt", "innovative food science", "journal of food engineering",
             "food research international", "food and bioprocess technology",
             "international journal of food science", "food bioscience",
             "journal of food science", "frontiers in nutrition"]
    tier3_keywords = ["food", "protein", "bio", "colloid", "emulsion", "insect"]

    matched_tier = None
    for j in tier1:
        if j in journal:
            score += 20
            matched_tier = 1
            break
    if not matched_tier:
        for j in tier2:
            if j in journal:
                score += 15
                matched_tier = 2
                break
    if not matched_tier:
        for kw in tier3_keywords:
            if kw in journal:
                score += 10
                matched_tier = 3
                break
    if not matched_tier:
        score += 3

    return min(100, score)


def get_weekly_top_articles(limit: int = 10) -> list:
    """Main function: fetch, combine, deduplicate, score, and return top articles."""
    from_date = (datetime.now() - timedelta(days=14)).strftime("%Y-%m")
    all_articles = []

    # Fetch from Crossref (primary, most reliable for food science)
    for query in RESEARCH_QUERIES:
        articles = fetch_from_crossref(query, from_date, rows=10)
        all_articles.extend(articles)

    # Fetch from OpenAlex (secondary, for broader coverage)
    for query in RESEARCH_QUERIES[:3]:
        articles = fetch_from_openalex(query, per_page=15)
        all_articles.extend(articles)

    # Deduplicate by DOI
    seen_dois = set()
    unique_articles = []
    for article in all_articles:
        doi = article.get("doi", "").lower().strip()
        if doi and doi in seen_dois:
            continue
        if doi:
            seen_dois.add(doi)
        unique_articles.append(article)

    # Score, filter, and sort
    scored_articles = []
    for article in unique_articles:
        article["relevance_score"] = calculate_relevance_score(article)
        if article["relevance_score"] >= MIN_RELEVANCE_SCORE:
            scored_articles.append(article)

    scored_articles.sort(key=lambda x: x["relevance_score"], reverse=True)
    return scored_articles[:limit]


def get_retrospective_articles(years: int = 5, limit: int = 20) -> list:
    """Fetch high-impact articles from the last N years."""
    from_date = (datetime.now() - timedelta(days=365 * years)).strftime("%Y-%m")
    all_articles = []

    for query in RESEARCH_QUERIES[:4]:
        articles = fetch_from_crossref(query, from_date, rows=15)
        all_articles.extend(articles)

    # Deduplicate
    seen_dois = set()
    unique = []
    for a in all_articles:
        doi = a.get("doi", "").lower().strip()
        if doi and doi in seen_dois:
            continue
        if doi:
            seen_dois.add(doi)
        unique.append(a)

    for a in unique:
        a["relevance_score"] = calculate_relevance_score(a)

    unique.sort(key=lambda x: x["relevance_score"], reverse=True)
    return unique[:limit]
