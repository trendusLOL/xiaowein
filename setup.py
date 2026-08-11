from setuptools import setup, find_packages

setup(
    name="xiaowein",
    version="0.1.0",
    author="TrendusLOL",
    author_email="ojhhjvj4@gmail.com",
    description="An OpenAI Sora 2 Python SDK fallback client layer.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # TL-MIT functions like MIT legally
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "urllib3>=2.0.0",
        "python-dotenv>=1.0.1",
        "httpx>=0.25.0", # Added for async operations
    ],
)
