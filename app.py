import streamlit as st
from PIL import Image

from analyzers.lsb import analyze_lsb
from analyzers.chi_square import analyze_chi_square
from analyzers.dct import analyze_dct
from analyzers.statistics import analyze_statistics
from analyzers.summary import generate_summary


st.set_page_config(
    page_title="Steganalysis Toolkit",
    page_icon=None,
    layout="wide"
)


# ============================================================
# PAGE STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background: #F3F0F7;
        color: #292536;
    }

    .block-container {
        max-width: 1350px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background: #E7E1EF;
        border-right: 1px solid #D4CDDF;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    .sidebar-title {
        color: #393143;
        font-size: 21px;
        font-weight: 750;
        letter-spacing: -0.3px;
    }

    .sidebar-subtitle {
        color: #766D80;
        font-size: 12px;
        margin-top: 5px;
        margin-bottom: 25px;
    }

    .sidebar-section {
        color: #81788A;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* ========================================================
       TYPOGRAPHY
       ======================================================== */

    h1 {
        color: #292536 !important;
        font-weight: 750 !important;
        letter-spacing: -0.8px;
    }

    h2 {
        color: #373144 !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #40394E !important;
        font-weight: 650 !important;
    }

    p {
        color: #625B6D;
    }

    /* ========================================================
       HERO
       ======================================================== */

    .hero-card {
        background: #E7E1EF;
        border: 1px solid #D4CDDF;
        border-radius: 18px;
        padding: 32px 36px;
        margin-bottom: 24px;
        box-shadow: 0 8px 25px rgba(66, 52, 82, 0.07);
    }

    .hero-label {
        color: #75658A;
        font-size: 11px;
        font-weight: 750;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }

    .hero-title {
        color: #2F2939;
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -1.2px;
        margin-bottom: 8px;
    }

    .hero-description {
        color: #6B6474;
        font-size: 15px;
        line-height: 1.6;
        max-width: 780px;
    }

    /* ========================================================
       ANALYSIS CARD
       ======================================================== */

    .analysis-card {
        background: #E7E1EF;
        border: 1px solid #D4CDDF;
        border-radius: 15px;
        padding: 20px 22px;
        margin: 12px 0 16px 0;
        box-shadow: 0 5px 18px rgba(66, 52, 82, 0.05);
    }

    .analysis-title {
        color: #4E4658;
        font-size: 17px;
        font-weight: 700;
    }

    .analysis-description {
        color: #81788A;
        font-size: 13px;
        margin-top: 4px;
    }

   /* ========================================================
      FILE UPLOADER
      ======================================================== */

   div[data-testid="stFileUploader"] {
    	background: #E7E1EF;
    	border: 1px solid #D4CDDF;
    	border-radius: 14px;
    	padding: 12px;
    	box-shadow: 0 5px 18px rgba(66, 52, 82, 0.05);
   }

   div[data-testid="stFileUploader"] section {
    	background: #E7E1EF;
    	border: none;
   }

   div[data-testid="stFileUploaderDropzone"] {
    	background: #F3F0F7 !important;
    	border: 1px dashed #B9AFC8 !important;
    	border-radius: 10px;
   }

   div[data-testid="stFileUploaderDropzoneInstructions"] {
    	color: #625B6D !important;
   }

   div[data-testid="stFileUploaderDropzoneInstructions"] * {
    	color: #625B6D !important;
   }

   div[data-testid="stFileUploader"] small {
    	color: #625B6D !important;
    	opacity: 1 !important;
   }

   div[data-testid="stFileUploader"] small * {
    	color: #625B6D !important;
   }

   /* ========================================================
      DOWNLOAD BUTTON
      ======================================================== */

   .stDownloadButton button {
    	background: #62527A !important;
    	color: #FFFFFF !important;
    	border: none !important;
    	border-radius: 9px !important;
    	font-weight: 650 !important;
    	min-height: 42px;
   }

   .stDownloadButton button p,
   .stDownloadButton button span {
    	color: #FFFFFF !important;
   }

   .stDownloadButton button:hover {
    	background: #514267 !important;
   }
   /* Hide Streamlit Deploy button */

   [data-testid="stAppDeployButton"] {
    	display: none !important;
   }
    /* ========================================================
       METRICS
       ======================================================== */

    div[data-testid="stMetric"] {
        background: #E7E1EF;
        border: 1px solid #D4CDDF;
        border-radius: 13px;
        padding: 15px 17px;
        box-shadow: 0 4px 14px rgba(66, 52, 82, 0.04);
    }

    div[data-testid="stMetricLabel"] {
        color: #81788A !important;
    }

    div[data-testid="stMetricValue"] {
        color: #3E3650 !important;
    }

    /* ========================================================
       BUTTONS
       ======================================================== */

    .stDownloadButton button {
        background: #62527A !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 9px !important;
        font-weight: 650 !important;
    }

    .stDownloadButton button:hover {
        background: #514267 !important;
    }

    /* ========================================================
       ALERTS
       ======================================================== */

    div[data-testid="stAlert"] {
        border-radius: 11px;
    }

    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;
        color: #958C9D;
        font-size: 11px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #D4CDDF;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">STEGANALYSIS LAB</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'Digital Image Security Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">Analysis Modules</div>',
        unsafe_allow_html=True
    )

    st.write("LSB Analysis")
    st.write("Chi-Square Analysis")
    st.write("DCT Analysis")
    st.write("Image Statistics")
    st.write("Automated Summary")

    st.markdown(
        '<div class="sidebar-section">Project</div>',
        unsafe_allow_html=True
    )

    st.caption("Python-based image steganalysis")
    st.caption("Statistical and frequency-domain analysis")
# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-label">DIGITAL IMAGE SECURITY</div>
        <div class="hero-title">Steganalysis Toolkit</div>
        <div class="hero-description">
            A multi-method analytical tool for examining digital
            images using statistical, pixel-level and
            frequency-domain characteristics.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# UPLOAD SECTION
# ============================================================

st.markdown(
    """
    <div class="analysis-card">
        <div class="analysis-title">Image Analysis</div>
        <div class="analysis-description">
            Upload an image to begin the analysis.
            Supported formats: PNG, JPG and JPEG.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Select an image",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)


# ============================================================
# WAITING STATE
# ============================================================

if uploaded_file is None:

    st.info(
        "Upload an image above to begin the analysis."
    )

    st.markdown(
        """
        <div class="footer">
            Steganalysis Toolkit · Statistical Image Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    st.stop()


# ============================================================
# LOAD IMAGE
# ============================================================

image = Image.open(uploaded_file).convert("RGB")


st.success(
    "Image loaded successfully. Analysis is ready."
)


# ============================================================
# IMAGE OVERVIEW
# ============================================================

stats_preview = analyze_statistics(image)

st.markdown("## Image Overview")

st.caption(
    "Basic properties of the uploaded image."
)


preview_col, details_col = st.columns(
    [1.2, 1],
    gap="large"
)


with preview_col:

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )


with details_col:

    st.markdown("### File Information")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Width",
            f'{stats_preview["width"]:,} px'
        )

    with c2:
        st.metric(
            "Height",
            f'{stats_preview["height"]:,} px'
        )

    c3, c4 = st.columns(2)

    with c3:
        st.metric(
            "Channels",
            stats_preview["channels"]
        )

    with c4:
        st.metric(
            "Format",
            uploaded_file.type.split("/")[-1].upper()
        )


# ============================================================
# LSB ANALYSIS
# ============================================================

st.markdown("## LSB Analysis")

st.caption(
    "Examines the distribution of least significant bits "
    "across RGB pixel values."
)


lsb_results = analyze_lsb(image)


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.metric(
        "Total Bits",
        f'{lsb_results["total_bits"]:,}'
    )

with c2:
    st.metric(
        "Zero Bits",
        f'{lsb_results["zeros"]:,}'
    )

with c3:
    st.metric(
        "One Bits",
        f'{lsb_results["ones"]:,}'
    )

with c4:
    st.metric(
        "LSB Imbalance",
        f'{lsb_results["imbalance"]:.2%}'
    )
# ============================================================
# CHI-SQUARE ANALYSIS
# ============================================================

st.markdown("## Chi-Square Analysis")

st.caption(
    "Evaluates paired pixel-value frequencies across "
    "the red, green and blue channels."
)


chi_results = analyze_chi_square(image)


for channel, result in chi_results.items():

    p_value = result["p_value"]

    if p_value < 0.000001:
        p_value_display = "< 0.000001"
    else:
        p_value_display = f"{p_value:.6f}"

    if p_value < 0.05:
        interpretation = "Statistically unusual distribution"
    else:
        interpretation = "No significant difference detected"

    st.markdown(f"### {channel} Channel")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Chi-Square Statistic",
            f'{result["chi_square"]:.2f}'
        )

    with c2:
        st.metric(
            "P-Value",
            p_value_display
        )

    with c3:
        st.metric(
            "Significance Level",
            "Below 5%" if p_value < 0.05 else "Above 5%"
        )

    st.caption(
        f"Interpretation: {interpretation}"
    )


# ============================================================
# DCT ANALYSIS
# ============================================================

st.markdown("## DCT Analysis")

st.caption(
    "Examines frequency-domain characteristics using "
    "8×8 Discrete Cosine Transform blocks."
)


dct_results = analyze_dct(image)


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.metric(
        "Mean Coefficient",
        f'{dct_results["mean_dct"]:.2f}'
    )

