Changelog
=========

This list the changes made between versions

Version 1
---------

18/8/2021: v1.0.5
~~~~~~~~~~~~~~~~~

[NOTE] Even though this is the first changelog entry this is not the first version

- **README:** Rewrote and edited parts of readme to not make it specific to any version
- **Documentation:** Added documentation for using custom storages and added logo and sidebar links to page. Within the Piuma file some more type hints have been added.
- **Logo:** Changed logo with text to be black
- **Pep8:** Applied pep8 formatting to all the python files
- **Storage:** Added a Storage base class. When passing through storage you now have to call the object while passing it through.
- **Piuma:** Added duplicate id check to insert method. Get returns none if document cannot be found instead of returning an error.
- **setup.py:** Long description now reads from "docs/readme.rst" to save some space and make the file cleaner.
