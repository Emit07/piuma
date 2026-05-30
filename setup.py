from setuptools import setup, find_packages

LONG_DESCRIPTION = """
Piuma
=====

Piuma is a lightweight Python library that provides a simple
document-oriented interface layer with pluggable storage backends. Piuma
is designed around a minimal and flexible core that makes it easy to:

-  work with structured and document-like data
-  swap or extend storage implementations
-  build custom database behaviors

Out of the box, Piuma can be used as a small memory or file backed
document store. However, its primary design goal is to serve as a
foundation for building more complex or specialized database systems.
Piuma has three core structural principles: minimal design,
extensibility, compositional architecture.

Quick Links
-----------

-  Github: https://github.com/emit07/piuma
-  Documentation: https://piuma.readthedocs.io/
-  PyPi: https://pypi.org/project/piuma

Use Cases
---------

Piuma works well in situations where you want a lightweight and
embeddable data layer.

-  Building prototypes or experimental data systems
-  Adding simple document storage to Python applications
-  Creating a custom persistence layer without adopting a full database
-  Flexibility in rapid development
-  Testing environments

Why is it called Piuma?
-----------------------

Piuma (‹più·ma›) is the Italian word for feather, which reflects the
design goals.
"""

setup(
    name="piuma",
    version="1.1.2",
    license="gpl-3.0",
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="A lighweight document oriented database interface written in python",
    long_description_content_type="text/x-rst",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'database', 'document oriented'],
    url="https://github.com/emit07/piuma",
)
