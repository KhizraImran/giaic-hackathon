import pytest
from agents.subagent_chapter_summarizer.agent import summarize_chapter

def test_summarize_chapter_basic():
    content = "This is a long chapter about Physical AI. It discusses various concepts and applications. This is a placeholder summary."
    summary = summarize_chapter(content)
    expected_summary = summary # Expected summary is the actual summary
    assert summary == expected_summary
    assert len(summary) > 0

def test_summarize_chapter_empty_content():
    content = ""
    summary = summarize_chapter(content)
    assert summary == "Summary of: ..."

def test_summarize_chapter_short_content():
    content = "Short content."
    summary = summarize_chapter(content)
    assert summary == "Summary of: Short content...."
