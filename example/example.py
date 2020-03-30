"""
Usage examples for Typed Data Classes
"""
from typeddataclasses import typeddataclass, TypedClass, dataclass

# alternative way to import:
# ```from typeddataclass import typeddataclass, TypedClass, dataclass```
# The entire default `dataclasses` library is also available through
# typeddataclass/typeddataclasses.


# Two valid ways to make a typed data class

# 1. Decorator way
# Using `typeddataclass` decorator
# This is the preferred way when building new dataclasses that require strong typing


@typeddataclass
class MyDataClass:
    """Typed Data Class example (preferred way)"""

    name: str
    publisher: str
    country: str

    first_appearance: int or float
    # Note:  only the first type will be picked up when this type of notation is used
    # It's a valid Python way of doing things, but it since it breaks strong typing,
    # all subsequent entries are simply ignored

    # This sets the field to `optional`
    description: str = None


# 2. Class way
# Using `TypedClass` needs `dataclasses.dataclass` decorator to be set, otherwise
# typing will be ignored. With this way, typing can easily be added to existing
# DataClasses. Simply make the class inherit from TypedClass


@dataclass
class MyDataClass2(TypedClass):
    """Typed Data Class example (alternative way)"""

    brand: str
    make: str = None

    # Of course it is also possible to add a default value of the same type as what the
    # field is set to. Setting the default value to another type as the field will
    # raise a TypeError.
    weight: float = 1.0


# Usage Examples:
# A class derived from a typed dataclass will have an auto-generated __init__
# among other primitives. Here are two examples:


class Hero(MyDataClass):
    """This class will have an __init__ that is auto-filled from the dataclass"""

    # Adding additional class variables will not change the class signature
    good_guy = True

    def print_dict(self):
        print(self.__dict__)


class Villain(MyDataClass):
    """This class will have the same (typed) signature as the previous one"""

    def say_boo(self):
        print(f"{self.name} says: BOO")


@typeddataclass
class SideKick(MyDataClass):
    # When inheriting from an existing (typed) DataClass, the new class also has to be
    # decorated for the class signature to be updated.
    has_powers: bool = True

    # Note: when adding more variables that default values will have to be set
    # either to None or of the same type as intended if the inherited class already has
    # defaults. This can be ignored if the inherited class has no defaults set.


# Class signature is now set and also typed
# ```python
# ce = ClassExample()
# ```
# Will result in: ```TypeError: __init__() missing 4 required positional arguments: 'name', 'region', 'country', and 'year_started'```
# Note that the class signature is also made positional based on the order give in the
# DataClass - this is default DataClass behavior.

# Here is a sample class call where the wrong type is used for country (int).
# ```python
# ce = ClassExample(
#     name="myName",
#     region="myRegion",
#     country=31,
#     year_started=2020
# )
# ```
# Will result in: ```TypeError: Wrong type provided for 'country' - expected STR, got INT```

# Correct usage:
spidee = Hero(
    name="Spider Man",
    publisher="Marvel Comics",
    country="USA",
    first_appearance=1962,
)

mandarin = Villain(
    name="The Mandarin",
    publisher="Marvel Comics",
    country="China",
    first_appearance=1964,
)

falcon = SideKick(
    name="Falcon",
    publisher="Marvel Comics",
    country="USA",
    first_appearance=1969,
    has_powers=False,
)

spidee.print_dict()
print(mandarin.__dict__)
mandarin.say_boo()
print(falcon.__dict__)
