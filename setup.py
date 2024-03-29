import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapinsta",
    version="0.0.3",
    author="Matheus Kolln",
    author_email="matheuzhenrik@gmail.com",
    description="A package to scraping data from Instagram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheuskolln/scrapinsta",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
