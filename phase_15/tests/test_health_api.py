import unittest
import json
from unittest.mock import patch, MagicMock

# Import the actual handler function we created in Phase 14/15
from api.routes.health_routes import health_check

class MockHandler:
    """A mock HTTP handler to intercept responses."""
    def __init__(self):
        self.status_code = None
        self.headers = {}
        self.response_body = b""
        self.wfile = MagicMock()
        
        # Capture writes to wfile
        def write_side_effect(data):
            self.response_body += data
            
        self.wfile.write.side_effect = write_side_effect

    def send_response(self, code):
        self.status_code = code

    def send_header(self, keyword, value):
        self.headers[keyword] = value

    def end_headers(self):
        pass

class TestPhase15HealthAPI(unittest.TestCase):

    @patch("api.routes.health_routes.repo")
    def test_health_check_returns_200_when_db_ok(self, mock_repo):
        # Arrange
        mock_repo.check_health.return_value = True
        handler = MockHandler()

        # Act
        health_check(handler)

        # Assert
        self.assertEqual(handler.status_code, 200)
        
        # Parse the JSON response
        response_json = json.loads(handler.response_body.decode("utf-8"))
        self.assertTrue(response_json["success"])
        self.assertEqual(response_json["data"]["status"], "ok")
        self.assertEqual(response_json["data"]["database"], "connected")

    @patch("api.routes.health_routes.repo")
    def test_health_check_returns_503_when_db_down(self, mock_repo):
        # Arrange
        mock_repo.check_health.return_value = False
        handler = MockHandler()

        # Act
        health_check(handler)

        # Assert
        self.assertEqual(handler.status_code, 503)
        
        response_json = json.loads(handler.response_body.decode("utf-8"))
        self.assertFalse(response_json["success"])
        self.assertEqual(response_json["error"]["message"], "Service Unavailable")
