# 📄 Invoice-Extractor-Gemini

**Invoice-Extractor-Gemini** is an AI-powered tool that enables users to upload invoice documents (images, PDFs, scans) in **any language**, and extract key information by simply asking natural language questions. It combines **Google Cloud Vision** for OCR and a **Large Language Model (LLM)** (such as Gemini or GPT-4) for semantic understanding, making invoice processing smarter and more flexible.

---

## 🚀 Features

- 🖼️ **Multi-Format Upload**  
  Upload invoices in formats like `.jpg`, `.png`, `.pdf`, or scanned documents.

- 🧠 **Prompt-Based Data Extraction**  
  Ask natural language questions and receive context-aware answers:
  - *"Who is this invoice addressed to?"*
  - *"What is the total amount?"*
  - *"कुल राशि क्या है?"* (What is the total amount?)

- 🌐 **Multi-Language Support**  
  Upload invoices in any language and ask questions in your preferred language — the system intelligently extracts answers across languages.

- 🔍 **Google Vision OCR Integration**  
  Accurate optical character recognition to extract raw text from invoices in multiple languages and formats.


---

## 🧠 Use Cases

- Automate invoice data entry and processing
- Extract invoice details from multilingual global vendors
- Integrate with accounting systems for smarter document intake
- Ask ad-hoc, conversational questions instead of relying on static templates

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **OCR:** Google Cloud Vision API
- **LLM:** Gemini Pro
- **Multilingual NLP:** Built-in LLM multilingual capabilities

---

## 🔧 Requirements

- Google Gemini API credentials
- Environment setup with required packages (see below)

---

## 🧪 Example Prompt Flow

1. **Upload Invoice (PDF/Image)**
2. **Ask a question**, such as:
   - “What is the due date?”
   - “Who issued the invoice?”
   - “Fakturadatum?” *(Invoice date in Swedish)*
3. **Receive Answer** extracted from document via LLM.

---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/SinghRobinKumar/Invoice-Extractor-Gemini.git
cd Invoice-Extractor-Gemini

# Install dependencies
pip install -r requirements.txt

# Add your API keys
# - Google Gemini api key put in .env file
