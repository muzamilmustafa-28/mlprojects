from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
    #-e. in the requirements.txt file will automatically trigger setup.py file
    #but when i am running this code here -e . should not come so i have to remove it for that i have 
    #to write the condition

setup(
    name = 'mlproject',
    version = '0.01',
    author='krish',
    author_email='muzamilmustafa28@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
     
)