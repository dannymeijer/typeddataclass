# Typed Data Classes
![v0.0.1](https://img.shields.io/badge/release-v0.0.1-blue)
![Python Versions](https://img.shields.io/badge/python-3.7%20|%203.8-blue)
![Black Logo](https://img.shields.io/badge/code%20style-black-black.svg)

This (simple) library introduces __strict typing__ in a primitive way.  
Requires Python >3.7 as it extends the `dataclasses` module present in version 3.7

This library works by using `__post_init__` to determine types for all variables set 
through the `__init__` method of the subsequent `dataclass`.

See docs: https://docs.python.org/3/library/dataclasses.html#post-init-processing

## Restrictions

Besides being more stringent with regard to typing, the same restrictions as a regular
dataclass also apply on a typed dataclass. The intended use of a typed dataclass is 
hence the same as a dataclass. This library aims to make it easy for one to add typing
to a python project.

This aims to severely reduce the need for boilerplate code.

## Easy to use

So instead of this:

```python
class SomeClass:
    _some_var: str = None
    
    @property
    def some_var(self):
        return self._some_var
    
    @some_var.setter
    def some_var(self, _n: str):
        assert isinstance(_n, str)
        self._some_var = _n
```

It becomes this:
```python
from typeddataclass import typeddataclass

@typeddataclass
class SomeClass:
   some_var: str = None
```

## Requirements

Other than needing Python 3.7 or higher, no further requirements are needed

## Example

Refer to `example/example.py` to see it in action.

## Contributing

I am presenting this work under the GNU GENERAL PUBLIC LICENSE and do not provide any
warranties of any kind. Feel free to raise any PRs or issues, should the need arise.
