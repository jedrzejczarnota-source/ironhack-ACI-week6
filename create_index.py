import os
import requests
from dotenv import load_dotenv

load_dotenv()                                  # reads the .env file in this folder
API_KEY = os.getenv("PINECONE_API_KEY")

if not API_KEY:
    raise SystemExit("PINECONE_API_KEY not found. Check your .env file.")

response = requests.post(
    "https://api.pinecone.io/indexes",
    headers={
        "Api-Key": API_KEY,
        "Content-Type": "application/json",
        "X-Pinecone-Api-Version": "2026-07",
    },
    json={
        "name": "project-week6",
        "schema": {
            "fields": {
                "_values": {"type": "dense_vector", "dimension": 1536, "metric": "cosine"}
            }
        },
    },
)

print(response.status_code)
print(response.json())