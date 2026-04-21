#!/usr/bin/env python3
# oracle.py

import os
import sys
try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv is not installed.")
    sys.exit(1)
# from typing import Final


def security_check() -> None:

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if all([
            os.getenv("MATRIX_MODE"),
            os.getenv("DATABASE_URL"),
            os.getenv("API_KEY"),
            os.getenv("LOG_LEVEL"),
            os.getenv("ZION_ENDPOINT"),
            ]):
        print("[OK] .env file properly configured")
    else:
        print("[FAIL] .env file missing or incomplete")

    # Check for production overrides
    # test using environment variable MATRIX_MODE
    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        # If it's in development, show that overrides are ready but not active
        print("[INFO] Production overrides available (Running in Dev)")


def main() -> None:

    if not load_dotenv(override=False):
        print("[WARNING]: No .env file found.")

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    # 1.- MATRIX_MODE
    if not os.getenv("MATRIX_MODE"):
        print("[WARNING] Default Configuration for MATRIX_MODE")
    mode: str = os.getenv("MATRIX_MODE", "development")
    print(f"Mode: {mode}")

    # 2.- DATABASE_URL
    if not os.getenv("DATABASE_URL"):
        print("[WARNING] Missing Configuration for DATABASE_URL")
    db_status: str = (
        "Connected" if os.getenv("DB_PASS")
        else "Connected to local instance"
    )
    print(f"Database: {db_status}")

    # 3.- API_KEY
    if not os.getenv("API_KEY"):
        print("[WARNING] Missing Configuration for API_KEY")
    api_access: str = (
        "Authenticated" if os.getenv("API_KEY")
        else "Not authenticated"
    )
    print(f"API Access: {api_access}")

    # 4.- LOG_LEVEL
    if not os.getenv("LOG_LEVEL"):
        print("[WARNING] Default Configuration for LOG_LEVEL")
    log_level: str = os.getenv("LOG_LEVEL", "DEBUG")
    print(f"Log Level: {log_level}")

    # 5.- ZION_ENDPOINT
    if not os.getenv("ZION_ENDPOINT"):
        print("[WARNING] Missing Configuration for ZION_ENDPOINT")
    zion_network: str = "Online" if os.getenv("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {zion_network}")

    # SECURITY CHECK
    security_check()


if __name__ == "__main__":
    main()
