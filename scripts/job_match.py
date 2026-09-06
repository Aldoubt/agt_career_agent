"""
Job matching tool skeleton.

Future implementation:
Input:
    Job description
    Knowledge database

Output:
    Skill matching
    Resume keywords
    Interview preparation topics
"""

from pathlib import Path


def load_job_description(path: str):
    return Path(path).read_text(encoding="utf-8")


def match_job(job_text: str):
    return {
        "status": "prototype",
        "job_length": len(job_text),
        "next": "connect knowledge base and LLM evaluation"
    }


if __name__ == "__main__":
    print("Job Match Agent prototype")
