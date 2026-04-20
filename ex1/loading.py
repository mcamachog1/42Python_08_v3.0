#!/usr/bin/env python3

from importlib import metadata
import sys


def check_packages(
        required_packages: list[str]) -> dict[str, str]:

    result: dict[str, str] = {}
    for package in required_packages:
        try:
            result[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            result[package] = "Not found"
    return result


def pip_instructions() -> None:
    print("Installing with pip:")
    print("pip install -r requirements.txt")
    print("python3 loading.py\n")    


def poetry_instructions() -> None:
    print("Installing with Poetry")
    print("poetry install")
    print("poetry run python3 loading.py\n")   


def check_dependencies(result: dict[str, str], package_description: dict[str, str]) -> None:
    installed_packages: list[str] = [k for k, v in result.items() if v != "Not found"]

    print("Checking dependencies:")

    for k in result.keys():
        if k in installed_packages:
            print(f"[OK] {k} ({result[k]}) - {package_description[k]} ready")
        else:
            print(f"[ERROR] {k} - {package_description[k]} not found")

    print()


def main() -> None:
    required_packages = ["pandas", "numpy", "matplotlib"]
    package_description: dict[str, str] = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "matplotlib": "Visualization"
            }    
    result: dict[str, str] = check_packages(required_packages)
   
    check_dependencies(result, package_description)
    if "Not found" in result.values():
        pip_instructions()
        poetry_instructions()
        return
    print("Run analysis and visualization")



if __name__ == "__main__":
    main()

