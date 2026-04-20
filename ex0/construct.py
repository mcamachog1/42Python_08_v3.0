#!/usr/bin/env python3


import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_path_package() -> str:
    paths: list[str] = site.getsitepackages()

    for path in paths:
        if "site-packages" in path:
            return path
    return ""


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def outside_matrix():
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print(
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scriptsi\\activate # On Window\n"
    )

    print("Then run this program again.")


def inside_matrix():
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(get_path_package())
    print()


def main():
    if is_virtual_env():
        inside_matrix()
    else:
        outside_matrix()


if __name__ == "__main__":
    main()

