"""
Tests for the ThoughtTree implementation.
"""

import pytest
import numpy as np
from superllm import ThoughtTree, ExpertFeedback
from superllm.search import AdaptiveBeamSearch

def test_thought_tree_initialization():
    """Test basic initialization of ThoughtTree."""
    tree = ThoughtTree()
    assert tree.max_branches == 5
    assert tree.max_depth == 3
    assert tree.temperature == 0.7

def test_thought_tree_solve():
    """Test solving a simple problem with ThoughtTree."""
    tree = ThoughtTree()
    expert = ExpertFeedback()
    search = AdaptiveBeamSearch()
    
    result = tree.solve(
        prompt="What is the capital of France?",
        search_algorithm=search,
        expert_system=expert
    )
    
    assert isinstance(result, dict)
    assert "solution" in result
    assert "reasoning_path" in result
    assert "confidence" in result
    assert 0 <= result["confidence"] <= 1

def test_expert_feedback():
    """Test expert feedback system."""
    expert = ExpertFeedback(feedback_strategy="hybrid")
    
    # Test automated evaluation
    feedback = expert.evaluate("Test thought")
    assert isinstance(feedback.score, float)
    assert 0 <= feedback.score <= 1
    
    # Test feedback statistics
    stats = expert.get_feedback_statistics()
    assert isinstance(stats, dict)
    assert "mean_score" in stats
    assert "num_feedback" in stats

def test_adaptive_beam_search():
    """Test adaptive beam search."""
    search = AdaptiveBeamSearch(
        initial_beam_width=3,
        max_steps=5
    )
    
    # Define simple test functions
    def score_fn(state):
        return float(state)
    
    def expand_fn(state):
        return [state + 0.1, state + 0.2]
    
    path, score = search.search(
        initial_state=0.0,
        score_fn=score_fn,
        expand_fn=expand_fn
    )
    
    assert isinstance(path, list)
    assert isinstance(score, float)
    assert len(path) > 0
    assert score > 0

def test_integration():
    """Test integration of all components."""
    tree = ThoughtTree()
    expert = ExpertFeedback()
    search = AdaptiveBeamSearch()
    
    # Test complete pipeline
    result = tree.solve(
        prompt="Explain quantum computing",
        search_algorithm=search,
        expert_system=expert
    )
    
    assert isinstance(result, dict)
    assert len(result["reasoning_path"]) > 0
    
    # Check expert feedback integration
    stats = expert.get_feedback_statistics()
    assert stats["num_feedback"] > 0
    
    # Check search statistics
    search_stats = search.get_search_statistics()
    assert search_stats["num_steps"] > 0

if __name__ == "__main__":
    pytest.main([__file__]) 