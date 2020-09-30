# python-doc

Open Python docs in the browser.

## Background

- Search engines still take you to Python 2.7 docs, and not the docs for the Python version you're using.
- `python-doc` installs all docs on your machine, so you don't need an internet connection to view them.
- You can also ask `python-doc` to take you to the [docs.python.org](https://docs.python.org/) website.

Inspired by `rustup doc` which opens docs associated with the installed Rust toolchain in your browser.

## Installation

You can simply use `pip` to install `python-doc`:

```
$ pip install python-doc
```

## Usage

You can open the main docs page for _your_ Python version using:

```
$ python-doc
```

You can also go to a specific module's doc page using the `-m` option:

```
$ python-doc -m os
```

If you want to see the docs for a different Python version than your own, you can use the `-py` option:

```
$ python-doc -m os -py 3.6
```

To open docs on the [docs.python.org](https://docs.python.org/) website, you can use the `-w` option:

```
$ python-doc -m os -py 3.6 -w
```

To look at all the available options, you can check out the help using:

```
$ python-doc --help
```

## Versioning

`python-doc` uses [Calendar Versioning](https://calver.org/). For the available versions, see the tags on the GitHub repository.

## License

This project is licensed under the Apache License, see the [LICENSE](https://github.com/vinayak-mehta/python-doc/blob/master/LICENSE) file for details.
