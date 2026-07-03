''' 
 this setup.py is used to install the package and its dependencies.
 configuration of our project is done in this file.
 '''

#  -e . in req.txt refere to setup.py file. It is used to install the package in editable mode.
from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements_list = []
    try:
        with open('requirements.txt') as file:

            lines = file.readlines()

            for line in lines:
                req=line.strip()
                if req and req!= '-e .':
                    requirements_list.append(req)
    
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")

    return requirements_list




setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Dastagir Sheikh",
    author_email="dastgir7999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)