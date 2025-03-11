# Use Case 2: Agent with Tool Example

This example demonstrates an OpenAI Agent that uses tools to enhance its capabilities.

## Overview

This example shows how to:
- Define and register tools with the OpenAI API
- Process tool calls from the agent
- Execute functions based on the agent's requests
- Handle the conversation flow with tool usage

## Requirements

- Python 3.11
- OpenAI API key

## Tools Implemented

1. **get_current_time**: Returns the current date and time
2. **get_weather**: Returns the weather for a specified location (mock implementation)

## Running Locally

1. Ensure you have set up the environment as described in the main README
2. Run the example:

```bash
python src/main.py
```

## Running with Docker

```bash
cd /path/to/project
docker-compose -f docker/docker-compose.yml up use_case_2
```

## Expected Output

The agent will use tools to respond to the user query, with output similar to:

```
Starting Use Case 2: Agent with Tool Example

Assistant is thinking...
Tool used: get_current_time
Tool used: get_weather

Final Agent Response:
The current time is 2023-07-15 14:30:45. The weather in Tokyo is currently sunny and 72°F.

Use Case 2 completed successfully.
```

## Next Steps

- Add more complex tools
- Implement real API integrations (e.g., actual weather data)
- Create a multi-turn conversation example
- Explore advanced tool calling patterns 