with c2:
    st.metric(
        "Standard Deviation",
        f'{dct_results["std_dct"]:.2f}'
    )

with c3:
    st.metric(
        "Maximum Coefficient",
        f'{dct_results["max_dct"]:.2f}'
    )

with c4:
    st.metric(
        "High-Frequency Energy",
        f'{dct_results["high_frequency_ratio"]:.2%}'
    )


# ============================================================
# IMAGE STATISTICS
# ============================================================

st.markdown("## Image Statistics")

st.caption(
    "Descriptive statistical characteristics of the image pixels."
)


stats_results = analyze_statistics(image)


c1, c2, c3 = st.columns(3)


with c1:
    st.metric(
        "Mean Pixel Value",
        f'{stats_results["mean_pixel"]:.2f}'
    )

with c2:
    st.metric(
        "Pixel Standard Deviation",
        f'{stats_results["std_pixel"]:.2f}'
    )

with c3:
    st.metric(
        "Average Entropy",
        f'{stats_results["entropy"]:.2f}'
    )


# ============================================================
# AUTOMATED SUMMARY
# ============================================================

st.markdown("## Automated Summary")

st.caption(
    "Combined interpretation of the implemented analysis methods."
)


summary = generate_summary(
    lsb_results,
    chi_results,
    dct_results,
    stats_results
)


st.success(
    summary["status"]
)

st.write(
    summary["message"]
)

st.warning(
    summary["disclaimer"]
)


# ============================================================
# OVERALL ASSESSMENT
# ============================================================

st.markdown("## Overall Assessment")


significant_channels = [
    channel
    for channel, result in chi_results.items()
    if result["p_value"] < 0.05
]


if (
    lsb_results["imbalance"] < 0.02
    and not significant_channels
):

    assessment_title = "No Strong Statistical Indicators"

    assessment_text = (
        "The analyzed image does not show strong statistical "
        "indicators from the implemented methods. This does not "
        "prove that the image contains no hidden information."
    )

elif significant_channels:

    assessment_title = "Statistical Anomalies Detected"

    assessment_text = (
        "One or more statistical indicators differ from the "
        "expected patterns used by the implemented tests. "
        "Further investigation and comparison with reference "
        "images may be useful."
    )

else:

    assessment_title = "Mixed Statistical Indicators"

    assessment_text = (
        "The analysis produced a combination of statistical "
        "observations. These results should be interpreted "
        "together with the image characteristics and reference "
        "images."
    )


st.info(
    f"**{assessment_title}**\n\n"
    f"{assessment_text}"
)


# ============================================================
# ANALYSIS REPORT
# ============================================================

st.markdown("## Analysis Report")

st.caption(
    "Export the complete analysis results as a text file."
)


report = f"""
STEGANALYSIS TOOLKIT
====================

FILE INFORMATION
----------------
File: {uploaded_file.name}
Image Size: {stats_results["width"]} x {stats_results["height"]}
Channels: {stats_results["channels"]}

LSB ANALYSIS
------------
Total Bits: {lsb_results["total_bits"]}
Zero Bits: {lsb_results["zeros"]}
One Bits: {lsb_results["ones"]}
Zero Ratio: {lsb_results["zeros_ratio"]:.4%}
One Ratio: {lsb_results["ones_ratio"]:.4%}
LSB Imbalance: {lsb_results["imbalance"]:.4%}

CHI-SQUARE ANALYSIS
-------------------
"""


for channel, result in chi_results.items():

    report += (
        f"{channel} Channel\n"
        f"Chi-Square Statistic: "
        f"{result['chi_square']:.6f}\n"
        f"P-Value: {result['p_value']:.10e}\n\n"
    )


report += f"""
DCT ANALYSIS
------------
Mean Coefficient: {dct_results["mean_dct"]:.4f}
Standard Deviation: {dct_results["std_dct"]:.4f}
Maximum Coefficient: {dct_results["max_dct"]:.4f}
High-Frequency Energy Ratio:
{dct_results["high_frequency_ratio"]:.4%}

IMAGE STATISTICS
----------------
Mean Pixel Value: {stats_results["mean_pixel"]:.4f}
Pixel Standard Deviation: {stats_results["std_pixel"]:.4f}
Average Entropy: {stats_results["entropy"]:.4f}

AUTOMATED SUMMARY
-----------------
{summary["message"]}

DISCLAIMER
----------
{summary["disclaimer"]}

OVERALL ASSESSMENT
------------------
{assessment_title}

{assessment_text}
"""


st.download_button(
    label="Download Analysis Report",
    data=report,
    file_name="steganalysis_report.txt",
    mime="text/plain",
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Steganalysis Toolkit · Statistical Image Analysis
    </div>
    """,
    unsafe_allow_html=True
)