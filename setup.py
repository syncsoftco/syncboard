from setuptools import setup, find_packages

setup(
    name="SyncBoard",
    version="0.1.0",
    author_email="syncsoft@googlegroups.com",
    description="A Python library for synchronizing issues between Notion and GitHub.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/syncsoftco/syncboard",
    packages=find_packages(),
    install_requires=[
        "notion-client",
        "requests>=2.25.1",
        "python-dotenv>=0.19.2"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.8',
)
