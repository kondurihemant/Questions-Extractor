# Universal Exam Question & Option Extractor Pipeline
### Automated PDF Parsing, Syllabus Classification, and Question Bank Compilation

This tool provides an end-to-end Python pipeline to extract complete examination questions (including question statements, code blocks, tables, and options `(A)`, `(B)`, `(C)`, `(D)` or Numerical Answer Type `NAT` formats) from examination PDF documents, classify them by syllabus domain, and output clean GitHub-flavored Markdown files as well as structured JSON datasets.

---

## 1. Directory Structure

```
gate_question_extractor/
├── extractor.py         # PDF parsing, header/footer cleaning & question boundary detection
├── classifier.py        # Weighted multi-class syllabus domain classifier
├── compiler.py          # Formats and compiles questions into Markdown & JSON
├── run_pipeline.py      # Master CLI runner for single or batch processing
├── requirements.txt     # Python dependencies
└── README.md            # Complete user documentation & adaptation guide
```

---

## 2. Prerequisites & Setup

### Requirements
- **Python**: Version `3.8` or higher
- **Core Library**: `pymupdf` (high-performance MuPDF PDF parsing engine)

### Installation
Install the necessary package using `pip`:
```bash
pip install -r requirements.txt
```
*(Alternatively: `pip install pymupdf`)*

---

## 3. Quick Start & Usage

### A. Extract a Single PDF Paper
To extract all questions from a specific question paper and organize them into section-wise Markdown files:
```bash
python3 run_pipeline.py \
  --input-pdf "/path/to/GATE_2024.pdf" \
  --label "GATE 2024 (CS2)" \
  --output-dir "./output_2024"
```

### B. Batch Process an Entire Directory of Papers
To process multiple years or multiple sessions simultaneously:
```bash
python3 run_pipeline.py \
  --input-dir "/path/to/folder_with_pdfs" \
  --output-dir "./output_master"
```

### C. Generate a Structured JSON Dataset
To generate both Markdown documents and a structured JSON file (`questions_database.json`) for downstream use (e.g., test engines, web apps, databases):
```bash
python3 run_pipeline.py \
  --input-pdf "/path/to/paper.pdf" \
  --output-dir "./output" \
  --export-json
```

---

## 4. Pipeline Architecture: How It Works

```
                     +------------------------+
                     |  Input PDF Paper(s)    |
                     +-----------+------------+
                                 |
                                 v
                     +------------------------+
                     |      extractor.py      |
                     | - PyMuPDF text stream  |
                     | - Noise / Header scrub |
                     | - Regex question split |
                     | - Options & NAT detect |
                     +-----------+------------+
                                 |
                                 v
                     +------------------------+
                     |     classifier.py      |
                     | - Weighted keyword map |
                     | - Syllabus domain tag  |
                     | - Legacy topic routing |
                     +-----------+------------+
                                 |
                                 v
                     +------------------------+
                     |      compiler.py       |
                     | - Section Markdown     |
                     | - Master Question Bank |
                     | - JSON Dataset Export  |
                     +------------------------+
```

### Step 1: Text Extraction & Scrubbing (`extractor.py`)
- Reads text blocks across all PDF pages.
- Strips administrative footers, page numbering (e.g., `Page 1 of 40`, `CS 1/20`), and grouped headers (e.g., `Q.1 - Q.5 carry one mark each`).
- Splits text cleanly at question anchors (`Q.1`, `Question Number : 1`, etc.).
- Identifies whether the question is multiple choice (contains `(A)`, `(B)`, `(C)`, `(D)`) or Numerical Answer Type (`NAT`).

### Step 2: Syllabus Domain Classification (`classifier.py`)
- Evaluates extracted question text using a weighted rule scoring model.
- Automatically handles overlapping terms: for instance, a question containing `"graph"` will route to **Algorithms** if it includes `"Dijkstra"` or `"Shortest Path"`, but to **Engineering Mathematics** if it references `"eigenvalues"` or `"chromatic number"`.
- Explicitly detects **Legacy / Deprecated Topics** (Software Engineering models like COCOMO, Waterfall, Spiral, Testing, Metrics; HTML tags and tables) and routes them into Section 11.

