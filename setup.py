from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="image_proccesing",
    version="0.0.1",
    author="Lilian",
    description="",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lilian-retori/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5",
)