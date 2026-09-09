import streamlit as st
import random
import requests

st.set_page_config(
    page_title="Worker Safety AI - Details",
    page_icon="🦺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# REPOSITORY SETTINGS & DATA
# -------------------------------------------------------------
GITHUB_USER = "your-username"
GITHUB_REPO = "worker-safety-ai"
GITHUB_REPO_URL = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}"
RAW_METRICS_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/models/checkpoints/cv_metrics_report.csv"

FALLBACK_CSV = """Fold,Precision,Recall,F1-Score,mAP50,mAP50-95
Fold 0,0.7112,0.6568,0.6830,0.6826,0.3461
Fold 1,0.7201,0.7167,0.7184,0.7431,0.3518
Fold 2,0.6496,0.6858,0.6672,0.6771,0.3282
Fold 3,0.7270,0.6472,0.6848,0.6921,0.3302
Fold 4,0.6477,0.6616,0.6546,0.6646,0.3235
Mean,0.6911,0.6736,0.6816,0.6919,0.3360
"""

@st.cache_data(ttl=3600)
def fetch_metrics_file() -> bytes:
    try:
        response = requests.get(RAW_METRICS_URL, timeout=4)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass
    return FALLBACK_CSV.encode("utf-8")

TAG_GRADIENTS = [
    "linear-gradient(135deg, #1e3c72, #2a5298)",
    "linear-gradient(135deg, #3a1c71, #d76d77)",
    "linear-gradient(135deg, #4776e6, #8e54e9)",
    "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
    "linear-gradient(135deg, #654ea3, #eaafc8)",
    "linear-gradient(135deg, #2b5876, #4e4376)",
    "linear-gradient(135deg, #134e5e, #71b280)"
]

def make_gradient_tag(label: str) -> str:
    grad = random.choice(TAG_GRADIENTS)
    return f'<span class="tech-tag" style="background: {grad}; margin: 3px 4px; display: inline-block;">{label}</span>'

# -------------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------------
custom_css = """
<style>
#MainMenu, header, footer {
    visibility: hidden !important;
}
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1100px !important;
}
body {
    background: radial-gradient(circle at center, #450005 0%, #170002 85%, #080001 100%) !important;
    color: #f1f1f1;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
}

/* Nav header */
.nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.nav-header a {
    color: #f1f1f1;
    text-decoration: none;
    transition: color 0.3s ease;
}
.nav-header a:hover {
    color: #e5b94c;
}

/* Titles and content boxes */
.project-title {
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #ffffff;
    margin: 0;
}
.content-box {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}
.content-box h3 {
    margin-top: 0;
    font-size: 1.25rem;
    color: #ecc05e;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Yellow Action Buttons */
.yellow-btn-link {
    display: inline-block;
    background-color: #d8a238;
    color: #1a0003 !important;
    font-weight: 800;
    font-size: 0.82rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 10px 22px;
    border-radius: 30px;
    text-decoration: none !important;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(216, 162, 56, 0.25);
    border: none;
    text-align: center;
    width: 100%;
}
.yellow-btn-link:hover {
    background-color: #ecc05e;
    box-shadow: 0 6px 20px rgba(216, 162, 56, 0.45);
    transform: translateY(-2px);
}

/* Streamlit Download Button to match Yellow Fiery Vibe */
div.stDownloadButton > button {
    background-color: #d8a238 !important;
    color: #1a0003 !important;
    font-weight: 800 !important;
    font-size: 0.82rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border-radius: 30px !important;
    padding: 12px 26px !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(216, 162, 56, 0.25) !important;
    transition: all 0.3s ease !important;
}
div.stDownloadButton > button:hover {
    background-color: #ecc05e !important;
    box-shadow: 0 6px 22px rgba(216, 162, 56, 0.45) !important;
    transform: translateY(-2px);
    color: #1a0003 !important;
}

/* Streamlit Selectbox border */
div[data-baseweb="select"] {
    border-radius: 20px !important;
    border: 1px solid #d8a238 !important;
}

.tech-tag {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    padding: 4px 9px;
    border-radius: 6px;
    color: #ffffff;
    text-transform: uppercase;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}
th, td {
    padding: 9px 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    text-align: left;
}
th {
    background: rgba(216, 162, 56, 0.15);
    color: #ecc05e;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------------------------------------
# TOP NAVIGATION (Opens in same tab)
# -------------------------------------------------------------
st.markdown(
    """
    <div class="nav-header">
        <a href="/" target="_self">← Return to Portfolio</a>
        <span>Worker Safety Detection</span>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# HEADER: TITLE, REPOSITORY LINK, VERSION DROPDOWN
