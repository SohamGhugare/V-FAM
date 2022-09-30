import os
from configparser import ConfigParser

def set_up():
    # Sets up configuration for the app

    env = os.getenv("ENV", ".config")

    if env == ".config":
        config = ConfigParser()
        config.read(".config")
        config = config["AUTH0"]
    else:
        config = {
            "API_AUDIENCE": os.getenv("API_AUDIENCE", "http://127.0.0.1:8000"),
            "ALGORITHMS": os.getenv("ALGORITHMS", "RS256"),
        }
    return config