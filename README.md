# py-aiger-abc
Aiger <-> ABC bridge

[![PyPI version](https://badge.fury.io/py/py-aiger-abc.svg)](https://badge.fury.io/py/py-aiger-abc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Installation

## Non-Python Dependencies

This package currently assumes that the
[ABC](https://github.com/berkeley-abc/abc) and
[aigtoaig](http://fmv.jku.at/aiger/) commands are installed and in the
PATH. In the future, we hope to automatically include these
dependencies, but currently one needs to install them on their own.

## Python Package

If you just need to use `aiger_abc`, you can just run:

`$ pip install py-aiger-abc`

For developers, note that this project uses the
[poetry](https://poetry.eustace.io/) python package/dependency
management tool. Please familarize yourself with it and then run:

`$ poetry install`

# Usage

The primary entry point for using `aiger_abc` is the `simplify`
function which uses `abc` to simplify an AIG. For example, below we
show how `aiger_abc` can be used to simplify the following inefficient
encoding of const false.

```python
import aiger

x = aiger.atom('x')

f = x ^ x
print(f.aig)
```

```
aag 4 1 0 1 3
2
8
4 2 2
6 3 3
8 5 7
```

```python
import aiger_abc
f2 = aiger_abc.simplify(f)
print(f2.aig)
```

```
aag 1 1 0 1 0
2
0
```

## Explicitly Specifying for `abc` and `aigtoaig` commands

`simplify` supports explicitly specifying the
`abc` and `aigtoaig` commands. This is useful
if you have installed them in non-standard paths
or names. E.g.,

```python
f2 = aiger_abc.simplify(f, abc_cmd='abc', aigtoaig_cmf='aigtoaig')
```
