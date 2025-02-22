from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the List of requirements from the requirements.txt file.
    It filters out the '-e .' if it's present, which is commonly used for editable installs.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters and filter out the '-e .' line
        requirements = [req.strip() for req in requirements if req.strip() != HYPEN_E_DOT]

    # Optional: Raise an error if the requirements file is empty
    if not requirements:
        raise ValueError("The requirements.txt file is empty or doesn't contain any valid dependencies.")

    return requirements

# Setup function to install your package
setup(
    name='mlproject',  # Name of your package
    version='0.0.1',  # Version of your package
    author='avina',  # Author name
    author_email='avvvviiiii11@gmail.com',  # Author's email
    packages=find_packages(),  # Automatically discover all packages
    install_requires=get_requirements('requirements.txt'),  # Install dependencies from requirements.txt
)
