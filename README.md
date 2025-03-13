# LlamaAnki

LlamaAnki is an AI-powered tool that enhances your Anki flashcard experience by leveraging large language models (LLMs) to help you create, manage, and optimize your flashcards.

## Features

- **AI-Assisted Flashcard Generation**: Create high-quality flashcards from PDFs, websites, and text
- **Smart Card Review**: Get AI help when you're stuck on difficult cards
- **Deck Organization**: Use AI to organize, categorize, and tag your cards
- **Spaced Repetition Optimization**: AI analysis of your learning patterns
- **PDF Processing**: Extract content from academic papers and textbooks
- **Custom Prompting**: Create specialized prompts for different subjects
- **Multiple LLM Support**: Use OpenAI models, local models, or others

## Installation

### Prerequisites

- Python 3.9 or higher
- Anki installed (for full functionality)
- OpenAI API key (for OpenAI features)

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/LlamaSearch/llamaanki.git
cd llamaanki

# Install with pip
pip install -e .

# Or install with optional dependencies
pip install -e ".[all]"
```

### Setting up API Keys

For OpenAI integration, set your API key:

```bash
export OPENAI_API_KEY=your_api_key_here
```

Or create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Command Line Interface

LlamaAnki provides a powerful command-line interface:

```bash
# Get help
llamaanki --help

# List available commands
llamaanki --list-commands

# Process a PDF and generate flashcards
llamaanki pdf generate path/to/document.pdf --deck "My Study Deck" --num 10
```

### Working with PDFs

Extract content from PDFs:

```bash
llamaanki pdf extract path/to/document.pdf --output extracted_content
```

Generate flashcards from PDFs:

```bash
llamaanki pdf generate path/to/document.pdf --deck "Biology 101" --num 20 --model gpt-4
```

### Deck Management

```bash
# Create a new deck
llamaanki deck create "History 101" --description "Ancient civilizations study materials"

# List all decks
llamaanki deck list

# Get deck statistics
llamaanki deck stats "Biology 101"
```

### Note Management

```bash
# Find notes matching a tag
llamaanki note find "tag:important"

# Summarize a note
llamaanki note summarize 1234567890

# Generate similar questions
llamaanki note similar 1234567890 --count 3
```

### LLM Interaction

```bash
# List available models
llamaanki llm models

# Generate text
llamaanki llm prompt "Explain the Krebs cycle"
```

## Configuration

LlamaAnki uses a configuration file to customize its behavior. Create a JSON file (e.g., `config.json`):

```json
{
  "api_keys": {
    "openai": "your_openai_api_key"
  },
  "default_model": "gpt-4",
  "anki": {
    "collection_path": "/custom/path/to/collection.anki2",
    "media_path": "/custom/path/to/media"
  },
  "pdf": {
    "extraction_method": "pdfminer",
    "chunk_size": 1000
  }
}
```

Use the configuration file:

```bash
llamaanki --config config.json [command]
```

## Development

### Project Structure

```
llamaanki/
├── src/
│   └── llama_anki/         # Main package
│       ├── __init__.py
│       ├── cli.py          # Command line interface
│       ├── pdf/            # PDF processing module
│       ├── anki/           # Anki integration module
│       ├── llms/           # LLM integration module
│       └── utils/          # Utility functions
├── tests/                  # Test suite
├── examples/               # Example scripts and notebooks
├── docs/                   # Documentation
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Anki team for their incredible spaced repetition software
- OpenAI for their powerful language models
- All contributors who have helped improve this project 
# Updated in commit 1 - 2025-04-04 17:40:35

# Updated in commit 9 - 2025-04-04 17:40:36

# Updated in commit 17 - 2025-04-04 17:40:36

# Updated in commit 25 - 2025-04-04 17:40:37

# Updated in commit 1 - 2025-04-05 14:41:29

# Updated in commit 9 - 2025-04-05 14:41:30

# Updated in commit 17 - 2025-04-05 14:41:30

# Updated in commit 25 - 2025-04-05 14:41:30
