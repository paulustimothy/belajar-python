# 🐍 Belajar Python Projects

A collection of Python projects demonstrating various applications of AI and machine learning. This repository contains three distinct projects that showcase different aspects of Python programming, AI integration, and web application development. 🚀

### 1. 🖼️ Image Classifier

A web-based image classification application built with Streamlit and TensorFlow. The application uses MobileNetV2, a pre-trained deep learning model, to classify images into 1000 different categories.

**✨ Features:**

- 🔍 Real-time image classification
- 🎨 User-friendly web interface
- 📊 Top 3 predictions with confidence scores
- 📁 Support for JPG and PNG formats

**🛠️ Technologies:**

- 🤖 TensorFlow
- 🌐 Streamlit
- 📸 OpenCV
- 🧠 MobileNetV2

### 2. 📃 Resume Critique

An AI-powered resume analysis tool that provides constructive feedback on resumes. The application uses Google's Gemini AI to analyze resume content and provide detailed recommendations.

**✨ Features:**

- 📄 PDF and TXT file support
- 🎯 Job role-specific analysis
- 📝 Comprehensive feedback on:
  - ✨ Content clarity and impact
  - 🎯 Skills presentation
  - 💼 Experience descriptions
  - 📈 Specific improvements for target roles

**🛠️ Technologies:**

- 🤖 Google Gemini AI
- 🌐 Streamlit
- 📑 PyPDF2

### 3. 🧮 Calculator

An AI-powered calculator that combines basic arithmetic operations with natural language processing. The application uses Google's Gemini AI to understand and process user queries in natural language.

**✨ Features:**

- 🗣️ Natural language input processing
- ➕ Basic arithmetic operations
- ⌨️ Interactive command-line interface
- 🤖 AI-powered response generation

**🛠️ Technologies:**

- 🤖 Google Gemini AI
- 🔗 LangChain
- 📊 LangGraph

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.x
- pip (Python package installer)
- Google API Key (for AI features)

### ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/paulustimothy/belajar-python.git
cd belajar-python
```

2. Install dependencies for all project:

```bash
# create virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate     # On Windows

# install all dependencies
pip install -r requirements.txt
```

3. Set up environment variables:
   Create a `.env` file in the respective project directories with:

```bash
GOOGLE_API_KEY=your_api_key_here
```

### Running the Projects

#### 🖼️ Image Classifier

```bash
cd image-classifier
uv run streamlit run main.py
```

#### 📃 Resume Critique

```bash
cd resume-critique
uv run streamlit run main.py
```

#### 🧮 Calculator

```bash
cd calculator
uv run main.py
```

Special thanks to Tech With Tim
