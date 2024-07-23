from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    This Function will return the list of requirements from out requirements.txt file
    '''
    requirements = []
    with open(file_path) as w:
        requirements = w.readlines()
        requirements = [req.replace("\n", "")for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)


setup(
    name="MLproject",
    version="0.0.1",
    author="Akshat Shethia",
    author_email="akshatshethia@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
