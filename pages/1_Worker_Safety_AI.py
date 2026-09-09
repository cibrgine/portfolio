import streamlit as st
import requests
import io

st.set_page_config(
    page_title="Worker Safety AI - Details",
    page_icon="🦺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# CONFIGURATION & REPOSITORY DETAILS
# -------------------------------------------------------------
# Replace with your actual GitHub username and repository name
GITHUB_USER = "your-username"
GITHUB_REPO = "worker-safety-ai"  # Or your specific repo name
GITHUB_REPO_URL = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}"

# Raw file path for remote fetching
RAW_METRICS_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/models/checkpoints/cv_metrics_report.csv"

# Fallback metric data in case the remote repo/file is private or unreachable
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
        response = requests.get(RAW_METRICS_URL, timeout=5)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass
    return FALLBACK_CSV.encode("utf-8")

# -------------------------------------------------------------
# CUSTOM CSS (Matches app.py Theme + Low-Contrast Yellow Buttons)
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

/* Header link styling */
.nav-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
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

/* Page Title */
.project-title {
    font-size: 2.3rem;
    font-weight: 900;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #ffffff;
    margin-bottom: 0.5rem;
}

/* Content Container Cards */
.content-box {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 1.8rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
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
}
.yellow-btn-link:hover {
    background-color: #ecc05e;
    box-shadow: 0 6px 20px rgba(216, 162, 56, 0.45);
    transform: translateY(-2px);
}

/* Override native Streamlit Download Button to match yellow theme */
div.stDownloadButton > button {
    background-color: #d8a238 !important;
    color: #1a0003 !important;
    font-weight: 800 !important;
    font-size: 0.82rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border-radius: 30px !important;
    padding: 10px 24px !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(216, 162, 56, 0.25) !important;
    transition: all 0.3s ease !important;
}
div.stDownloadButton > button:hover {
    background-color: #ecc05e !important;
    box-shadow: 0 6px 20px rgba(216, 162, 56, 0.45) !important;
    transform: translateY(-2px);
    color: #1a0003 !important;
}

