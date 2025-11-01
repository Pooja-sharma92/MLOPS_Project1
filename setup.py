from setuptools import find_packages,setup
HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    

setup(
    name="MLOPS_Project1",
    version="0.0.1",
    author = "Pooja Sharma",
    author_email="pooja.sharma@example.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)