from setuptools import setup, find_packages

setup(
    name="codegenie",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["black", "pytest"],
    entry_points={
        "console_scripts": [
            "codegenie = codegenie.cli:main",
        ],
    },
)