/* Clean markdown tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
}
th, td {
    padding: 10px 14px;
    border: 1px solid rgba(255, 255, 255, 0.12);
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
# TOP NAVIGATION
# -------------------------------------------------------------
st.markdown(
    """
    <div class="nav-header">
        <a href="/">← Return to Portfolio</a>
        <span>Worker Safety Detection</span>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# HEADER & VERSION SELECTOR
# -------------------------------------------------------------
col_title, col_actions = st.columns([1.6, 1.0], vertical_alignment="center")

with col_title:
    version_choice = st.selectbox(
        "Release Version",
        options=["v1.0", "v1.1", "v1.2"],
        index=0,
        label_visibility="collapsed"
    )
    st.markdown(f'<div class="project-title">YOLO Worker Safety AI ({version_choice})</div>', unsafe_allow_html=True)

with col_actions:
    col_btn, col_select = st.columns([1, 1], vertical_alignment="center")
    with col_btn:
        st.markdown(
            f'<a href="{GITHUB_REPO_URL}" target="_blank" class="yellow-btn-link">See in GitHub</a>',
            unsafe_allow_html=True
        )
    with col_select:
        # Visual label for versioning
        st.caption("Active Release: " + version_choice)

st.write("")

# -------------------------------------------------------------
# DYNAMIC VERSION CONTENT
# -------------------------------------------------------------
if version_choice == "v1.0":
    st.markdown("""
    <div class="content-box">
        <h3>Overview</h3>
        <p>The <b>YOLO Worker Safety AI</b> project detects personal protective equipment (PPE) and compliance/non-compliance states on construction-site workers. It leverages <b>YOLOv11-m</b> fine-tuned on a <i>Construction-PPE</i> dataset via an automated pipeline: acquisition, letter-box preprocessing, 5-fold cross-validation, and multi-threshold evaluation.</p>
    </div>
    """, unsafe_allow_html=True)

    # MODEL & PREPROCESSING
    st.markdown("""
    <div class="content-box">
        <h3>Model Choice & Dataset</h3>
        <p><b>Target Classes (11 total):</b> <code>helmet</code> (0), <code>gloves</code> (1), <code>vest</code> (2), <code>boots</code> (3), <code>goggles</code> (4), <code>none</code> (5), <code>Person</code> (6), <code>no_helmet</code> (7), <code>no_goggle</code> (8), <code>no_gloves</code> (9), and <code>no_boots</code> (10).</p>
        <p><b>Why YOLOv11-m:</b> Selected over YOLOv8 for refined C3k2 and SPPF feature extractors, maintaining high localization accuracy for small accessories (gloves, goggles) while running at real-time speeds (~15.9 ms per frame).</p>
        <hr style="border: 0.5px solid rgba(255,255,255,0.1); margin: 15px 0;">
        <h4>Preprocessing Pipeline (<code>preprocess.py</code>)</h4>
        <ul>
            <li><b>Automated Download:</b> Fetches <code>construction-ppe.zip</code> from release assets.</li>
            <li><b>Letter-box Resizing:</b> Standardizes inputs to 640×640 with border padding (gray 114) preserving aspect ratios.</li>
            <li><b>Splits:</b> Creates a 20% holdout test set and stratified 5-fold cross-validation splits.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # TRAINING PIPELINE
    st.markdown("""
    <div class="content-box">
        <h3>Training Workflow (<code>train.py</code>)</h3>
        <ul>
            <li><b>Hardware:</b> NVIDIA GeForce RTX 3060 Laptop GPU (CUDA 12.1).</li>
            <li><b>Hyperparameters:</b> 30 epochs/fold, Batch Size 8, Resolution 640×640.</li>
            <li><b>Process:</b> Iteratively fine-tunes across all 5 folds, exports validation reports, and preserves optimal weights to <code>models/checkpoints/best.pt</code>.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # EVALUATION & METRICS
    st.markdown("""
    <div class="content-box">
        <h3>Evaluation & Performance</h3>
        <h4>5-Fold Cross-Validation Aggregate</h4>
        <table>
            <tr><th>Metric</th><th>Fold 0</th><th>Fold 1</th><th>Fold 2</th><th>Fold 3</th><th>Fold 4</th><th>Mean</th></tr>
            <tr><td><b>Precision</b></td><td>0.7112</td><td>0.7201</td><td>0.6496</td><td>0.7270</td><td>0.6477</td><td><b>0.6911</b></td></tr>
            <tr><td><b>Recall</b></td><td>0.6568</td><td>0.7167</td><td>0.6858</td><td>0.6472</td><td>0.6616</td><td><b>0.6736</b></td></tr>
            <tr><td><b>F1-Score</b></td><td>0.6830</td><td>0.7184</td><td>0.6672</td><td>0.6848</td><td>0.6546</td><td><b>0.6816</b></td></tr>
            <tr><td><b>mAP@0.50</b></td><td>0.6826</td><td>0.7431</td><td>0.6771</td><td>0.6921</td><td>0.6646</td><td><b>0.6919</b></td></tr>
            <tr><td><b>mAP@0.50:0.95</b></td><td>0.3461</td><td>0.3518</td><td>0.3282</td><td>0.3302</td><td>0.3235</td><td><b>0.3360</b></td></tr>
        </table>
        <br>
        <h4>Class-Wise Bottlenecks & Strengths</h4>
        <ul>
            <li><b>Top Performers:</b> <code>helmet</code> (mAP50: 0.9501), <code>Person</code> (0.9146), <code>vest</code> (0.9026).</li>
            <li><b>Underrepresented Classes:</b> <code>no_boots</code> (10 instances, mAP50: 0.1590) and <code>no_helmet</code> (82 instances, mAP50: 0.4131).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # DOWNLOAD BUTTON SECTION (Directly following evaluation)
    csv_bytes = fetch_metrics_file()
    col_dl, _ = st.columns([1.5, 2])
    with col_dl:
        st.download_button(
            label="Download History of Metrics (CSV)",
            data=csv_bytes,
            file_name="cv_metrics_report.csv",
            mime="text/csv",
            help="Click to download the 5-fold cross validation summary report directly from the repository."
        )

    # REPOSITORY STRUCTURE & FIXES
    st.markdown("""
    <div class="content-box" style="margin-top: 1.8rem;">
        <h3>Future Optimizations</h3>
        <ul>
            <li><b>Class Balancing:</b> Augmenting negative compliance cases (CutMix, Mosaic) and adjusting class loss weights.</li>
            <li><b>High-Res Ingestion:</b> Training on 1024×1024 frames to enhance small-object bounding boxes (goggles, gloves).</li>
            <li><b>Runtime Deployment:</b> Exporting checkpoint weights to TensorRT (.engine) for sub-10ms inference.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

else:
    # Future version placeholders
    st.markdown(f"""
    <div class="content-box">
        <h3>Version {version_choice} (In Development)</h3>
        <p>Documentation, checkpoints, and benchmark evaluations for release <b>{version_choice}</b> will be logged here upon completion of fine-tuning runs.</p>
    </div>
    """, unsafe_allow_html=True)