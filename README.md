# python-doc

Open Python docs in the browser.

## Why?

- Google still shows Python 2.7 doc links in search results.
- Inspiration from `rustup doc` which opens docs associated with the installed Rust toolchain.
- You don't need an internet connection to view docs as `python-doc` installs them on your machine.

## Installation

You can simply use `pip` to install `python-doc`:

```
$ pip install python-doc
```

## Usage

You can open the main page associated with _your_ Python version using:

```
$ python-doc
```

You can go to a specific module's page using the `-m` option:

```
$ python-doc -m os
```

If you want to see the docs for a different Python version than your own, you can do that using the `-py` option:

```
$ python-doc -m os -py 3.6
```

To open the docs on the [docs.python.org](https://docs.python.org/) website, you can use the `-w` option:

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
