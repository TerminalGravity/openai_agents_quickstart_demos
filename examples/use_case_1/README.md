# Use Case 1: Simple Agent Example

This example demonstrates a basic OpenAI Agent setup that can answer questions.

## Overview

This simple example shows how to:
- Set up the OpenAI client
- Create a basic completion request
- Handle the response

## Requirements

- Python 3.11
- OpenAI API key

## Running Locally

1. Ensure you have set up the environment as described in the main README
2. Run the example:

```bash
python src/main.py
```

## Running with Docker

```bash
cd /path/to/project
docker-compose -f docker/docker-compose.yml up use_case_1
```

## Expected Output

The agent will generate a haiku about the ocean, with output similar to:

```
Starting Use Case 1: Simple Agent Example

Agent Response:
Waves crash on the shore
Ocean stretches endlessly
Blue meets horizon

Use Case 1 completed successfully.
```

## Next Steps

- Modify the prompt in `main.py` to ask different questions
- Experiment with different models or parameters
- Add more complex functionality 