from distutils.dist import Distribution
from typing import List

def setup(
    name: str,
    version: str,
    author: str,
    author_email: str,
    description: str,
    long_description: str,
    long_description_content_type: str,
    url: str,
    classifiers: List[str],
    python_requires: str,
    packages: list[str],
) -> Distribution | None: ...
def find_packages() -> list[str]: ...
