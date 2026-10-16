# -*- coding: utf-8 -*-
"""
Module: compiler.py
Description: Compiles extracted questions into neatly formatted Markdown files
             categorized by syllabus sections, with support for JSON export.
"""

import os
import json
from classifier import SyllabusClassifier


class QuestionBankCompiler:
    """
    Compiles and exports categorized questions into Markdown and JSON files.
    """

    FILE_NAMES = {
        1: "Section_01_Engineering_Mathematics.md",
        2: "Section_02_Digital_Logic.md",
        3: "Section_03_Computer_Organization_and_Architecture.md",
        4: "Section_04_Programming_and_Data_Structures.md",
        5: "Section_05_Algorithms.md",
        6: "Section_06_Theory_of_Computation.md",
        7: "Section_07_Compiler_Design.md",
        8: "Section_08_Operating_Systems.md",
        9: "Section_09_Databases.md",
        10: "Section_10_Computer_Networks.md",
        11: "Section_11_Legacy_and_Deprecated_Topics.md",
    }

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.classifier = SyllabusClassifier()
        self.buckets = {i: [] for i in self.FILE_NAMES}

    def add_question(self, q_item: dict, forced_section: int = None):
        """
        Adds a single question item to the appropriate section bucket.
        """
        sec_id = forced_section if forced_section else self.classifier.classify(q_item['text'])
        q_item['section_id'] = sec_id
        q_item['section_name'] = self.classifier.get_section_name(sec_id)
        self.buckets[sec_id].append(q_item)

    def add_questions_batch(self, questions: list):
        for q in questions:
            self.add_question(q)

    def generate_markdown(self, master_filename: str = "Master_Question_Bank.md"):
        """
        Writes out individual section Markdown files and merges into a master document.
        """
        master_parts = [
            "# Master Question Bank\n",
            "*(Compiled from Examination PDFs with Complete Options and Problem Statements)*\n\n---\n"
        ]

        for sec_id, fname in self.FILE_NAMES.items():
            sec_title = self.classifier.get_section_name(sec_id)
            sec_file_path = os.path.join(self.output_dir, fname)

            q_list = self.buckets[sec_id]
            header = f"# {sec_title}\n\n*Total Questions in this section: {len(q_list)}*\n\n---\n\n"

            formatted_qs = []
            for q in q_list:
                item_md = f"### [{q['paper']}, Q.{q['qnum']}]\n\n{q['text']}\n"
                formatted_qs.append(item_md)

            body = '\n---\n\n'.join(formatted_qs)
            full_sec_content = header + (body if body else "_No questions classified in this section yet._\n")

            with open(sec_file_path, 'w', encoding='utf-8') as f:
                f.write(full_sec_content)

            master_parts.append(full_sec_content)

        # Write unified master file
        master_path = os.path.join(self.output_dir, master_filename)
        with open(master_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(master_parts))

        print(f"Compilation complete! Master file written to: {master_path}")
        return master_path

    def export_json(self, json_filename: str = "questions_database.json"):
        """Exports the full question catalog to a structured JSON file."""
        all_questions = []
        for sec_id, q_list in self.buckets.items():
            all_questions.extend(q_list)

        json_path = os.path.join(self.output_dir, json_filename)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(all_questions, f, indent=2, ensure_ascii=False)
        print(f"JSON database exported to: {json_path}")
        return json_path
