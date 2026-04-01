# Claude Code - AI Coding Assistant

A powerful AI-powered coding assistant built with Python that leverages large language models (LLMs) to understand code and execute complex tasks through intelligent tool calling and agent loops.

## Overview

Claude Code is an intelligent assistant that integrates with OpenRouter API to provide advanced code analysis and manipulation capabilities. It uses function calling to interact with the filesystem and execute programming tasks autonomously.

## Features

- 🤖 **LLM-Powered Agent Loop**: Uses Claude Haiku 4.5 model for intelligent code understanding and task execution
- 🛠️ **Multi-Tool Integration**: Supports file reading, writing, and code execution
- 📝 **OpenAI-Compatible API**: Built with OpenRouter for flexible model access
- 🔧 **Extensible Architecture**: Easy to add new tools and capabilities
- 🚀 **Fast Response Times**: Optimized for quick code analysis and generation

## Getting Started

### Prerequisites

- Python 3.x
- `uv` package manager
- OpenRouter API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Ma7moudkolib
```

2. Set up environment variables:
```bash
export OPENROUTER_API_KEY="your-api-key"
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
```

### Running the Application

```bash
./your_program.sh -p "Your coding task or question here"
```

Or directly:
```bash
python app/main.py -p "Your coding task here"
```

## Architecture

### Main Components

- **`app/main.py`**: Core application logic with LLM integration and tool calling
- **OpenRouter Integration**: Leverages Claude Haiku 4.5 for code understanding
- **Tools System**: Extensible function-calling interface for code manipulation

### Key Tools

- **Read**: Read and analyze file contents
- **Write**: Create and modify files
- **Execute**: Run code and capture results

## Technologies Used

- **Python 3**: Core language
- **OpenAI SDK**: For LLM API communication
- **OpenRouter**: AI model provider
- **Claude Haiku 4.5**: LLM backbone

## Project Structure

```
.
├── app/
│   └── main.py           # Main application entry point
├── .codecrafters/
│   ├── compile.sh        # Build script
│   └── run.sh            # Execution script
├── your_program.sh       # CLI wrapper
├── codecrafters.yml      # Configuration
└── README.md             # This file
```

## Usage Examples

### Analyze Code

```bash
./your_program.sh -p "Analyze this Python function for performance issues"
```

### Generate Code

```bash
./your_program.sh -p "Create a Python function that sorts a list of dictionaries by multiple keys"
```

### Code Transformation

```bash
./your_program.sh -p "Refactor this JavaScript code to use async/await"
```

## Development

To extend the assistant with new tools:

1. Define the tool specification in the tools array within `app/main.py`
2. Handle the tool response in the message loop
3. Update the agent logic as needed

## Performance

- Optimized for latency-sensitive operations
- Uses Claude Haiku 4.5 for faster responses
- Streaming tool execution for real-time feedback

## Author

**Mahmoud Kolib** - Python Developer & AI Enthusiast

## License

MIT License - Feel free to use this project in your own work

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
