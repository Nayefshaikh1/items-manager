# config.py

import os
import json

class Config:
    """Central configuration manager for the application."""

    def __init__(self):
        # Default to development if not specified
        self.env = os.environ.get("APP_ENV", "development").lower()

        # Try to load environment-specific .env file manually 
        # (avoiding external libraries like python-dotenv to stick to vanilla Python)
        self._load_env_file(f".env.{self.env}")
        self._load_env_file(".env") # fallback to local overrides

        # --- ENVIRONMENT VARIABLES ---

        # Server Config
        self.HOST = os.environ.get("APP_HOST", "127.0.0.1")
        self.PORT = int(os.environ.get("APP_PORT", 8000))

        # Database Config
        # Production might use a different DB file or an external path
        self.DB_PATH = os.environ.get("DB_PATH", "database.db")

        # Security
        self.SECRET_KEY = os.environ.get(
            "SECRET_KEY", 
            "fallback_unsafe_dev_key_only"
        )
        if self.env == "production" and self.SECRET_KEY == "fallback_unsafe_dev_key_only":
            raise ValueError("CRITICAL: SECRET_KEY must be set in production environment!")

        # Logging
        self.LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG" if self.env == "development" else "INFO")

    def _load_env_file(self, filename):
        """Simple parser for .env files."""
        if not os.path.exists(filename):
            return

        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                
                parts = line.split("=", 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    val = parts[1].strip()
                    # Strip quotes if present
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'"):
                        val = val[1:-1]
                    
                    # Only set if not already in the OS environment
                    if key not in os.environ:
                        os.environ[key] = val

# Singleton instance to be used across the app
config = Config()
