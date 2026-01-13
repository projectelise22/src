import os

ENVIRONMENTS = {
    "dev": "https://jsonplaceholder.typicode.com",
    "staging": "https://jsonplaceholder.typicode.com",
    "prod": "https://jsonplaceholder.typicode.com",
}

def get_base_url():
    env = os.getenv("ENV", "dev")
    return ENVIRONMENTS[env]