"""
Resume Generator Prototype

Pipeline:
knowledge -> template -> generated resume

The first version focuses on keeping facts from the project knowledge base
and avoiding unsupported claims.
"""

from pathlib import Path


def load_template(path):
    return Path(path).read_text(encoding="utf-8")


def generate_resume(template_path, output_path):
    content = load_template(template_path)
    Path(output_path).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    print("Resume generator prototype ready")
