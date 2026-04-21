#!/usr/bin/env python3
# loading.py

from importlib import metadata


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
    print("Installing with Poetry:")
    print("poetry install")
    print("poetry run python3 loading.py\n")


def check_dependencies(
        result: dict[str, str],
        package_description: dict[str, str]) -> None:

    print("Checking dependencies:")

    for k, v in result.items():
        if v == "Not found":
            print(f"[ERROR] {k} - {package_description[k]} not found")
        else:
            print(f"[OK] {k} ({result[k]}) - {package_description[k]} ready")
    print()


def run_analysis() -> None:
    from numpy.random import normal
    from pandas import DataFrame
    from matplotlib import pyplot as plt
    print("Analyzing Matrix data...")
    # Generate data
    data = normal(loc=50, scale=15, size=1000)

    # Generate data table
    df = DataFrame(data, columns=["signal"])

    # Calculate statistics
    mean: float = df["signal"].mean()
    std: float = df["signal"].std()
    count: int = df["signal"].count()

    print(f"Processing {count} data points...")
    print(f"Mean: {mean:.2f}")
    print(f"Std: {std:.2f}\n")

    print("Generating visualization...\n")
    # Draw chart
    plt.hist(df["signal"], bins=30)
    plt.title("Matrix signal distribution")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    required_packages = ["pandas", "numpy", "matplotlib"]
    package_description: dict[str, str] = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "matplotlib": "Visualization"
            }

    print("\nLOADING STATUS: Loading programs...\n")

    result: dict[str, str] = check_packages(required_packages)
    check_dependencies(result, package_description)
    if "Not found" in result.values():
        pip_instructions()
        poetry_instructions()
        return
    run_analysis()


if __name__ == "__main__":
    main()
