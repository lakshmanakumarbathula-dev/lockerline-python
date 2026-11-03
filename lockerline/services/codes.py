"""Secure pickup-code generation, hashing and verification."""

import hashlib
import hmac
import secrets


def issue_code() -> str:
    return f"{secrets.randbelow(10**6):06d}"


def hash_code(key: str, code: str) -> str:
    return hmac.new(key.encode(), code.encode(), hashlib.sha256).hexdigest()


def matches(key: str, code: str, stored_hash: str) -> bool:
    return hmac.compare_digest(hash_code(key, code), stored_hash)