# auth.py

import hmac
import hashlib
import base64
import json
import time
from config import config

SECRET_KEY = config.SECRET_KEY


class AuthManager:

    def __init__(self):

        self.current_user = None

    # =========================
    # CREATE JWT
    # =========================

    def _create_jwt(
        self,
        username
    ):

        header = {
            "alg": "HS256",
            "typ": "JWT"
        }

        payload = {
            "sub": username,
            "iat": int(time.time()),
            "exp": int(time.time()) + 86400
        }

        h = base64.urlsafe_b64encode(
            json.dumps(header).encode()
        ).rstrip(b"=").decode()

        p = base64.urlsafe_b64encode(
            json.dumps(payload).encode()
        ).rstrip(b"=").decode()

        message = f"{h}.{p}"

        sig = hmac.new(
            SECRET_KEY.encode(),
            message.encode(),
            hashlib.sha256
        ).digest()

        s = base64.urlsafe_b64encode(
            sig
        ).rstrip(b"=").decode()

        return f"{h}.{p}.{s}"

    # =========================
    # VERIFY JWT
    # =========================

    def _verify_jwt(self, token):

        try:

            parts = token.split(".")

            if len(parts) != 3:
                return None

            h, p, s = parts

            # Verify signature
            message = f"{h}.{p}"

            expected = hmac.new(
                SECRET_KEY.encode(),
                message.encode(),
                hashlib.sha256
            ).digest()

            expected_sig = (
                base64.urlsafe_b64encode(
                    expected
                ).rstrip(b"=").decode()
            )

            if not hmac.compare_digest(
                s, expected_sig
            ):
                return None

            # Decode payload
            padding = 4 - len(p) % 4
            p_padded = p + "=" * padding

            payload = json.loads(
                base64.urlsafe_b64decode(
                    p_padded
                )
            )

            # Check expiry
            if payload.get("exp", 0) < time.time():
                return None

            return payload

        except Exception:
            return None

    # =========================
    # GENERATE TOKEN
    # =========================

    def generate_token(
        self,
        username
    ):

        return self._create_jwt(
            username
        )

    # =========================
    # LOGIN
    # =========================

    def login(self, user):

        self.current_user = user

        token = self.generate_token(user)

        return token

    # =========================
    # LOGOUT
    # =========================

    def logout(self):

        self.current_user = None

    # =========================
    # REQUIRE LOGIN
    # =========================

    def require_login(self):

        if not self.current_user:

            raise PermissionError(
                "Login required"
            )

    # =========================
    # AUTHENTICATE TOKEN
    # =========================

    def authenticate_token(
        self,
        token
    ):

        payload = self._verify_jwt(token)

        if not payload:

            raise PermissionError(
                "Invalid or expired token"
            )

        username = payload.get("sub")

        self.current_user = username

        return username

    # =========================
    # TOKEN EXISTS
    # =========================

    def token_exists(self, token):

        payload = self._verify_jwt(token)

        return payload is not None