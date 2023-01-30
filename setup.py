from setuptools import setup, find_packages

requirements = ["numpy", "pgmpy", "pandas", "joblib", "networkx"]

setup(
    name="kltools",
    version="0.0.1",
    description="This repository contains code for implementing the KL divergence method for two networks.",
    author="See AUTHORS",
    author_email="jaron2005@gmail.com",
    install_requires=requirements,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    zip_safe=False,
)
