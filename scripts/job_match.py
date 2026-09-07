"""
Job Match Agent prototype.

Matches a job description with personal technical assets.
The interface is prepared for later LLM integration.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class MatchResult:
    score: int
    strengths: List[str]
    gaps: List[str]
    suggestions: List[str]


def match_job(job_text: str, skills: List[str]) -> MatchResult:
    text = job_text.lower()
    matched = [skill for skill in skills if skill.lower() in text]

    return MatchResult(
        score=min(100, len(matched) * 20),
        strengths=matched,
        gaps=[],
        suggestions=[
            "Customize project keywords according to the target position",
            "Add measurable engineering results when available"
        ],
    )


if __name__ == "__main__":
    print(match_job(
        "SLAM engineer ROS2 C++ LiDAR navigation",
        ["ROS2", "SLAM", "C++", "LiDAR"]
    ))
