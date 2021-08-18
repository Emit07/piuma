from setuptools import setup, find_packages

f = open("docs/readme.rst", "r")
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name="piuma",
    version="1.0.5",
    license="gpl-3.0",
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="An ultra-lighweight document oriented database",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'database', 'document oriented'],
    url="https://github.com/emit07/piuma",
)
