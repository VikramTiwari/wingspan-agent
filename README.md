# Wingspan Agent

An AI agent implementation using Google's Agent Development Kit (ADK) and LiteLLM for flexible LLM integration.

## Features

- Integration with Google's Agent Development Kit (ADK)
- Support for multiple LLM providers through LiteLLM
- Data processing capabilities with pandas
- Environment-based configuration

## Setup

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Set up Google Cloud credentials:
   - Create a service account in Google Cloud Console
   - Download the JSON key file
   - Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to your key file

5. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your project-specific values

## Project Structure

- `src/` - Main source code
  - `agents/` - Agent implementations
  - `tools/` - Custom tools for the agent
  - `config/` - Configuration files
  - `main.py` - Entry point
- `tests/` - Test files
- `requirements.txt` - Project dependencies
- `pyproject.toml` - Project metadata and build configuration

## Running the Agent

```bash
python src/main.py
```

## Development

To add new capabilities to the agent:
1. Create a new tool in `src/tools/`
2. Implement the required interface
3. Register the tool in the agent configuration

### Adding New Dependencies

To add new dependencies:
```bash
uv pip install package-name
uv pip freeze > requirements.txt
```

## Running with ADK

```bash
# cli
adk run scr

# Web UI
adk web
```


## Evaluations

```bash
pytest src/eval/
```

## License

MIT License
