#!/usr/bin/env python
"""
Use Case 1: Simple Agent Example
This demonstrates a basic OpenAI Agent setup that can answer questions.
"""

import os
import sys
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def check_env():
    """Check if the required environment variables are set."""
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it in the .env file or as an environment variable.")
        sys.exit(1)

def main():
    """Main function to run the example."""
    check_env()
    
    print("Starting Use Case 1: Simple Agent Example")
    
    try:
        # Import OpenAI package
        from openai import OpenAI
        
        # Initialize the client
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        
        # Simple completion example
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Write a haiku about the ocean."}
            ]
        )
        
        # Print the response
        print("\nAgent Response:")
        print(response.choices[0].message.content)
        
        print("\nUse Case 1 completed successfully.")
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 