# OpenAI Agents Quickstart

This repository contains examples and experiments for working with OpenAI Agents and their tools. It provides a structured approach to explore their capabilities and develop practical applications.

## Repository Structure

```
openai_agents_quickstart/
├── notebooks/           # Jupyter notebooks for experiments
├── examples/            # Specific use case examples
│   ├── use_case_1/
│   │   └── src/         # Python application code
│   ├── use_case_2/
│   │   └── src/
│   └── ...
├── docker/              # Docker configurations
│   ├── Dockerfile
│   └── docker-compose.yml
├── .env.example         # Template for environment variables
├── DOCS.json            # Dictionary of URLs related to OpenAI agents tools
└── README.md            # This file
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
   - poetry or uv recomended over pip :D
- pip (Python package installer)

### Setting Up the Environment

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/openai_agents_quickstart.git
   cd openai_agents_quickstart
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env to add your API keys
   ```

## Running Examples

### Jupyter Notebooks

To run the example notebooks:

```bash
cd notebooks
jupyter notebook
```

### Use Case Examples

Each use case in the `examples/` directory contains its own README with specific instructions.

## Docker Usage

To run the examples using Docker:

```bash
cd docker
docker-compose up
```

## Documentation

Refer to the `DOCS.json` file for links to official documentation and helpful resources related to OpenAI Agents.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 