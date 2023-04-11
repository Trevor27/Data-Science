from setuptools import setup,find_packages
setup(
    name= 'validate_sa_id',
    version= '1.0.0',
    description = 'this package is about validating SA Id number',
    author= 'Mpho Mashau',
    install_requires = ['pytest'], 
    packages= find_packages(),
)