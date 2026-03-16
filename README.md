# 💸 FINFLOW — GST Register & Finance Manager

> A smart, all-in-one GST-compliant finance management web app built during the **Wave Hackathon** by a team of CSE students from KLS VDIT College.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?style=flat&logo=streamlit)
![Hackathon](https://img.shields.io/badge/Wave-Hackathon-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Language](https://img.shields.io/badge/Language-English%20%7C%20ಕನ್ನಡ-purple?style=flat)

---

## 📌 About the Project

**FINFLOW** is a GST Sales & Purchase Register application designed to help small businesses manage their finances and GST compliance — all in one place.

From OCR-based invoice scanning to auto-generating GSTR-1 and GSTR-3B reports, FINFLOW brings real-world GST workflows into a clean, interactive dashboard.

Built as part of the **Wave Hackathon** by a team of CSE students from **KLS Vishwanathrao Deshpande Institute of Technology (VDIT), Haliyal**.

---

## ✨ Features

### 🧾 Invoice Management
- **OCR Invoice Scanning** — Upload PDF or image invoices; auto-reads vendor, GSTIN, amounts, tax
- **Smart Invoice Detection** — Auto-classifies as Purchase or Sales invoice using GSTIN position logic
- **Invoice Validation** — Rejects illegal invoices (no GSTIN but GST charged), fake GSTINs, and Composition scheme violations
- **Manual Entry** — Add entries directly without uploading a document

### 📊 Registers & Dashboard
- **Purchase Register** — All inward supply invoices with Input Tax Credit (ITC) tracking
- **Sales Register** — All outward supply invoices with Output Tax tracking
- **Live Dashboard** — Real-time totals, GST breakdown, gross margin, and net tax payable

### 📄 GST Reports
- **GSTR-1** — Outward supplies report with B2B, B2C, and HSN summary tabs
- **GSTR-3B** — Monthly summary return with net tax payable calculation
- **GSTR-2A / 2B** — Inward supplies ITC tracking and reconciliation with Purchase Register

### 🔒 Security & Users
- **Multi-user Authentication** — Sign up / Sign in with password rules (uppercase + special character)
- **Per-user Persistent Storage** — Data saved to disk as JSON; survives page reloads and restarts
- **Password Change** — Users can update their password from Settings

### 🌐 Bilingual Support
- Full support for **English** and **ಕನ್ನಡ (Kannada)**

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| **Python** | Core backend logic, OCR parsing, GST calculations |
| **Streamlit** | Frontend UI & interactive dashboard |
| **Pytesseract** | OCR text extraction from invoice images/PDFs |
| **Pandas** | Data handling for registers and reports |
| **PyMuPDF / pdf2image** | PDF rendering for OCR |
| **JSON** | Lightweight per-user persistent storage |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Rajendra7250/FINFLOW-FINAL.git
cd FINFLOW-FINAL
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. Open your browser at `http://localhost:8501`

### Demo Credentials
```
Username: admin
Password: Admin@123
```

---

## 📁 Project Structure

```
FINFLOW-FINAL/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── finflow_data/           # Auto-created: per-user JSON data storage
│   ├── _users.json         # User credentials
│   └── <username>.json     # Per-user financial data
└── README.md               # Project documentation
```

---

## 🧠 How It Works

```
Invoice (PDF/Image)
      ↓
  OCR Engine (Pytesseract)
      ↓
  Parse: Vendor, GSTIN, Date, Subtotal, CGST, SGST, IGST
      ↓
  Validate: Is GSTIN valid? Is tax charge legal?
      ↓ (if rejected → show reason, block entry)
  Auto-detect: Sales Invoice or Purchase Invoice?
      ↓
  Add to Register → Update Dashboard → Generate GST Reports
```

---

## 📋 GST Compliance Features

- ✅ Validates GSTIN format (15-char regex check)
- 🚫 Rejects invoices from unregistered suppliers charging GST (illegal under CGST Act)
- 🚫 Rejects invoices from Composition Scheme dealers charging GST
- ⚠️ Flags invoices with invalid/fake GSTINs
- 📊 Calculates net GST payable = Output Tax − Input Tax Credit (ITC)
- 📑 GSTR-2A reconciliation to identify unmatched/mismatched ITC

---

## 👥 Team

Built with ❤️ by CSE students from **KLS VDIT College, Haliyal** at the **Wave Hackathon**.

| Rajendra M Madival |
| Nikhil Hatti |
| Sai prasad Ekabote |
| Mukesh Ghanchi |

## 🏆 Hackathon

| Detail | Info |
|--------|------|
| **Event** | Wave Hackathon |
| **College** | KLS Vishwanathrao Deshpande Institute of Technology |
| **Status** | ✅ Successfully Completed |

---

## 🔮 Future Improvements

- [ ] Hash passwords (bcrypt) instead of plain text storage
- [ ] Split `app.py` into modules (auth, ocr, reports, ui)
- [ ] Replace regex OCR parsing with AI-based invoice extraction
- [ ] SQLite database instead of flat JSON files
- [ ] Deploy on Streamlit Cloud
- [ ] Export GSTR reports as PDF
- [ ] Mobile responsive design
- [ ] Email alerts for GST filing deadlines

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> *"The best way to learn is to build something real."*  
> This is our first real-world application — built under hackathon pressure, with real GST logic. 🚀
