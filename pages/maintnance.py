import streamlit as st

st.set_page_config(
    page_title="Project Not Available",
    page_icon="🚧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling matching the main portfolio red/dark aesthetic
st.markdown("""
<style>
#MainMenu, header, footer {
    visibility: hidden !important;
}

body {
    background: radial-gradient(circle at center, #450005 0%, #170002 85%, #080001 100%) !important;
    color: #ffffff;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
}

.maintenance-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 75vh;
    text-align: center;
    padding: 20px;
}

.status-badge {
    display: inline-block;
    background: rgba(255, 42, 42, 0.15);
    border: 1px solid rgba(255, 42, 42, 0.4);
    color: #ff4d4d;
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 20px;
}

.maintenance-title {
    font-size: 2.8rem;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 15px;
    color: #ffffff;
}

.maintenance-text {
    font-size: 1.1rem;
    color: #d1d1d1;
    max-width: 550px;
    line-height: 1.6;
    margin-bottom: 30px;
}

.back-button {
    display: inline-block;
    background: linear-gradient(135deg, #d31010, #800005);
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-decoration: none !important;
    padding: 12px 28px;
    border-radius: 8px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.back-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(255, 42, 42, 0.3);
}
</style>
""", unsafe_allow_html=True)

maintenance_html = """<div class="maintenance-container">
<div class="maintenance-title">Project not available come back later</div>
<a href="/" class="back-button" target="_self">Back to Portfolio</a>
</div>"""

st.markdown(maintenance_html, unsafe_allow_html=True)