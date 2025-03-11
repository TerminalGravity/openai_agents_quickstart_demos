#!/usr/bin/env python
"""
Use Case 2: Agent with Tool Example
This demonstrates an OpenAI Agent that uses tools to enhance its capabilities.
"""

import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def check_env():
    """Check if the required environment variables are set."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it in the .env file or as an environment variable.")
        sys.exit(1)

def get_current_time():
    """Tool function to get the current time."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_weather(location="New York"):
    """Mock tool function to get the weather for a location."""
    # In a real application, this would call a weather API
    return f"The weather in {location} is currently sunny and 72°F."

def main():
    """Main function to run the example."""
    check_env()
    
    print("Starting Use Case 2: Agent with Tool Example")
    
    try:
        # Import OpenAI package
        from openai import OpenAI
        
        # Initialize the client
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        
        # Define the tools
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_current_time",
                    "description": "Get the current date and time",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA"
                            }
                        },
                        "required": ["location"]
                    }
                }
            }
        ]
        
        # Create the agent with access to tools
        messages = [
            {"role": "system", "content": "You are a helpful assistant with access to tools."},
            {"role": "user", "content": "What time is it now? And what's the weather in Tokyo?"}
        ]
        
        # First call to create the assistant's response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        # Process assistant's response
        assistant_response = response.choices[0].message
        messages.append(assistant_response)
        
        print("\nAssistant is thinking...")
        
        # Check if the assistant wants to call a tool
        if assistant_response.tool_calls:
            # Process each tool call
            for tool_call in assistant_response.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                # Call the appropriate function
                if function_name == "get_current_time":
                    function_response = get_current_time()
                elif function_name == "get_weather":
                    function_response = get_weather(function_args.get("location", "New York"))
                else:
                    function_response = f"Error: Function {function_name} not implemented"
                
                # Add the function response to messages
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                })
                
                print(f"Tool used: {function_name}")
            
            # Get the final response after tool use
            final_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            
            # Print the final response
            print("\nFinal Agent Response:")
            print(final_response.choices[0].message.content)
        else:
            # Print the original response if no tools were used
            print("\nAgent Response (no tools used):")
            print(assistant_response.content)
        
        print("\nUse Case 2 completed successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 