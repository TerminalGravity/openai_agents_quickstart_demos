# Jupyter Notebooks for OpenAI Agents

This directory contains Jupyter Notebooks that demonstrate various concepts and techniques for working with OpenAI Agents.

## Notebook Files

### 1. Introduction to OpenAI Agents (`01_openai_agents_intro.ipynb`)

This notebook provides a basic introduction to working with OpenAI Agents and tools:
- Setting up the OpenAI client
- Making simple chat completions
- Using tools with agents
- Building multi-turn conversations

### 2. Advanced OpenAI Agents with Tools (`02_advanced_agent_tools.ipynb`)

This notebook demonstrates more advanced usage patterns:
- Creating structured tools with Pydantic
- Building advanced multi-tool agents
- Implementing specialized agents
- Coordinating multi-agent workflows

### 3. Building Complex Agent Workflows with LangGraph (`03_langgraph_agents.ipynb`)

This notebook shows how to build complex agent workflows using LangGraph:
- Creating specialized agents for research and coding
- Building a supervisor to manage agent coordination
- Implementing conditional workflows
- Handling multi-stage task execution

## Usage Instructions

To use these notebooks:

1. Ensure you have set up your environment with the required packages (see main README)
2. Rename these `.json` files to `.ipynb` (they are stored as `.json` for compatibility)
3. Set up your API keys in a `.env` file
4. Run the notebooks in Jupyter or a compatible environment

## Available via Docker

You can also run these notebooks using Docker:

```bash
cd /path/to/project
docker-compose -f docker/docker-compose.yml up jupyter
```

Then access the Jupyter server at http://localhost:8888
