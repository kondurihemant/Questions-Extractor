# -*- coding: utf-8 -*-
"""
Module: extractor.py
Description: Robust extraction of question items, options, and metadata
             from competitive examination PDF documents (such as GATE).
"""

import re
import os
import pymupdf


class QuestionExtractor:
    """
    Extracts individual questions, options, and metadata from exam PDF documents.
    Supports multiple historical and modern layout formats (OMR, CBT, Boxed).
    """

    # Regex patterns for matching start of questions
    QUESTION_START_PATTERNS = [
        # CBT style: Question Number : 1 Question Type : MCQ
        r'(?:^|\n)(Question\s+Number\s*:\s*(\d+))',
        # Standard format: Q.1, Q. 1, Q.No. 1, Q1
        r'(?:^|\n)(Q(?:uestion)?\.?\s*(?:No\.?)?\s*(\d+))\b',
    ]

    # Patterns to filter out non-question header/footer lines
    NOISE_PATTERNS = [
        r'GATE\s*20\d\d[^\n]*',
        r'Page\s+\d+\s+of\s+\d+',
        r'CS(?:-[A-D])?\s*\d+/\d+',
        r'Organi[sz]ing\s+Institute\s*:[^\n]*',
        r'Computer\s+Science\s+and\s+Information\s+Technology[^\n]*',
        r'Graduate\s+Aptitude\s+Test\s+in\s+Engineering[^\n]*',
        r'Answer\s+Keys?[^\n]*',
        r'Duration\s*:\s*[^\n]+',
        r'Maximum\s+Marks\s*:\s*[^\n]+',
        r'Read\s+the\s+following\s+instructions\s+carefully[^\n]*',
        r'SESSION\s*-\s*\d+',
        r'^\s*\d+\s*/\s*\d+\s*$',
    ]

    def __init__(self, remove_noise=True):
        self.remove_noise = remove_noise

    def clean_text(self, text: str) -> str:
        """Strips headers, footers, and redundant line breaks."""
        if not self.remove_noise:
            return text.strip()

        lines = text.splitlines()
        cleaned_lines = []
        for line in lines:
            line_str = line.strip()
            if not line_str:
                cleaned_lines.append('')
                continue
            # Check noise regexes
            is_noise = False
            for pat in self.NOISE_PATTERNS:
                if re.match(pat, line_str, re.IGNORECASE):
                    is_noise = True
                    break
            # Ignore grouped range announcements like "Q.1 - Q.5 carry one mark each"
            if re.match(r'^Q\.\s*\d+\s*[–-]\s*Q\.\s*\d+\s*(?:carry|Carry)', line_str, re.IGNORECASE):
                is_noise = True
            if re.match(r'^Q\.\s*\d+\s+to\s+Q\.\s*\d+\s*(?:carry|Carry)', line_str, re.IGNORECASE):
                is_noise = True

            if not is_noise:
                cleaned_lines.append(line)

        res = '\n'.join(cleaned_lines)
        # Collapse multiple blank lines into max 2
        res = re.sub(r'\n{3,}', '\n\n', res)
        return res.strip()

    def parse_pdf(self, pdf_path: str, paper_label: str = None) -> list:
        """
        Parses a PDF file and returns a list of extracted question dictionaries.
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        doc = pymupdf.open(pdf_path)
        pages_text = [page.get_text() for page in doc]
        full_text = '\n'.join(pages_text)

        if not paper_label:
            # Try to infer year from filename or text
            match = re.search(r'20[0-2][0-9]', full_text[:1000])
            paper_label = f"GATE {match.group(0)}" if match else os.path.basename(pdf_path)

        # Build compound regex for question splitting
        combined_pat = r'(?:^|\n)(?:Question\s+Number\s*:\s*(\d+)|Q(?:uestion)?\.?\s*(?:No\.?)?\s*(\d+))\b'
        matches = list(re.finditer(combined_pat, full_text, re.IGNORECASE))

        questions = []
        seen_qnums = {}

        for i, match in enumerate(matches):
            qnum = match.group(1) or match.group(2)
            start_idx = match.start()
            end_idx = matches[i + 1].start() if (i + 1 < len(matches)) else len(full_text)

            raw_block = full_text[start_idx:end_idx]
            cleaned_block = self.clean_text(raw_block)

            # Avoid tiny fragments
            if len(cleaned_block) < 25:
                continue

            # Detect NAT vs MCQ
            is_nat = bool(re.search(r'\b(?:NAT|Numerical\s+Answer|answer\s+in\s+integer|rounded\s+off\s+to)\b', cleaned_block, re.IGNORECASE))
            has_options = bool(re.search(r'\([A-D]\)', cleaned_block))

            # Disambiguate duplicate numbers across shifts/sessions
            occurrence = seen_qnums.get(qnum, 0) + 1
            seen_qnums[qnum] = occurrence
            unique_id = f"{paper_label}_Q{qnum}" if occurrence == 1 else f"{paper_label}_S{occurrence}_Q{qnum}"

            questions.append({
                'id': unique_id,
                'qnum': qnum,
                'paper': paper_label,
                'text': cleaned_block,
                'is_nat': is_nat and not has_options,
                'has_options': has_options
            })

        return questions


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Extract questions from a PDF exam paper.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--label", default=None, help="Label for the exam paper (e.g., 'GATE 2024')")
    args = parser.parse_args()

    extractor = QuestionExtractor()
    results = extractor.parse_pdf(args.pdf_path, args.label)
    print(f"Successfully extracted {len(results)} questions from {args.pdf_path}")
    if results:
        print("\nSample Extracted Question (First Question):\n")
        print(results[0]['text'][:300] + "...\n")
