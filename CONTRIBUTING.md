# Contributing to LlamaAnki

Thank you for your interest in contributing to LlamaAnki! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

- Use the GitHub issue tracker to report bugs
- Before creating a new issue, please check if the issue already exists
- Include detailed information about:
  - Expected behavior
  - Actual behavior
  - Steps to reproduce
  - Environment (OS, Python version, etc.)
  - Screenshots if applicable

### Suggesting Enhancements

- Use the GitHub issue tracker to suggest enhancements
- Provide a clear and detailed explanation of the feature/enhancement
- Explain why this enhancement would be useful to most LlamaAnki users

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Run tests and ensure they pass: `pytest`
5. Format your code using our code style guidelines (see below)
6. Submit a pull request to the `main` branch

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llamaanki.git
   cd llamaanki
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. Setup pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Coding Standards

- Follow PEP 8 guidelines
- Use type hints wherever possible
- Write docstrings in the Google style format
- Maximum line length is 100 characters

## Testing

- Write tests for new features or bug fixes
- Ensure all tests pass before submitting a pull request
- Run tests with: `pytest`
- Aim for good test coverage of your code

## Documentation

- Update documentation for new features or changes to existing functionality
- Document public API methods and classes
- Keep the README and other documentation up to date
- Use clear and concise language

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in the present tense (e.g., "Add feature" not "Added feature")
- Reference issue numbers if applicable

## Release Process

1. Version numbers follow [Semantic Versioning](https://semver.org/)
2. Update the CHANGELOG.md with all notable changes
3. Release notes should be clear and comprehensive

## Get Help

If you need help with contributing:

- Join our [community chat](#)
- Ask questions in GitHub issues

Thank you for contributing to LlamaAnki! 