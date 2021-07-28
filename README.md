<div align="center">
	<a href="https://piuma.readthedocs.io/"><img width="200" height="200" style="margin: 20px" src="https://raw.githubusercontent.com/Emit07/piuma/master/logo/piuma.png"></a>
</div>

<span align="center">
	<h3 align="center">Piuma</h3>
	<p align="center">An ultra-lighweight document oriented database</p>
</span>

<div align="center">
	<a href="https://pypi.org/project/piuma/"><img src="https://img.shields.io/pypi/v/piuma?style=flat-square"></a>
	<img src="https://img.shields.io/badge/test%20coverage-100%25-green?style=flat-square">
	<a href="https://piuma.readthedocs.io"><img src="https://readthedocs.org/projects/piuma/badge/?version=latest&style=flat-square"></a>
	<img src="https://img.shields.io/badge/lines-54-green?style=flat-square">
	<img src="https://shields.io/github/size/Emit07/piuma/piuma/piuma.py?style=flat-square">
	<a href="https://github.com/Emit07/piuma/blob/master/LICENSE"><img src="https://shields.io/github/license/emit07/piuma?style=flat-square"></a>
</div>

Piuma is an no-headache ultra-lightweight local document database written purely in python. With just over 50 lines (54 lines to be precise) of active code and a source file that is 3.39kb (comments included) piuma is designed without just the **absoulute bare** essentials in mind. In the core version of Piuma there is no query language or any advanced search/modify functions. In its current version Piuma only stores data in memory, I plan to add local storage subpackage hopefully in the near future. This database should not be taken too seriously and should really only be used for small projects and testing.

## Why you *should* use Piuma?
* **Light and Small:** Piuma is written in 54 lines of code and can be sub millisecond fast because of its memory storage
* **Easy to Use:** Piuma runs out of the box and is easy to use and learn. Piuma also requires no dependencies or external servers.
* **Experimenting:** If you are trying something new and you need a fast database that just works while testing then Piuma is a good choice.

## Why you *should not* use Piuma?
* **Big Database:** Piuma was not designed to be used as a big database; Piuma only runs *only* in memory (for now) so the limit of how big it could be comes much quicker than other database
* **ACID Guarantees:** Because of Piumas small nature it does not have room for [ACID Guarantees](https://en.wikipedia.org/wiki/ACID)
* **Query Language:** Piuma does not have a query language (though I plan to add one in a submodule in the future)

## Why is it called Piuma?

Piuma (‹più·ma›) is the Italian word for feather and (from what I feel) the word feather can convay lightness. Also I am a little proud of the logo I made :]

# Documentation

I recomend checking out the [documentation](https://piuma.readthedocs.io/) I wrote.

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

Once piuma is installed you can setup Piuma and insert your first Document. 

```python
from piuma import Piuma

piuma = Piuma()
piuma.insert({"name": "Che Guevara", "age": 39})
```


