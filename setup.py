from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requiremnts

    input: file_path (str): requirements.txt file
    output: requirements
    """
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [requirement.strip() for requirement in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Schduler",
    version="0.0.1",
    author="manish",
    author_email="manishyadav62995@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("./requirements.txt"),
)
