"""
Introduces strict typing in a primitive way
Requires Python > 3.7 as it extends the `dataclasses` module present in version 3.7

Uses post_init processing to determine types for all variables set through the init method
(see docs: https://docs.python.org/3/library/dataclasses.html#post-init-processing)

Besides being more stringent with regard to typing, he same restrictions as a regular
dataclass also apply on a typed dataclass.

--------------------
Author: Danny Meijer
GitHub: https://github.com/dannymeijer/typeddataclass
"""
import dataclasses


class TypedClass:
    def __post_init__(self):
        _cls = self.__class__

        for _dcf in _cls.__dataclass_fields__:
            _attr = self.__getattribute__(_dcf)
            expected_type = _cls.__dataclass_fields__[_dcf].type
            default = _cls.__dataclass_fields__[_dcf].default

            # Check if type is correct for the given attribute
            if not isinstance(_attr, expected_type):

                # Defaults to None that are set to None (implicit) are skipped
                if isinstance(default, type(None)) and isinstance(_attr, type(None)):
                    continue

                # If a default type is not set, we raise an error
                raise TypeError(
                    f"Wrong type provided for '{_dcf}' - "
                    f"expected {expected_type.__name__.upper()}, "
                    f"got {type(self.__getattribute__(_dcf)).__name__.upper()}"
                )


def typeddataclass(
    _cls=None,
    *,
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
):
    """
    Extends dataclasses.dataclass decorator with typing

    Following code and description are taken form 'dataclass' decorator from
    Python's  `dataclasses` module with some minor changes (`__post_init__` added):
    ---
    Returns the same class as was passed in, with dunder methods
    added based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If
    repr is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method function is added. If frozen is true, fields may
    not be assigned to after instance creation.
    """

    def wrap(cls):
        # Strong typing added here
        cls.__post_init__ = TypedClass.__post_init__
        return dataclasses._process_class(
            cls, init, repr, eq, order, unsafe_hash, frozen
        )

    # See if we're being called as @dataclass or @dataclass().
    if _cls is None:
        # We're called with parens.
        return wrap

    # We're called as @dataclass without parens.
    return wrap(_cls)
