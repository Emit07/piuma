from setuptools import setup, find_packages

if sys.version_info < (3, 6):                                                                                           
    sys.exit('Python 3.6 or greater is required for Snek')  

setup(
    name="piuma",
    version="v1.0.0",
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="An ultra-lighweight document oriented database",
    packages=find_packages(),
    keywords=['python', 'database', 'document oriented'],
    url="https://github.com/emit07/piuma",
)