# 🔐 Steganalysis Toolkit

A Python-based image steganalysis tool that analyzes images using statistical and frequency-domain techniques to identify patterns that may indicate hidden information.

The toolkit combines multiple analysis methods, including Least Significant Bit (LSB) analysis, Chi-Square analysis, Discrete Cosine Transform (DCT) analysis, and image statistics to provide a combined view of an image's characteristics.

## Features

-  **LSB Analysis** — Examines the distribution of least significant bits in image pixels.
-  **Chi-Square Analysis** — Compares paired pixel-value frequencies across RGB channels.
-  **DCT Analysis** — Examines 8×8 image blocks in the frequency domain.
-  **Image Statistics** — Calculates pixel mean, standard deviation, and entropy.
-  **Automated Summary** — Combines observations from the different analysis modules.
-  **Analysis Report** — Generates a downloadable text report containing the analysis results.
-  **Streamlit Interface** — Provides an interactive web interface for uploading and analyzing images.

## How It Works

1. Upload a PNG, JPG, or JPEG image through the Streamlit interface.
2. The image is converted into an RGB representation for analysis.
3. The toolkit performs LSB analysis to examine the distribution of least significant bits.
4. Chi-Square analysis evaluates paired pixel-value frequencies for each RGB channel.
5. DCT analysis processes the image in 8×8 blocks and measures frequency-domain characteristics.
6. Image statistics are calculated, including mean pixel value, pixel standard deviation, and entropy.
7. The results are combined into an automated analysis summary.
8. A text-based analysis report can be downloaded from the application.

## Project Structure

```text
Steganalysis-Toolkit/
├── app.py
├── requirements.txt
├── create_stego.py
├── README.md
├── .gitignore
└── analyzers/
    ├── lsb.py
    ├── chi_square.py
    ├── dct.py
    ├── statistics.py
    └── summary.py

Technologies Used
Python
Streamlit — Web interface
NumPy — Numerical and pixel-array processing
Pillow — Image loading and processing
SciPy — Statistical calculations
OpenCV — DCT and image processing
Methodology & Limitations

The toolkit uses multiple statistical indicators rather than relying on a single detection method.

LSB Analysis

The tool extracts the least significant bit from each RGB pixel value and measures the number and proportion of zero and one bits. It also calculates the absolute difference between the two proportions as an LSB imbalance measure.

Chi-Square Analysis

The implementation compares paired pixel-value frequencies within each RGB channel and calculates a chi-square statistic and corresponding p-value. Very small p-values indicate that the observed paired frequencies differ from the equal-frequency expectation under this test.

This implementation is intended as a simplified statistical indicator for educational and exploratory analysis. It should not be interpreted as a complete implementation of a production-grade steganalysis detector.

DCT Analysis

The image is converted to grayscale and divided into 8×8 blocks. A Discrete Cosine Transform is applied to each block, and descriptive statistics such as mean coefficient magnitude, standard deviation, maximum coefficient magnitude, and high-frequency energy ratio are calculated.

Image Statistics

The toolkit calculates basic image characteristics including mean pixel value, pixel standard deviation, and average per-channel entropy.

Limitations
Statistical indicators do not independently prove that an image contains hidden information.
Results can vary depending on image content, format, compression, and image processing history.
A balanced LSB distribution does not necessarily indicate steganography.
Chi-square results should be interpreted in the context of the image and the assumptions of the test.
DCT characteristics are descriptive features and should be compared with suitable reference images.
The current toolkit is intended for educational, experimental, and exploratory steganalysis rather than forensic certification.
Installation

Clone the repository and navigate into the project directory:

git clone https://github.com/Mvarsh726/Steganalysis-Toolkit.git
cd Steganalysis-Toolkit

Create and activate a virtual environment:

py -m venv venv
venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt
Usage


Start the Streamlit application:

streamlit run app.py

The application will open in your browser. Upload a PNG, JPG, or JPEG image to begin the analysis.

The results include LSB distribution, Chi-Square statistics, DCT characteristics, image statistics, and an automated analysis summary.