### Step 3: Compilation & Formatting (`compiler.py`)
- Groups questions into modular Markdown files (`Section_01_Engineering_Mathematics.md` ... `Section_11_Legacy_and_Deprecated_Topics.md`).
- Merges all sections into a unified `Master_Question_Bank.md`.
- Generates `questions_database.json` with fields:
  ```json
  {
    "id": "GATE 2024 (CS2)_Q11",
    "qnum": "11",
    "paper": "GATE 2024 (CS2)",
    "text": "Consider a computer with a 4 MHz processor...",
    "is_nat": false,
    "has_options": true,
    "section_id": 3,
    "section_name": "Section 3: Computer Organization and Architecture"
  }
  ```

---

## 5. Implementing for Other Examination PDFs

You can adapt this pipeline to **any other examination** (e.g., other GATE disciplines like ECE, EE, ME, CE; or UPSC, JEE, University semester exams) by following these three simple steps:

### 1. Customizing Question Numbering Patterns (`extractor.py`)
If the target exam numbers questions differently (e.g., `1.`, `Question 1:`, `Problem 1.`), update `QUESTION_START_PATTERNS` in `extractor.py`:
```python
QUESTION_START_PATTERNS = [
    r'(?:^|\n)(Question\s*(\d+)[\.:])',     # Matches: Question 1: or Question 1.
    r'(?:^|\n)(Problem\s*(\d+)[\.:])',      # Matches: Problem 1.
    r'(?:^|\n)(\d+[\.:])\s+[A-Z]',          # Matches: 1. Let x be...
]
```

### 2. Customizing Syllabus Sections & Keywords (`classifier.py`)
To adapt to another subject (for example, **Electronics & Communication Engineering** or **Electrical Engineering**), replace `SECTIONS` and `RULES` in `classifier.py`:
```python
SECTIONS = {
    1: "Section 1: Engineering Mathematics",
    2: "Section 2: Networks, Signals and Systems",
    3: "Section 3: Electronic Devices",
    4: "Section 4: Analog Circuits",
    5: "Section 5: Digital Circuits",
    6: "Section 6: Control Systems",
    7: "Section 7: Communications",
    8: "Section 8: Electromagnetics"
}

RULES = {
    2: [('laplace transform', 10), ('fourier', 10), ('two-port', 9), ('thevenin', 9)],
    3: [('pn junction', 10), ('mosfet', 10), ('bandgap', 9), ('carrier mobility', 9)],
    4: [('op-amp', 10), ('bjt amplifier', 10), ('differential pair', 9), ('active filter', 8)],
    # Add your keywords and weights here
}
```

### 3. Customizing Header / Footer Filters (`extractor.py`)
If the target PDFs contain unique institutional headers (e.g., `"UPSC Civil Services Examination"`, `"Indian Institute of Technology"`), add them to `NOISE_PATTERNS` in `extractor.py`:
```python
NOISE_PATTERNS = [
    r'UPSC\s*20\d\d[^\n]*',
    r'Page\s+\d+\s+of\s+\d+',
    r'DO\s+NOT\s+OPEN\s+THIS\s+BOOKLET[^\n]*',
    # Add exam-specific header/footer regexes
]
```

---

## 6. Handling Scanned (Image-Only) vs Digital PDFs

- **Digital PDFs (Text-Based)**: Directly parsed by PyMuPDF at high speed (fraction of a second per paper). All modern GATE papers (2012–2026) are digital PDFs.
- **Scanned (Raster Image) PDFs**: Legacy papers (such as pre-2012 scanned prints) require an optical character recognition (OCR) step before or during parsing:
  1. **Option A (Tesseract CLI)**:
     ```bash
     ocrmypdf input_scanned.pdf input_searchable.pdf
     ```
     Then pass `input_searchable.pdf` directly to `run_pipeline.py`.
  2. **Option B (Python OCR)**:
     You can integrate `pytesseract` or `easyocr` to render page pixmaps via `page.get_pixmap()` and run OCR on pages where `len(page.get_text()) == 0`.
