import unittest
import os
from unittest.mock import patch
from config import Config

class TestPhase15Config(unittest.TestCase):

    def setUp(self):
        # Clear out env vars before each test to ensure isolation
        self.patcher = patch.dict(os.environ, clear=True)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_default_config_loads_development(self):
        config = Config()
        self.assertEqual(config.env, "development")
        self.assertEqual(config.HOST, "127.0.0.1")
        self.assertEqual(config.PORT, 8000)
        self.assertEqual(config.LOG_LEVEL, "DEBUG")

    def test_production_config_enforces_secret_key(self):
        # Set environment to production but leave the secret key empty/default
        os.environ["APP_ENV"] = "production"
        
        # This should crash because production requires a secure key
        with self.assertRaises(ValueError) as context:
            Config()
            
        self.assertIn("CRITICAL: SECRET_KEY must be set in production", str(context.exception))

    def test_production_config_loads_safely_with_secret(self):
        os.environ["APP_ENV"] = "production"
        os.environ["SECRET_KEY"] = "super_secure_test_key"
        
        config = Config()
        self.assertEqual(config.env, "production")
        self.assertEqual(config.SECRET_KEY, "super_secure_test_key")
