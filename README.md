<div align="center">
	<a href="https://piuma.readthedocs.io/"><img width="200" height="200" style="margin: 20px" src="https://raw.githubusercontent.com/Emit07/piuma/master/logo/piuma.png"></a>
</div>

<span align="center">
	<h3 align="center">Piuma</h3>
	<p align="center">An ultra-lighweight document oriented database</p>
</span>

<div align="center">
	<a href="https://pypi.org/project/piuma/"><img src="https://img.shields.io/pypi/v/piuma"></a>
	<a href="https://github.com/Emit07/piuma/releases/latest"><img src="https://img.shields.io/github/v/tag/emit07/piuma"></a>
	<a href="https://github.com/emit07/piuma/actions"><img src="https://github.com/Emit07/piuma/actions/workflows/ci-workflow.yml/badge.svg"></a>
	<a href="https://piuma.readthedocs.io"><img src="https://readthedocs.org/projects/piuma/badge/?version=latest"></a>
	<a href="https://github.com/Emit07/piuma/blob/master/LICENSE"><img src="https://shields.io/github/license/emit07/piuma"></a>
	<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</div>

Piuma is a lightweight Python library that provides a simple document-oriented interface layer with pluggable storage backends. Piuma is designed around a minimal and flexible core that makes it easy to:

* work with structured and document-like data
* swap or extend storage implementations
* build custom database behaviors

Out of the box, Piuma can be used as a small memory or file backed document store. However, its primary design goal is to serve as a foundation for building more complex or specialized database systems. 

Piuma has three core ideas: 

* Minimal design
* Extensibility
* Compositional Architecture


## Quick Links
* Github: https://github.com/emit07/piuma
* Documentation: https://piuma.readthedocs.io/
* PyPi: https://pypi.org/project/piuma

## Use Cases

Piuma works well in situations where you want a lightweight and embeddable data layer.

* Building prototypes or experimental data systems
* Adding simple document storage to Python applications
* Creating a custom persistence layer without adopting a full database
* Flexibility in rapid development
* Testing environments

## Installing

Piuma is on PyPi and can be installed with PyPi:

```
$ pip install piuma
```

Piuma can also be installed by cloning the Github repository and using:

```
$ pip install .
```

## Getting Started 

Once installed, you can setup Piuma and insert your first Document. 

```python
from piuma import Piuma

piuma = Piuma()
piuma.insert({"name": "Che Guevara", "age": 39})
```

## Extensibility Example

Piuma is designed so storage can be swapped or extended.

```python
from piuma.storage import JSONStorage
from piuma import Piuma

storage = JSONStorage("data/db.json")
db = Piuma(storage=storage)
```

Custom storage backends can be implemented by extending `Storage`.

## Why is it called Piuma?

Piuma (‹più·ma›) is the Italian word for feather, which reflects the design goal. 

