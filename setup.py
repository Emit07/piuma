from setuptools import setup, find_packages

LONG_DESCRIPTION = """
Piuma
=====

Piuma is an no-headache ultra-lightweight local document database written
purely in python. Piuma is designed without just the **absoulute bare**
essentials in mind. In the core version of Piuma there is no query language or
any advanced search/modify functions. In its current version Piuma only stores
data in memory, I plan to add local storage subpackage hopefully in the near
future. This database should not be taken too seriously and should really only
be used for small projects and testing.

Quick Links
-----------
- Github: https://github.com/emit07/piuma
- Documentation: https://piuma.readthedocs.io/

Why you *should* use Piuma?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Light and Small:** Piuma's core is written with one very small file and can
    be sub millisecond fast because of its memory storage
- **Easy to Use:** Piuma runs out of the box and is easy to use and learn.
    Piuma also requires no dependencies or external servers.
- **Experimenting:** If you are trying something new and you need a fast
    database that just works while testing then Piuma is a good choice.
- **No Dependencies:** Piuma is written with no external dependecies.

Why you *should not* use Piuma?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Big Database:** Piuma was not designed to be used as a big database; Piuma
    only runs *only* in memory (for now) so the limit of how big it could be
    comes much quicker than other database
- **ACID Guarantees:** Because of Piumas small nature it does not have room for
    ACID_ Guarantees
- **Query Language:** Piuma does not have a query language (though I currently
    working on a query submodule)
- **Storage:** While Piuma supports interchangeable storage, it only has memory
    storage built in

Why is it called Piuma?
~~~~~~~~~~~~~~~~~~~~~~~

Piuma is the Italian word for feather and (from what I feel) the word feather
can convay lightness.

.. _ACID: https://en.wikipedia.org/wiki/ACID
"""

setup(
    name="piuma",
    version="1.1.1",
    license="gpl-3.0",
    author="Alessandro De Leo",
    author_email="emit07@protonmail.com",
    description="An ultra-lighweight document oriented database",
    long_description_content_type="text/x-rst",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'database', 'document oriented'],
    url="https://github.com/emit07/piuma",
)
