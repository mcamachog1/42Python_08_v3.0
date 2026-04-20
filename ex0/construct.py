#!/usr/bin/env python3


import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_path_package() -> str:
    paths: list[str] = site.getsitepackages()
    # paths: list[str] = sys.path

    for path in paths:
        if "site-packages" in path:
            return path
    return ""


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    if "linux" in sys.platform:
        print("source matrix_env/bin/activate\n")
    elif "win" in sys.platform:
        print("matrix_env\\Scripts\\activate\n")
    else:
        print(
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
        )

    print("Then run this program again.")


def inside_matrix() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(get_path_package())
    print()


def main() -> None:
    if is_virtual_env():
        inside_matrix()
    else:
        outside_matrix()


if __name__ == "__main__":
    main()
