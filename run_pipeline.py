# -*- coding: utf-8 -*-
"""
Master Pipeline Script: run_pipeline.py
Automates PDF parsing, question extraction, syllabus classification,
and compilation of questions with options into structured Markdown and JSON.
"""

import os
import sys
import glob
import argparse
from extractor import QuestionExtractor
from compiler import QuestionBankCompiler


def process_single_pdf(pdf_path: str, compiler: QuestionBankCompiler, label: str = None):
    print(f"[>] Processing: {pdf_path}")
    extractor = QuestionExtractor()
    questions = extractor.parse_pdf(pdf_path, label)
    print(f"    Extracted {len(questions)} questions.")
    compiler.add_questions_batch(questions)


def process_directory(dir_path: str, compiler: QuestionBankCompiler):
    pdf_files = sorted(glob.glob(os.path.join(dir_path, "*.pdf")))
    if not pdf_files:
        print(f"No PDF files found in directory: {dir_path}")
        return

    print(f"Found {len(pdf_files)} PDF files in {dir_path}.")
    for pdf_path in pdf_files:
        process_single_pdf(pdf_path, compiler)


def main():
    parser = argparse.ArgumentParser(
        description="Extract and compile exam questions and options from PDF papers."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input-pdf", help="Path to a single PDF paper")
    group.add_argument("--input-dir", help="Directory containing multiple PDF question papers")

    parser.add_argument("--output-dir", default="./output", help="Directory where results will be saved (default: ./output)")
    parser.add_argument("--label", default=None, help="Paper title/label (only used with --input-pdf)")
    parser.add_argument("--export-json", action="store_true", help="Also export a structured questions_database.json file")
    parser.add_argument("--master-file", default="Master_Question_Bank.md", help="Name of the consolidated master Markdown file")

    args = parser.parse_args()

    compiler = QuestionBankCompiler(output_dir=args.output_dir)

    if args.input_pdf:
        process_single_pdf(args.input_pdf, compiler, args.label)
    elif args.input_dir:
        process_directory(args.input_dir, compiler)

    compiler.generate_markdown(master_filename=args.master_file)

    if args.export_json:
        compiler.export_json()

    print("\n[SUCCESS] Pipeline execution finished.")


if __name__ == '__main__':
    main()
