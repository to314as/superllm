Installation Guide
=================

This guide will help you install SuperLLM and its dependencies.

Requirements
-----------

SuperLLM requires Python 3.8 or later. The package has the following core dependencies:

* ``numpy`` >= 1.20.0
* ``torch`` >= 2.0.0
* ``transformers`` >= 4.30.0
* ``networkx`` >= 2.8.0
* ``tqdm`` >= 4.65.0
* ``scipy`` >= 1.8.0
* ``pandas`` >= 1.5.0

Installation Methods
------------------

Via pip (Recommended)
~~~~~~~~~~~~~~~~~~~~

The easiest way to install SuperLLM is via pip:

.. code-block:: bash

   pip install superllm

This will install SuperLLM and all its required dependencies.

Development Installation
~~~~~~~~~~~~~~~~~~~~~~

For development purposes, you can install SuperLLM with additional development dependencies:

.. code-block:: bash

   git clone https://github.com/yourusername/superllm.git
   cd superllm
   pip install -e ".[dev]"

This will install the package in editable mode with additional development dependencies:

* ``pytest`` for testing
* ``black`` for code formatting
* ``isort`` for import sorting
* ``flake8`` for linting
* ``mypy`` for type checking

GPU Support
----------

SuperLLM can leverage GPU acceleration through PyTorch. To enable GPU support, ensure you have:

1. A CUDA-compatible GPU
2. CUDA toolkit installed
3. PyTorch with CUDA support

You can verify GPU support by running:

.. code-block:: python

   import torch
   print(f"CUDA available: {torch.cuda.is_available()}")
   print(f"Number of GPUs: {torch.cuda.device_count()}")

Troubleshooting
--------------

Common Issues
~~~~~~~~~~~~

1. **ImportError: No module named 'superllm'**

   * Ensure you've installed the package correctly
   * Check your Python path
   * Verify your virtual environment is activated (if using one)

2. **CUDA not available**

   * Check CUDA installation
   * Verify PyTorch CUDA support
   * Update GPU drivers

3. **Version conflicts**

   * Create a new virtual environment
   * Update all dependencies
   * Check compatibility matrix in documentation

Getting Help
~~~~~~~~~~~

If you encounter any issues:

1. Check the `GitHub Issues <https://github.com/yourusername/superllm/issues>`_
2. Join our `Discord community <https://discord.gg/superllm>`_
3. Read the `FAQ section <https://docs.superllm.ai/faq>`_

Next Steps
---------

After installation, check out the :doc:`quickstart` guide to begin using SuperLLM. 