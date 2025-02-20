Welcome to SuperLLM's documentation!
================================

SuperLLM is a powerful Python library for enhancing LLM capabilities through advanced test-time compute and search algorithms, focusing on expert human-AI co-construction.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   user_guide/index
   api_reference/index
   contributing
   changelog

Features
--------

* **Test-Time Compute Algorithms**
    * Tree of Thoughts implementation
    * Self-consistency sampling
    * Dynamic prompt optimization
    * Multi-perspective reasoning

* **Search Algorithms**
    * Beam search with adaptive width
    * Best-first symbolic search
    * Guided exploration with expert feedback
    * Knowledge graph-based reasoning

* **Expert Human-AI Co-Construction**
    * Interactive reasoning frameworks
    * Expert feedback integration
    * Knowledge distillation from expert interactions
    * Adaptive learning from human guidance

Quick Installation
----------------

.. code-block:: bash

   pip install superllm

Quick Example
------------

.. code-block:: python

   from superllm import ThoughtTree, ExpertFeedback
   from superllm.search import AdaptiveBeamSearch

   # Initialize components
   thought_tree = ThoughtTree()
   expert_system = ExpertFeedback()
   search = AdaptiveBeamSearch(beam_width=5, max_steps=10)

   # Run enhanced inference
   result = thought_tree.solve(
       prompt="Your complex question here",
       search_algorithm=search,
       expert_system=expert_system
   )

   print(f"Solution: {result['solution']}")
   print(f"Confidence: {result['confidence']}")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 