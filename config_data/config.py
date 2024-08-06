import os

from dotenv import load_dotenv, find_dotenv


try:
    load_dotenv(find_dotenv())
except FileNotFoundError:
    print("Warning: .env file not found. Some features may not work as expected.")

# Get environment variables
OPENAI_API_KEY = os.getenv("API_KEY")
