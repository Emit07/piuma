from setuptools import setup, find_packages

setup(
    name="piuma",
    version="1.1.0",
    license="gpl-3.0",
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="An ultra-lighweight document oriented database",
    long_description_content_type="text/x-rst",
    long_description=open("README-PYPI.rst").read(),
    packages=find_packages(),
    keywords=['python', 'database', 'document oriented'],
    url="https://github.com/emit07/piuma",
)
