from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="json-structure-fatalispm",
    version="0.0.1",
    packages=find_packages(),
    author="Ihor Melnyk",
    author_email="ih.melnyk@gmail.com",
    description="A package that helps you to view structure of json files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="json structure",
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ],
    python_requires='>=3.6',
)

