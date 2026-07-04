"""
MyOdyssey Raw Materials Database
In-memory database of raw materials and their key bioactive metabolites.
No file system writes required - works on any cloud platform.
"""


RAW_MATERIALS = {
    "Shrimp Shell (Crustacean Byproduct)": {
        "description": "Marine crustacean waste rich in structural biopolymers and high-value pigments. Represents ~50% of shrimp processing waste globally.",
        "metabolites": [
            {
                "name": "Chitin",
                "function": "Structural polysaccharide (poly-N-acetylglucosamine)",
                "extraction_method": "Chemical (HCl demineralization + NaOH deproteinization) or enzymatic",
                "bioactivity": "Immune modulation, antimicrobial, wound healing scaffold",
                "pef_relevance": "PEF can enhance demineralization efficiency and reduce chemical usage"
            },
            {
                "name": "Chitosan",
                "function": "Deacetylated chitin derivative, cationic biopolymer",
                "extraction_method": "Alkaline deacetylation of chitin (40-60% NaOH, 80-120C)",
                "bioactivity": "Antimicrobial, cholesterol-lowering, drug delivery carrier, film-forming",
                "pef_relevance": "PEF pre-treatment improves deacetylation degree and reduces processing time"
            },
            {
                "name": "Bioactive Peptides",
                "function": "Low molecular weight peptides (2-20 amino acids)",
                "extraction_method": "Enzymatic hydrolysis (alcalase, pepsin) or PEF-assisted extraction",
                "bioactivity": "ACE-inhibitory (antihypertensive), antioxidant, anti-inflammatory, DPP-IV inhibitory",
                "pef_relevance": "PEF enhances protein solubilization and exposes cleavage sites for enzymatic hydrolysis"
            },
            {
                "name": "Astaxanthin",
                "function": "Ketocarotenoid pigment (3,3'-dihydroxy-beta-carotene-4,4'-dione)",
                "extraction_method": "Organic solvent, supercritical CO2, or PEF + Deep Eutectic Solvent (DES)",
                "bioactivity": "Strongest natural antioxidant (6000x vitamin C), anti-inflammatory, neuroprotective, UV-protective",
                "pef_relevance": "PEF + DES is a green alternative to organic solvents for astaxanthin recovery"
            },
            {
                "name": "Calcium Carbonate (CaCO3)",
                "function": "Primary mineral component (20-30% of dry shell weight)",
                "extraction_method": "Acid demineralization (HCl, lactic acid)",
                "bioactivity": "Bone health supplementation, food fortification, pH regulation",
                "pef_relevance": "PEF-assisted demineralization reduces acid concentration needed"
            }
        ]
    },
    "Tenebrio molitor (Yellow Mealworm)": {
        "description": "Edible insect larvae with 45-60% protein content (dry basis). EU-approved novel food since 2021. Excellent amino acid profile.",
        "metabolites": [
            {
                "name": "Bioactive Peptides (ACE-inhibitory, antioxidant)",
                "function": "Peptide fractions <3 kDa with multiple bioactivities",
                "extraction_method": "Alkaline extraction + enzymatic hydrolysis (alcalase, flavourzyme) or PEF",
                "bioactivity": "ACE-inhibitory (IC50 ~0.5 mg/mL), antioxidant (ORAC), anti-inflammatory",
                "pef_relevance": "PEF increases protein extractability by 30-50% and enhances foaming properties"
            },
            {
                "name": "Oleic Acid (C18:1) & Linoleic Acid (C18:2)",
                "function": "Major unsaturated fatty acids (lipid content 25-35% DW)",
                "extraction_method": "Mechanical pressing, Soxhlet, or supercritical CO2",
                "bioactivity": "Cardiovascular protection, anti-inflammatory, skin barrier function",
                "pef_relevance": "PEF pre-treatment improves oil yield and reduces oxidation during extraction"
            },
            {
                "name": "Chitin (alpha-form)",
                "function": "Exoskeleton structural component (5-10% DW)",
                "extraction_method": "Acid-base sequential treatment after defatting",
                "bioactivity": "Prebiotic (gut microbiota modulation), immune stimulation",
                "pef_relevance": "PEF can assist in separating chitin from protein matrix"
            },
            {
                "name": "Zinc (Zn) & Iron (Fe)",
                "function": "Essential trace minerals in highly bioavailable forms",
                "extraction_method": "Mineral analysis after acid digestion",
                "bioactivity": "Immune support (Zn), oxygen transport (Fe), enzymatic cofactors",
                "pef_relevance": "PEF may enhance mineral bioaccessibility through matrix disruption"
            },
            {
                "name": "Complete Protein (all essential amino acids)",
                "function": "High biological value protein with PDCAAS ~0.75",
                "extraction_method": "Isoelectric precipitation (pH 4.5), alkaline extraction, or PEF-assisted",
                "bioactivity": "Muscle synthesis, satiety, nutritional completeness",
                "pef_relevance": "PEF improves protein solubility, foaming capacity, and emulsification"
            }
        ]
    },
    "Hermetia illucens (Black Soldier Fly Larvae)": {
        "description": "Fast-growing insect larvae with unique lipid profile. Protein 35-45% DW. Excellent for circular economy (feeds on organic waste).",
        "metabolites": [
            {
                "name": "Lauric Acid (C12:0)",
                "function": "Medium-chain saturated fatty acid (dominant lipid, 40-60% of total FA)",
                "extraction_method": "Mechanical pressing, solvent extraction",
                "bioactivity": "Potent antimicrobial (disrupts bacterial membranes), antiviral (enveloped viruses)",
                "pef_relevance": "PEF enhances oil release from larval cells, improving yield"
            },
            {
                "name": "Antimicrobial Peptides (AMPs: defensins, cecropins)",
                "function": "Innate immune defense molecules (cationic, amphipathic)",
                "extraction_method": "Acid extraction, solid-phase extraction, or PEF-induced release",
                "bioactivity": "Broad-spectrum antimicrobial, antifungal, potential food preservative",
                "pef_relevance": "PEF can trigger AMP release and enhance recovery without thermal degradation"
            },
            {
                "name": "Calcium (Ca)",
                "function": "Highly bioavailable mineral (5-8% DW in prepupae)",
                "extraction_method": "Mineral extraction from exoskeleton",
                "bioactivity": "Bone health, muscle contraction, nerve signaling",
                "pef_relevance": "Minimal direct PEF relevance; focus on protein/lipid fractionation"
            },
            {
                "name": "Chitin & Chitosan",
                "function": "Exoskeleton biopolymer (8-12% DW)",
                "extraction_method": "Chemical or biological (fermentation-based) deproteinization",
                "bioactivity": "Biodegradable films, wound dressing, water treatment",
                "pef_relevance": "PEF pre-treatment may improve chitin purity by better protein removal"
            },
            {
                "name": "Soluble Proteins (albumins, globulins)",
                "function": "Water/salt-soluble protein fractions with functional properties",
                "extraction_method": "Sequential extraction (water, salt, alkaline) or PEF-assisted",
                "bioactivity": "Emulsification, gelation, foam stabilization in food matrices",
                "pef_relevance": "PEF significantly improves colloidal properties and emulsion stability"
            }
        ]
    },
    "Acheta domesticus (House Cricket)": {
        "description": "Most commercially farmed edible insect globally. Protein 60-70% DW. Mild flavor profile suitable for food applications.",
        "metabolites": [
            {
                "name": "Vitamin B12 (Cobalamin)",
                "function": "Essential water-soluble vitamin (5-10 ug/100g)",
                "extraction_method": "Bioavailability studies via simulated digestion",
                "bioactivity": "Neurological health, DNA synthesis, red blood cell formation",
                "pef_relevance": "PEF may enhance B12 bioaccessibility through cell disruption"
            },
            {
                "name": "Omega-3 (ALA) & Omega-6 (LA) PUFAs",
                "function": "Essential polyunsaturated fatty acids",
                "extraction_method": "Lipid extraction (Folch, Bligh & Dyer)",
                "bioactivity": "Cardiovascular health, brain function, anti-inflammatory",
                "pef_relevance": "PEF-assisted extraction preserves PUFA integrity (no thermal oxidation)"
            },
            {
                "name": "Myofibrillar Proteins",
                "function": "Structural proteins with high gelation and emulsification capacity",
                "extraction_method": "Salt extraction (0.5M NaCl) or alkaline solubilization",
                "bioactivity": "Texture formation, water-holding, emulsion stabilization",
                "pef_relevance": "PEF modifies protein conformation, improving gel strength and WHC"
            },
            {
                "name": "Iron (heme and non-heme forms)",
                "function": "Highly bioavailable iron (8-20 mg/100g DW)",
                "extraction_method": "Acid digestion + AAS/ICP-MS quantification",
                "bioactivity": "Oxygen transport, energy production, cognitive function",
                "pef_relevance": "PEF cell disruption may increase iron release from protein-mineral complexes"
            },
            {
                "name": "Fiber (Chitin-glucan complex)",
                "function": "Insoluble dietary fiber from exoskeleton",
                "extraction_method": "Enzymatic deproteinization",
                "bioactivity": "Gut health, prebiotic effect, cholesterol binding",
                "pef_relevance": "PEF may modify chitin-glucan structure for improved prebiotic activity"
            }
        ]
    },
    "Spirulina platensis (Cyanobacteria)": {
        "description": "Photosynthetic microorganism with 55-70% protein. Complete amino acid profile. Rich in unique pigments and antioxidants.",
        "metabolites": [
            {
                "name": "C-Phycocyanin",
                "function": "Blue chromoprotein pigment (light-harvesting complex)",
                "extraction_method": "Freeze-thaw, ultrasonication, or PEF cell disruption + aqueous extraction",
                "bioactivity": "Potent antioxidant, anti-inflammatory (COX-2 inhibitor), neuroprotective, anticancer",
                "pef_relevance": "PEF is the most promising green method for phycocyanin extraction (no solvents needed)"
            },
            {
                "name": "Complete Protein (phycocyanin + other)",
                "function": "All essential amino acids, high digestibility (85-95%)",
                "extraction_method": "Cell disruption (PEF, HPH, bead milling) + solubilization",
                "bioactivity": "Muscle building, immune support, complete nutrition",
                "pef_relevance": "PEF achieves 80-95% cell disruption at low energy input"
            },
            {
                "name": "Gamma-Linolenic Acid (GLA, C18:3 n-6)",
                "function": "Rare omega-6 PUFA (1-2% DW)",
                "extraction_method": "Lipid extraction after cell disruption",
                "bioactivity": "Anti-inflammatory (PGE1 precursor), skin health, hormonal balance",
                "pef_relevance": "PEF enables selective lipid release without full cell lysis"
            },
            {
                "name": "Sulfated Polysaccharides (Calcium Spirulan)",
                "function": "Cell wall polysaccharides with sulfate groups",
                "extraction_method": "Hot water extraction after cell disruption",
                "bioactivity": "Antiviral (HIV, HSV), immunomodulatory, anticoagulant",
                "pef_relevance": "PEF pre-treatment enhances polysaccharide release from cell walls"
            },
            {
                "name": "Beta-Carotene & Zeaxanthin",
                "function": "Provitamin A carotenoids and xanthophylls",
                "extraction_method": "Organic solvent or supercritical CO2 after cell disruption",
                "bioactivity": "Antioxidant, eye health (macular degeneration prevention), immune support",
                "pef_relevance": "PEF + DES combination enables green carotenoid extraction"
            }
        ]
    },
}


def list_materials() -> list:
    """Return list of all material names."""
    return list(RAW_MATERIALS.keys())


def get_material(name: str) -> dict:
    """Get full material data."""
    return RAW_MATERIALS.get(name, {})


def get_metabolites(name: str) -> list:
    """Get metabolites for a specific material."""
    return RAW_MATERIALS.get(name, {}).get("metabolites", [])


def search_by_keyword(keyword: str) -> list:
    """Search across all materials by keyword."""
    results = []
    kw = keyword.lower()
    for material_name, data in RAW_MATERIALS.items():
        for met in data.get("metabolites", []):
            searchable = f"{met['name']} {met['bioactivity']} {met['function']} {met['pef_relevance']}".lower()
            if kw in searchable:
                results.append({
                    "material": material_name,
                    "metabolite_name": met["name"],
                    "bioactivity": met["bioactivity"],
                    "pef_relevance": met["pef_relevance"],
                })
    return results