# -------------------------------------------------------------
col_title, col_actions = st.columns([1.7, 1.1], vertical_alignment="center")

with col_title:
    st.markdown('<div class="project-title">YOLO Worker Safety AI</div>', unsafe_allow_html=True)

with col_actions:
    col_btn, col_drop = st.columns([1, 1], vertical_alignment="center")
    with col_btn:
        st.markdown(
            f'<a href="{GITHUB_REPO_URL}" target="_blank" class="yellow-btn-link">See in GitHub</a>',
            unsafe_allow_html=True
        )
    with col_drop:
        version_choice = st.selectbox(
            "Version",
            options=["v1.0"],
            index=0,
            label_visibility="collapsed"
        )

st.write("")

# -------------------------------------------------------------
# BOX 1: OVERVIEW
# -------------------------------------------------------------
st.markdown(
    """
    <div class="content-box">
        <h3>Overview</h3>
        <p>The <b>YOLO Worker Safety AI</b> project detects personal protective equipment (PPE) and compliance/non-compliance states on construction-site workers. It leverages <b>YOLOv11-m</b> fine-tuned on a <i>Construction-PPE</i> dataset via an end-to-end computer-vision pipeline: dataset acquisition, automated letter-box preprocessing, 5-fold cross-validation split generation, GPU-accelerated fine-tuning, and comprehensive evaluation.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# BOX 2: DATASET & TARGET CLASSES
# -------------------------------------------------------------
classes_list = [
    "helmet (0)", "gloves (1)", "vest (2)", "boots (3)", "goggles (4)",
    "none (5)", "Person (6)", "no_helmet (7)", "no_goggle (8)",
    "no_gloves (9)", "no_boots (10)"
]
classes_tags_html = "".join(make_gradient_tag(cls) for cls in classes_list)
zip_tag = make_gradient_tag("construction-ppe.zip")
raw_dir_tag = make_gradient_tag("data/raw/")

st.markdown(
    f"""
    <div class="content-box">
        <h3>Dataset &amp; Target Classes</h3>
        <p>The dataset is downloaded directly from the Ultralytics assets repository ({zip_tag}) and extracted into {raw_dir_tag}.</p>
        <p><b>Target Classes (11 Total):</b></p>
        <div style="margin-top: 6px; margin-bottom: 12px;">{classes_tags_html}</div>
        <p style="font-size: 0.9rem; color: #ccc;">Consists of real-world worker images annotated with normalized bounding-box coordinates in standard YOLO text format.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# BOX 3: MODEL CHOICE
# -------------------------------------------------------------
yolo_badge = make_gradient_tag("YOLOv11-m")
c3k2_badge = make_gradient_tag("C3k2")
sppf_badge = make_gradient_tag("SPPF")

st.markdown(
    f"""
    <div class="content-box">
        <h3>Model Choice</h3>
        <p>We selected {yolo_badge} (<code>yolo11m.pt</code>, ~20M parameters, 67.8 GFLOPs) over older architectures like YOLOv8 for key reasons:</p>
        <ul>
            <li><b>Enhanced Feature Extraction:</b> Utilizes {c3k2_badge} blocks and {sppf_badge} pooling for cleaner multi-scale feature representation.</li>
            <li><b>Speed-Accuracy Trade-off:</b> Offers high localization precision on smaller accessories (gloves, goggles) while retaining real-time inference (~15.9 ms on GPU).</li>
            <li><b>Transfer Learning:</b> Fine-tuning COCO pre-trained weights accelerates convergence on the construction domain.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# BOX 4: PREPROCESSING PIPELINE
# -------------------------------------------------------------
prep_badge = make_gradient_tag("preprocess.py")
cfg_badge = make_gradient_tag("config.yaml")

st.markdown(
    f"""
    <div class="content-box">
        <h3>Preprocessing Pipeline</h3>
        <p>{prep_badge} handles dataset ingestion, image standardization, and stratified 5-fold split creation.</p>
        <ul>
            <li><b>Configuration:</b> Settings and dimensions loaded directly via {cfg_badge}.</li>
            <li><b>Letter-box Resizing:</b> Resizes images to 640×640 with border padding (gray value 114) preserving aspect ratio.</li>
            <li><b>Cross-Validation Split:</b> Separates a 20% holdout test set and builds 5 train/val folds using scikit-learn's <code>KFold</code> with fold-specific <code>data.yaml</code> files.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# BOX 5: TRAINING WORKFLOW
# -------------------------------------------------------------
train_badge = make_gradient_tag("train.py")

st.markdown(
    f"""
    <div class="content-box">
        <h3>Training Workflow</h3>
        <p>{train_badge} performs 5-fold cross-validation fine-tuning of YOLOv11-m.</p>
        <ul>
            <li><b>Hardware Acceleration:</b> Automatically uses CUDA (NVIDIA GeForce RTX 3060 Laptop GPU).</li>
            <li><b>Hyperparameters:</b> 30 epochs per fold, Batch Size 8, Resolution 640×640.</li>
            <li><b>Execution:</b> Trains each fold sequentially, exports validation metric reports, and saves the top-performing fold weights to <code>models/checkpoints/best.pt</code>.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# BOX 6: EVALUATION & PERFORMANCE + DOWNLOAD BUTTON
# -------------------------------------------------------------
st.markdown(
    """
    <div class="content-box">
        <h3>Evaluation &amp; Performance</h3>
        <h4>5-Fold Cross-Validation Summary</h4>
        <table>
            <tr><th>Fold</th><th>Precision (P)</th><th>Recall (R)</th><th>F1-Score</th><th>mAP@0.50</th><th>mAP@0.50:0.95</th></tr>
            <tr><td>Fold 0</td><td>0.7112</td><td>0.6568</td><td>0.6830</td><td>0.6826</td><td>0.3461</td></tr>
            <tr><td>Fold 1</td><td>0.7201</td><td>0.7167</td><td>0.7184</td><td>0.7431</td><td>0.3518</td></tr>
            <tr><td>Fold 2</td><td>0.6496</td><td>0.6858</td><td>0.6672</td><td>0.6771</td><td>0.3282</td></tr>
            <tr><td>Fold 3</td><td>0.7270</td><td>0.6472</td><td>0.6848</td><td>0.6921</td><td>0.3302</td></tr>
            <tr><td>Fold 4</td><td>0.6477</td><td>0.6616</td><td>0.6546</td><td>0.6646</td><td>0.3235</td></tr>
            <tr><td><b>Mean</b></td><td><b>0.6911</b></td><td><b>0.6736</b></td><td><b>0.6816</b></td><td><b>0.6919</b></td><td><b>0.3360</b></td></tr>
        </table>
        <br>
        <h4>Class-Wise Bottlenecks &amp; Strengths</h4>
        <ul>
            <li><b>High Precision:</b> <code>helmet</code> (mAP50: 0.9501), <code>Person</code> (0.9146), <code>vest</code> (0.9026).</li>
            <li><b>Severe Scarcity:</b> <code>no_boots</code> (10 instances, mAP50: 0.1590) and <code>no_helmet</code> (82 instances, mAP50: 0.4131).</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Download Button Directly Under Evaluation
metrics_data = fetch_metrics_file()
dl_col, _ = st.columns([1.6, 2.0])
with dl_col:
    st.download_button(
        label="Download the history of metrics by version",
        data=metrics_data,
        file_name="cv_metrics_report_v1.0.csv",
        mime="text/csv"
    )

st.write("")

# -------------------------------------------------------------
# BOX 7: FUTURE OPTIMIZATIONS
# -------------------------------------------------------------
st.markdown(
    """
    <div class="content-box">
        <h3>Future Optimizations</h3>
        <ul>
            <li><b>Class Imbalance:</b> Targeted synthetic augmentations (Mosaic, CutMix) and loss-weight tuning on minority negative classes.</li>
            <li><b>High-Res Ingestion:</b> Train at 1024×1024 to refine bounding-box localization on fine items like goggles and gloves.</li>
            <li><b>Inference Acceleration:</b> Export model weights to TensorRT (.engine) for low-latency edge deployment.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)