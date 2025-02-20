from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="superllm",
    version="0.1.0",
    author="SuperLLM Contributors",
    author_email="tobias.oberkofler@lmu.de",
    description="Enhanced LLM capabilities through test-time compute and search algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    url="https://github.com/to314as/superllm",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "networkx>=2.8.0",
        "tqdm>=4.65.0",
        "scipy>=1.8.0",
        "pandas>=1.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.1.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
            "build>=1.0.0",
            "twine>=4.0.0",
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
            "sphinx-autodoc-typehints>=1.25.0",
            "myst-parser>=2.0.0",
        ],
    },
) 