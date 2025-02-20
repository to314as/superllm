Quickstart Guide
===============

This guide will help you get started with SuperLLM quickly.

Basic Usage
----------

First, import the necessary components:

.. code-block:: python

   from superllm import ThoughtTree, ExpertFeedback
   from superllm.search import AdaptiveBeamSearch

Initialize the Components
~~~~~~~~~~~~~~~~~~~~~~~

Create instances of the main components:

.. code-block:: python

   # Initialize the thought tree with default parameters
   thought_tree = ThoughtTree()

   # Create an expert feedback system
   expert_system = ExpertFeedback(
       feedback_strategy="hybrid",
       feedback_threshold=0.7
   )

   # Configure the search algorithm
   search = AdaptiveBeamSearch(
       initial_beam_width=5,
       max_beam_width=10,
       max_steps=10,
       diversity_weight=0.3
   )

Solve a Problem
~~~~~~~~~~~~~~

Use the components together to solve a complex problem:

.. code-block:: python

   # Define your problem
   result = thought_tree.solve(
       prompt="Explain how quantum entanglement works",
       search_algorithm=search,
       expert_system=expert_system
   )

   # Access the results
   print(f"Solution: {result['solution']}")
   print(f"Confidence: {result['confidence']}")
   print(f"Reasoning path: {result['reasoning_path']}")

Advanced Usage
-------------

Using Custom Models
~~~~~~~~~~~~~~~~~

You can use your own language models:

.. code-block:: python

   from transformers import AutoModelForCausalLM, AutoTokenizer

   # Load your model and tokenizer
   model = AutoModelForCausalLM.from_pretrained("your-model-name")
   tokenizer = AutoTokenizer.from_pretrained("your-model-name")

   # Create ThoughtTree with custom model
   thought_tree = ThoughtTree(
       model=model,
       tokenizer=tokenizer,
       temperature=0.8
   )

Custom Feedback Systems
~~~~~~~~~~~~~~~~~~~~~

Implement custom evaluation logic:

.. code-block:: python

   def custom_evaluator(thought):
       # Your custom evaluation logic here
       return score  # float between 0 and 1

   expert_system = ExpertFeedback(
       custom_evaluator=custom_evaluator,
       feedback_strategy="active"
   )

Analyzing Results
~~~~~~~~~~~~~~~

Get detailed statistics about the search process:

.. code-block:: python

   # Get expert feedback statistics
   feedback_stats = expert_system.get_feedback_statistics()
   print("Feedback Statistics:", feedback_stats)

   # Get search statistics
   search_stats = search.get_search_statistics()
   print("Search Statistics:", search_stats)

Example Applications
------------------

1. Complex Problem Solving
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   result = thought_tree.solve(
       prompt="What are the potential implications of artificial general intelligence?",
       search_algorithm=search,
       expert_system=expert_system,
       max_depth=5  # Deeper exploration
   )

2. Multi-step Reasoning
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Configure for multi-step reasoning
   thought_tree = ThoughtTree(
       max_branches=7,
       max_depth=4,
       temperature=0.9
   )

   result = thought_tree.solve(
       prompt="Develop a step-by-step plan for implementing a sustainable energy system",
       search_algorithm=search,
       expert_system=expert_system
   )

3. Creative Generation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Configure for creative exploration
   search = AdaptiveBeamSearch(
       diversity_weight=0.7,  # Increase diversity
       initial_beam_width=8
   )

   result = thought_tree.solve(
       prompt="Generate innovative solutions for urban transportation",
       search_algorithm=search,
       expert_system=expert_system
   )

Next Steps
---------

- Check out the :doc:`user_guide/index` for detailed documentation
- Explore the :doc:`api_reference/index` for complete API details
- Read the :doc:`contributing` guide to contribute to the project 