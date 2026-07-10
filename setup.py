from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="padmadb",
    version="0.1.2", 
    author="Heramb Rajesh Jaipurkar",
    author_email="heramb999jaipurkar@gmail.com",
    description="A blazing-fast, lightweight in-memory vector database built in pure Python.",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/herambjaipurkar/Padmadb",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "pydantic>=2.0.0",
        "requests>=2.31.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)