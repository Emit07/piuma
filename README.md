<div align="center">
	<img width="200" height="200" style="margin: 20px" src="https://raw.githubusercontent.com/Emit07/piuma/master/logo/piuma.png">
</div>

<span align="center">
	<h2 align="center">Piuma</h2>
	<p align="center">A ultra-lighweight document oriented database written in 54 lines of python</p>
</span>

Piuma is an no-headache ultra-lightweight local document database written purely in python. With just over 50 lines (54 lines to be precise) of active code Piuma is designed with just the **absoulute bare** essentials in mind. In the core version of Piuma there is no query language or any advanced search/modify functions. In its current version Piuma only stores data in memory, I plan to add local storage hopefully in the near future. This database should not be taken too seriously and should really only be used for small projects and testing.

## Why you *should* use Piuma?
* **Light and Small:** Piuma is written in 54 lines of code and can be sub millisecond fast because of its memory storage
* **Easy to Use:** Piuma runs out of the box and is easy to use and learn
* **Experimenting:** If you are trying something new and you need a fast database that *just works* then Piuma is a good choice

## Why you *should not* use Piuma?
* **Big Database:** Piuma was not designed to be used as a big database; Piuma only runs in *only* memory (for now) so the limit of how big it could be comes much quicker than other database
* **ACID Guarantees:** Because of Piumas small nature it does not have room for ACID Guarantees
* **Query Language:** Piuma does not have a query language (allthough I plan to add one in a submodule in the future)

## Why is it called Piuma?

Piuma (‹più·ma›) is the Italian word for feather and (from what I feel) the word feather can convay lightness. Also I am a little proud of the logo I made :]

# Documentation

Real Documentation is coming soon, I am writing this in a plane please be patient.

## Installing

Piuma is not on pypy yet (coming very soon). You can download this repo and have fun from there.

## Getting Started 

Once "Installed" you can setup Piuma and insert your first Document. 

```python
from piuma import Piuma

piuma = Piuma()
piuma.insert({"name": "Che Guevara", "age": 39})
```


