"""
MyOdyssey - Scientific Innovation Dashboard
PEF, Alternative Proteins, and Bioactivity Research Intelligence
"""

import streamlit as st
import os

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MyOdyssey",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;500;600&display=swap');

    .main { background-color: #FAFAF8; }

    h1, h2, h3 { font-family: 'Merriweather', serif; color: #2F3E2F; }
    p, li, span, div { font-family: 'Inter', sans-serif; }

    .article-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 16px;
        border-left: 5px solid #6B8E6B;
    }
    .score-badge {
        display: inline-block;
        background: linear-gradient(135deg, #D4A017, #E8B828);
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85em;
    }
    .researcher-card {
        background: white;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 12px;
        border-left: 4px solid #D4A017;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }
    .metabolite-card {
        background: white;
        padding: 14px;
        border-radius: 8px;
        margin-bottom: 8px;
        border-left: 3px solid #6B8E6B;
    }
    a { color: #6B8E6B; }
    .stTabs [data-baseweb="tab"] { font-family: 'Inter', sans-serif; font-weight: 600; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# AUTHENTICATION
# ─────────────────────────────────────────────────────────────────────────────
def check_login():
    """Simple authentication gate."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("## 🧬 MyOdyssey")
        st.markdown("*Your Scientific Innovation Radar*")
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.form("login"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Sign In", use_container_width=True)
                if submitted:
                    if username == "admin" and password == "odyssey2026":
                        st.session_state.authenticated = True
                        st.rerun()
                    else:
                        st.error("Invalid credentials. Please try again.")
        return False
    return True


# ─────────────────────────────────────────────────────────────────────────────
# MAIN APPLICATION
# ─────────────────────────────────────────────────────────────────────────────
def main():
    if not check_login():
        return

    # Sidebar
    st.sidebar.markdown("## 🧬 MyOdyssey")
    st.sidebar.markdown("**Scientific Innovation Radar**")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Research Focus:**")
    st.sidebar.markdown("- Pulsed Electric Field (PEF)")
    st.sidebar.markdown("- Alternative Proteins")
    st.sidebar.markdown("- Bioactive Peptides")
    st.sidebar.markdown("- Emulsion Science")
    st.sidebar.markdown("- Food & Material Science")
    st.sidebar.markdown("---")
    st.sidebar.caption("Updates: Mon & Fri at 10:00 AM")

    # Main content
    st.title("MyOdyssey")
    st.markdown("*Exploring the frontiers of PEF, Alternative Proteins, and Bioactivity*")

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📅 Weekly Top 10",
        "💡 Idea Lab",
        "⏳ 5-Year Retrospective",
        "📡 Researcher Radar",
        "🌿 Raw Materials & Chat",
    ])

    # ─── TAB 1: WEEKLY TOP 10 ────────────────────────────────────────────────
    with tab1:
        st.header("Weekly Top 10 Discoveries")
        st.markdown("Latest breakthroughs from Nature, Science, Elsevier, and Springer Nature.")

        from modules.article_fetcher import get_weekly_top_articles

        if "weekly_articles" not in st.session_state:
            st.session_state.weekly_articles = None

        if st.button("🔍 Fetch Latest Articles", key="fetch_weekly"):
            with st.spinner("Searching Crossref and OpenAlex databases..."):
                st.session_state.weekly_articles = get_weekly_top_articles(limit=10)

        articles = st.session_state.weekly_articles
        if articles:
            for i, article in enumerate(articles, 1):
                abstract_text = article.get("abstract", "")
                if not abstract_text or len(abstract_text) < 20:
                    abstract_text = "Abstract not available via open API. Click the link to read the full paper."
                else:
                    # Clean HTML tags from Crossref abstracts
                    import re
                    abstract_text = re.sub(r"<[^>]+>", "", abstract_text)[:500]

                st.markdown(f"""
                <div class="article-card">
                    <span class="score-badge">Score: {article.get('relevance_score', 0)}/100</span>
                    <h3 style="margin-top:8px;">{i}. {article.get('title', 'N/A')}</h3>
                    <p><strong>🏛️ Institution:</strong> {article.get('institution', 'N/A')}</p>
                    <p><strong>👨‍🔬 Senior Author:</strong> {article.get('senior_author', 'N/A')}</p>
                    <p><strong>📖 Journal:</strong> {article.get('journal', 'N/A')} &nbsp;|&nbsp; <strong>📅 Date:</strong> {article.get('publication_date', 'N/A')}</p>
                    <p><strong>Abstract:</strong> {abstract_text}</p>
                    <a href="{article.get('doi_url', '#')}" target="_blank"><strong>→ Read Full Article</strong></a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Click **Fetch Latest Articles** to load the most recent discoveries in your field.")

    # ─── TAB 2: IDEA LAB ─────────────────────────────────────────────────────
    with tab2:
        st.header("The Idea Lab")
        st.markdown("AI-generated research ideas combining recent discoveries with your expertise.")

        if st.session_state.weekly_articles:
            if st.button("🧠 Generate Research Ideas", key="gen_ideas"):
                api_key = os.environ.get("OPENAI_API_KEY", st.secrets.get("OPENAI_API_KEY", ""))
                if not api_key:
                    st.error("OpenAI API key not configured. Add it to Streamlit Secrets.")
                else:
                    with st.spinner("Synthesizing innovative research concepts..."):
                        try:
                            from openai import OpenAI
                            client = OpenAI(api_key=api_key)

                            article_summaries = "\n".join([
                                f"- {a['title']} ({a['journal']}, {a['publication_date']})"
                                for a in st.session_state.weekly_articles[:5]
                            ])

                            prompt = f"""You are a senior researcher specializing in Pulsed Electric Field (PEF) technology, 
alternative proteins (especially insect proteins from Black Soldier Fly and Yellow Mealworm), 
bioactive peptides, emulsion science, and food/material science.

Based on these recent publications:
{article_summaries}

And considering the researcher's expertise in:
- PEF-assisted protein extraction from insects
- Colloidal and functional properties of insect proteins
- Emulsion stabilization with alternative proteins
- Bioactive peptide generation and characterization
- Deep eutectic solvents for green extraction

Generate exactly 5 highly innovative and feasible research ideas. Each idea should combine 
concepts from the recent papers with the researcher's expertise in novel ways.

For each idea provide:
1. A compelling title
2. A 2-3 sentence description of the concept
3. The key innovation (what makes it truly novel)
4. Expected scientific and practical impact
5. Estimated timeline in months

Format your response as numbered ideas with clear headers."""

                            response = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[{"role": "user", "content": prompt}],
                                temperature=0.8,
                                max_tokens=3000,
                            )
                            st.session_state.ideas = response.choices[0].message.content
                        except Exception as e:
                            st.error(f"Error generating ideas: {str(e)}")

            if "ideas" in st.session_state:
                st.markdown(st.session_state.ideas)

                st.markdown("---")
                st.subheader("Scientific Illustrations")
                st.markdown("*Concept visualizations for the top research ideas:*")

                # Display pre-generated illustrations
                img_dir = os.path.join(os.path.dirname(__file__), "assets")
                for i in range(1, 4):
                    img_path = os.path.join(img_dir, f"idea_{i}.png")
                    if os.path.exists(img_path):
                        st.image(img_path, use_container_width=True)
                    else:
                        st.info(f"Illustration {i} will be generated during scheduled updates.")
        else:
            st.info("Please fetch articles in the **Weekly Top 10** tab first, then return here to generate ideas.")

    # ─── TAB 3: 5-YEAR RETROSPECTIVE ─────────────────────────────────────────
    with tab3:
        st.header("5-Year Retrospective")
        st.markdown("High-impact publications from 2020-2025 in PEF and Alternative Proteins.")

        from modules.article_fetcher import get_retrospective_articles

        if "retro_articles" not in st.session_state:
            st.session_state.retro_articles = None

        if st.button("📚 Load Retrospective", key="fetch_retro"):
            with st.spinner("Analyzing 5 years of research impact..."):
                st.session_state.retro_articles = get_retrospective_articles(years=5, limit=20)

        retro = st.session_state.retro_articles
        if retro:
            for i, article in enumerate(retro, 1):
                st.markdown(f"""
                <div style="padding:12px; border-bottom: 1px solid #eee;">
                    <span class="score-badge">Score: {article.get('relevance_score', 0)}/100</span>
                    <strong>{i}. {article.get('title', 'N/A')}</strong><br>
                    <span style="color:#666; font-size:0.85em;">
                        {article.get('journal', 'N/A')} &nbsp;|&nbsp; {article.get('publication_date', 'N/A')} 
                        &nbsp;|&nbsp; Senior: {article.get('senior_author', 'N/A')}
                    </span><br>
                    <a href="{article.get('doi_url', '#')}" target="_blank" style="font-size:0.85em;">Read Article →</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Click **Load Retrospective** to analyze the most impactful papers from the last 5 years.")

    # ─── TAB 4: RESEARCHER RADAR ─────────────────────────────────────────────
    with tab4:
        st.header("Researcher Radar")
        st.markdown("Global leaders and potential collaborators in PEF and Alternative Proteins.")

        from modules.researchers import RESEARCHERS

        col1, col2 = st.columns(2)
        for i, res in enumerate(RESEARCHERS):
            with (col1 if i % 2 == 0 else col2):
                st.markdown(f"""
                <div class="researcher-card">
                    <h4 style="margin:0; color:#2F3E2F;">{res['name']}</h4>
                    <p style="margin:2px 0; font-size:0.9em; color:#666;">{res['affiliation']}</p>
                    <p style="margin:4px 0;"><strong>Focus:</strong> {res['focus']}</p>
                    <p style="margin:4px 0; font-size:0.85em; color:#555;"><em>{res['key_contribution']}</em></p>
                    <a href="{res['scholar_url']}" target="_blank" style="font-size:0.85em;">Google Scholar Profile →</a>
                </div>
                """, unsafe_allow_html=True)

    # ─── TAB 5: RAW MATERIALS & CHAT ─────────────────────────────────────────
    with tab5:
        st.header("Raw Materials & Bioactive Metabolites")
        st.markdown("Interactive database of key raw materials and their bioactive components.")

        from modules.raw_materials_db import list_materials, get_material, get_metabolites, search_by_keyword

        col1, col2 = st.columns([1, 2])

        with col1:
            selected = st.selectbox("Select Raw Material", list_materials())
            material = get_material(selected)
            if material:
                st.markdown(f"**{selected}**")
                st.markdown(f"*{material['description']}*")

        with col2:
            st.subheader(f"Key Metabolites")
            metabolites = get_metabolites(selected)
            for met in metabolites:
                st.markdown(f"""
                <div class="metabolite-card">
                    <strong>{met['name']}</strong><br>
                    <span style="font-size:0.85em;">
                        <strong>Function:</strong> {met['function']}<br>
                        <strong>Bioactivity:</strong> {met['bioactivity']}<br>
                        <strong>Extraction:</strong> {met['extraction_method']}<br>
                        <strong>PEF Relevance:</strong> <em>{met['pef_relevance']}</em>
                    </span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("💬 Research Assistant")

        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = []

        for msg in st.session_state.chat_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if user_input := st.chat_input("Ask about raw materials, PEF applications, or extraction methods..."):
            st.session_state.chat_messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Generate response using keyword search + optional LLM
            with st.chat_message("assistant"):
                results = search_by_keyword(user_input)
                if results:
                    response = f"Based on my database, here are relevant findings for **'{user_input}'**:\n\n"
                    for r in results[:5]:
                        response += f"- **{r['metabolite_name']}** from *{r['material']}*: {r['bioactivity']}. PEF relevance: {r['pef_relevance']}\n"
                else:
                    response = f"I couldn't find a direct match for '{user_input}' in the metabolite database. Try searching for keywords like 'antioxidant', 'antimicrobial', 'emulsion', 'chitin', or 'peptide'."

                st.markdown(response)
                st.session_state.chat_messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
