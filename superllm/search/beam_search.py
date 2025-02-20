"""
Implementation of adaptive beam search for LLM exploration.
"""

from typing import List, Dict, Any, Optional, Tuple
import numpy as np
from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class BeamNode:
    """Represents a node in the beam search."""
    state: Any
    score: float
    parent: Optional['BeamNode']
    depth: int
    metadata: Dict[str, Any]

class AdaptiveBeamSearch:
    """
    Implements an adaptive beam search algorithm that dynamically adjusts
    its width based on the quality of explored solutions.
    """
    
    def __init__(
        self,
        initial_beam_width: int = 5,
        max_beam_width: int = 10,
        min_beam_width: int = 2,
        adaptation_rate: float = 0.1,
        max_steps: int = 10,
        diversity_weight: float = 0.3
    ):
        """
        Initialize the adaptive beam search.
        
        Args:
            initial_beam_width: Starting width of the beam
            max_beam_width: Maximum allowed beam width
            min_beam_width: Minimum allowed beam width
            adaptation_rate: Rate at which beam width adapts
            max_steps: Maximum number of search steps
            diversity_weight: Weight given to diversity in scoring
        """
        self.beam_width = initial_beam_width
        self.max_beam_width = max_beam_width
        self.min_beam_width = min_beam_width
        self.adaptation_rate = adaptation_rate
        self.max_steps = max_steps
        self.diversity_weight = diversity_weight
        self.search_history: List[List[BeamNode]] = []
        
    def search(
        self,
        initial_state: Any,
        score_fn: callable,
        expand_fn: callable,
        **kwargs
    ) -> Tuple[List[Any], float]:
        """
        Perform adaptive beam search.
        
        Args:
            initial_state: Starting state for the search
            score_fn: Function to score states
            expand_fn: Function to generate next states
            **kwargs: Additional arguments for scoring/expansion
            
        Returns:
            Tuple of (best path, score)
        """
        # Initialize beam with root node
        current_beam = [
            BeamNode(
                state=initial_state,
                score=score_fn(initial_state),
                parent=None,
                depth=0,
                metadata={}
            )
        ]
        
        for step in range(self.max_steps):
            # Generate candidates
            candidates = PriorityQueue()
            for node in current_beam:
                next_states = expand_fn(node.state)
                for next_state in next_states:
                    score = self._compute_score(
                        next_state,
                        score_fn,
                        current_beam,
                        **kwargs
                    )
                    candidates.put(
                        (-score,  # Negative for max-heap
                        BeamNode(
                            state=next_state,
                            score=score,
                            parent=node,
                            depth=step + 1,
                            metadata={"parent_score": node.score}
                        ))
                    )
            
            # Select next beam
            next_beam = []
            seen_states = set()
            while len(next_beam) < self.beam_width and not candidates.empty():
                _, node = candidates.get()
                state_hash = hash(str(node.state))
                if state_hash not in seen_states:
                    next_beam.append(node)
                    seen_states.add(state_hash)
            
            # Adapt beam width based on progress
            self._adapt_beam_width(next_beam)
            
            # Store search history
            self.search_history.append(next_beam)
            current_beam = next_beam
            
        # Return best path
        return self._extract_best_path(current_beam)
    
    def _compute_score(
        self,
        state: Any,
        score_fn: callable,
        current_beam: List[BeamNode],
        **kwargs
    ) -> float:
        """Compute score for a state, incorporating diversity bonus."""
        base_score = score_fn(state)
        
        # Add diversity bonus
        if current_beam:
            diversity_bonus = self._compute_diversity_bonus(state, current_beam)
            return (1 - self.diversity_weight) * base_score + self.diversity_weight * diversity_bonus
        return base_score
    
    def _compute_diversity_bonus(
        self,
        state: Any,
        current_beam: List[BeamNode]
    ) -> float:
        """Compute diversity bonus based on difference from current beam."""
        # This is a placeholder - actual implementation would depend on state representation
        return np.random.uniform(0.5, 1.0)
    
    def _adapt_beam_width(self, current_beam: List[BeamNode]) -> None:
        """Adapt beam width based on search progress."""
        if not current_beam:
            return
            
        # Compute average score improvement
        avg_improvement = np.mean([
            node.score - node.metadata["parent_score"]
            for node in current_beam
            if "parent_score" in node.metadata
        ])
        
        # Adjust beam width
        if avg_improvement > 0.1:
            self.beam_width = min(
                self.max_beam_width,
                self.beam_width + self.adaptation_rate
            )
        elif avg_improvement < 0.01:
            self.beam_width = max(
                self.min_beam_width,
                self.beam_width - self.adaptation_rate
            )
    
    def _extract_best_path(
        self,
        final_beam: List[BeamNode]
    ) -> Tuple[List[Any], float]:
        """Extract the best path from the final beam."""
        if not final_beam:
            return [], 0.0
            
        # Find best final node
        best_node = max(final_beam, key=lambda x: x.score)
        
        # Trace back path
        path = []
        current = best_node
        while current:
            path.append(current.state)
            current = current.parent
            
        return list(reversed(path)), best_node.score
    
    def get_search_statistics(self) -> Dict[str, Any]:
        """Get statistics about the search process."""
        if not self.search_history:
            return {}
            
        return {
            "final_beam_width": self.beam_width,
            "num_steps": len(self.search_history),
            "avg_beam_score": np.mean([
                node.score
                for beam in self.search_history
                for node in beam
            ]),
            "max_score_achieved": max(
                node.score
                for beam in self.search_history
                for node in beam
            )
        } 