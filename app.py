import streamlit as st
import base64
import os
import random
import textwrap

st.set_page_config(
    page_title="Amine Lassri's Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# 1. CONFIGURATION & PLACEHOLDER DATA
# -------------------------------------------------------------
CONTACT_EMAIL = "cibrgine@gmail.com"

TAG_GRADIENTS = [
    "linear-gradient(135deg, #1e3c72, #2a5298)",
    "linear-gradient(135deg, #3a1c71, #d76d77)",
    "linear-gradient(135deg, #4776e6, #8e54e9)",
    "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
    "linear-gradient(135deg, #654ea3, #eaafc8)",
    "linear-gradient(135deg, #2b5876, #4e4376)",
    "linear-gradient(135deg, #134e5e, #71b280)"
]

PROJECTS = [
    {
        "id": 2,
        "title": "Auto Predictive Maintenance",
        "desc": "Conception et conteneurisation d'un pipeline MLOps de maintenance prédictive sous Docker, intégrant le réentraînement continu via GitHub Actions et l'ingestion de données en temps réel.",
        "tech": ["Python", "PyTorch", "Docker", "GitHub Actions", "Apache Airflow",  "Apache Kafka", "PostgreSQL", "uv" ,"Git"],
        "link": "/pages/Maintenance",
        "image_path": "assets/project1.jpg"
    },
    {
        "id": 1,
        "title": "Worker Safety AI",
        "desc": "Développement et déploiement d'une solution temps réel de détection d'EPI (YOLOv11-m, OpenCV, Streamlit), optimisant la conformité sécurité avec gestion des classes positives et négatives.",
        "tech": ["Python", "OpenCV", "Ultralytics YOLO (YOLOv11)", "PyTorch", "NumPy & Pandas", "Streamlit", "Scikit-learn"],
        "link": "/Worker_Safety_AI",  # Points to the new page in pages/
        "image_path": "assets/project2.jpg"
    },
    {
        "id": 3,
        "title": "LEGAL RAG AI",
        "desc": " Conception et déploiement d'un pipeline RAG hybride (recherche dense et BM25, reranking Cross-Encoder) pour l'analyse de conformité contractuelle, intégrant une suite d'évaluation quantitative de la fidélité et du rappel de contexte (Ragas).",
        "tech": ["Python", "LangChain / LlamaIndex", "BM25 (Rank-BM25)", "Dense Vector Embeddings",  "Vector Database (FAISS / Qdrant / ChromaDB)", "Cross-Encoder Reranking (Sentence-Transformers)", "Large Language Models (LLMs)", "Ragas (Retrieval Augmented Generation Assessment)", "Hugging Face Transformers"],
        "link": "/pages/Maintenance",
        "image_path": "assets/project3.jpg"
    },
    {
        "id": 4,
        "title": "DomainLLM Adapt",
        "desc": "Fine-tuning supervisé et efficace (QLoRA, PEFT) d'un LLM open-source pour l'extraction structurée de données métier, optimisé par quantification pour inférence à faible empreinte mémoire et servi via une API haute performance.",
        "tech": [ "Python", "PyTorch",  "Hugging Face Transformers",  "PEFT (Parameter-Efficient Fine-Tuning)", "QLoRA",  "BitsAndBytes", "TRL (Transformer Reinforcement Learning / SFTTrainer)",  "Hugging Face Datasets",  "Accelerate",  "Pydantic",  "Instructor",  "vLLM",    "FastAPI", "Uvicorn",  "Docker"],
        "link": "/pages/Maintenance",
        "image_path": "assets/project4.jpg"
    },
]

def get_image_html(image_path: str, fallback_label: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            mime = "image/png" if image_path.endswith(".png") else "image/jpeg"
            return f'<img src="data:{mime};base64,{encoded}" class="card-bg" alt="{fallback_label}" />'
    return f'<div class="fallback-image">{fallback_label}</div>'

# -------------------------------------------------------------
# 2. CUSTOM CSS
# -------------------------------------------------------------
custom_css = """
<style>
#MainMenu, header, footer {
    visibility: hidden !important;
}
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

body {
    background: radial-gradient(circle at center, #450005 0%, #170002 85%, #080001 100%) !important;
    color: #ffffff;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
}

.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 1.5px;
}
.header-left {
    color: #f1f1f1;
}
.header-right a {
    color: #f1f1f1;
    text-decoration: none;
    transition: color 0.3s ease, text-shadow 0.3s ease;
}
.header-right a:hover {
    color: #00d2ff;
    text-shadow: 0 0 10px rgba(0, 210, 255, 0.7);
}

.main-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 2.5rem;
    text-transform: uppercase;
}

.projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    width: 100%;
}

@media (max-width: 768px) {
    .projects-grid {
        grid-template-columns: 1fr;
    }
}

.card-wrapper {
    position: relative;
    width: 100%;
    height: 280px;
    border-radius: 20px;
    overflow: hidden;
    cursor: pointer;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
    background: linear-gradient(135deg, #d31010, #800005);
    text-decoration: none !important;
    display: block;
}

.card-bg {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: filter 0.4s ease, transform 0.4s ease;
    display: block;
}
.fallback-image {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2.1rem;
    font-weight: 900;
    color: #ffffff;
    text-decoration: underline;
    text-underline-offset: 8px;
    transition: filter 0.4s ease, transform 0.4s ease;
}

.card-wrapper:hover .card-bg,
.card-wrapper:hover .fallback-image {
    filter: blur(12px) brightness(0.45);
    transform: scale(1.05);
}

.card-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    opacity: 0;
    transition: opacity 0.35s ease-in-out;
    background: rgba(0, 0, 0, 0.3);
    z-index: 2;
}

.card-wrapper:hover .card-overlay {
    opacity: 1;
}

.project-name {
    font-size: 1.35rem;
    font-weight: 900;
    letter-spacing: 1px;
    margin-bottom: 8px;
    text-transform: uppercase;
    color: #ffffff;
}

.project-desc {
    font-size: 0.85rem;
    line-height: 1.35;
    color: #eaeaea;
    margin-bottom: 14px;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}

.tech-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.tech-tag {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    padding: 5px 10px;
    border-radius: 6px;
    color: #ffffff;
    text-transform: uppercase;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------------------
# 3. HTML MARKUP RENDERING (No Indentation)
# -------------------------------------------------------------
header_html = f"""<div class="header-bar">
<div class="header-left">AI &amp; DATA ENGINEER</div>
<div class="header-right"><a href="mailto:{CONTACT_EMAIL}">CONTACT ME</a></div>
</div>
<div class="main-title">AMINE LASSRI'S PORTFOLIO</div>"""

st.markdown(header_html, unsafe_allow_html=True)

cards_markup = ""
for item in PROJECTS:
    image_content = get_image_html(item["image_path"], f"IMAGE {item['id']}")
    
    tags_html = "".join(
        f'<span class="tech-tag" style="background: {random.choice(TAG_GRADIENTS)};">{tech}</span>'
        for tech in item["tech"]
    )

    card_str = f"""<a class="card-wrapper" href="{item['link']}" target="_blank">
{image_content}
<div class="card-overlay">
<div class="project-name">{item['title']}</div>
<div class="project-desc">{item['desc']}</div>
<div class="tech-container">
{tags_html}
</div>
</div>
</a>"""
    cards_markup += card_str

grid_html = f"""<div class="projects-grid">
{cards_markup}
</div>"""

st.markdown(grid_html, unsafe_allow_html=True)