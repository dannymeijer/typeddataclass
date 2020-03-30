"""
Unit tests for typed dataclass
"""

import unittest
from typeddataclass import typeddataclass, TypedClass, dataclass, is_dataclass


class CustomType:
    """Placeholder class used for testing non-standard types"""


class TypedClassTest(unittest.TestCase):
    _ct = CustomType()

    @typeddataclass
    class ClassForTesting:
        a: str  # string expected, no default set
        b: float  # float expected, no default set
        c: list  # list expected, no default
        d: dict  # dict expected, no default
        e: int  # int expected, no default
        f: CustomType  # CustomType expected, no default
        g: str = None  # nullable string
        h: float = None  # nullable float
        i: str = ""  # string expected, default to empty string

    class NotADataClass(TypedClass):
        def __init__(self):
            pass

    def _helper(self, exception: str, exception_type=TypeError, **data):
        """helper function to reduce verbosity in subsequent tests"""
        with self.assertRaises(exception_type) as cm:
            self.ClassForTesting(**data)
        actual_exception = cm.exception.__str__()
        self.assertEqual(actual_exception, exception)

    def test_string_type(self):
        self._helper(
            exception="Wrong type provided for 'a' - expected STR, got INT",
            exception_type=TypeError,
            a=1,  # Wrong value
            b=1,
            c=[],
            d={},
            e=1,
            f=CustomType(),
        )

    def test_float_type(self):
        self._helper(
            exception="Wrong type provided for 'b' - expected FLOAT, got INT",
            exception_type=TypeError,
            a="a",
            b=1,  # Wrong value
            c=[],
            d={},
            e=1,
            f=CustomType(),
        )

    def test_list_type(self):
        self._helper(
            exception="Wrong type provided for 'c' - expected LIST, got INT",
            exception_type=TypeError,
            a="a",
            b=1.0,
            c=1,  # Wrong value
            d={},
            e=1,
            f=CustomType(),
        )

    def test_dict_type(self):
        self._helper(
            exception="Wrong type provided for 'd' - expected DICT, got INT",
            exception_type=TypeError,
            a="a",
            b=1.0,
            c=[],
            d=1,  # Wrong value
            e=1,
            f=CustomType(),
        )

    def test_int_type(self):
        self._helper(
            exception="Wrong type provided for 'e' - expected INT, got STR",
            exception_type=TypeError,
            a="a",
            b=1.0,
            c=[],
            d={},
            e="not an int",  # Wrong value
            f=CustomType(),
        )

    def test_custom_type(self):
        self._helper(
            exception="Wrong type provided for 'f' - expected CUSTOMTYPE, got INT",
            exception_type=TypeError,
            a="a",
            b=1.0,
            c=[],
            d={},
            e=1,
            f=1,  # Wrong value
        )

    def test_none_in_mandatory_field(self):
        self._helper(
            exception="Wrong type provided for 'e' - expected INT, got NONETYPE",
            exception_type=TypeError,
            a="a",
            b=1.0,
            c=[],
            d={},
            e=None,  # Wrong value, should not be nullable
            f=CustomType(),
        )

    def test_handling_none_types(self):
        self._helper(
            exception="Wrong type provided for 'a' - expected STR, got NONETYPE",
            exception_type=TypeError,
            a=None,
            b=None,
            c=None,
            d=None,
            e=None,
            f=None,
        )

    def test_handling_default_value(self):
        self._helper(
            exception="Wrong type provided for 'g' - expected STR, got INT",
            exception_type=TypeError,
            a="a",
            b=1.0,
            c=[],
            d={},
            e=1,
            f=CustomType(),
            g=1,  # Wrong value
            h=None,
            i="",
        )

    def test_not_in_order(self):
        self._helper(
            exception="Wrong type provided for 'g' - expected STR, got INT",
            exception_type=TypeError,
            i="",
            c=[],
            a="a",
            f=CustomType(),
            b=1.0,
            h=None,
            d={},
            e=1,
            g=1,  # Wrong value
        )

    def test_valid_class(self):
        valid_class = self.ClassForTesting(
            a="a", b=1.0, c=[], d={}, e=1, f=self._ct, i="test"
        )
        expected_dict = {
            "a": "a",
            "b": 1.0,
            "c": [],
            "d": {},
            "e": 1,
            "f": self._ct,
            "g": None,
            "h": None,
            "i": "test",
        }
        self.assertDictEqual(valid_class.__dict__, expected_dict)

    def test_is_dataclass(self):
        # TypedClass (or a derivative thereof) should never respond True to is_dataclass
        self.assertFalse(is_dataclass(self.NotADataClass))
        self.assertFalse(is_dataclass(TypedClass))

        # Properly decorated DataClasses however should
        @dataclass()
        class ClassForTesting2(TypedClass):
            pass

        self.assertTrue(is_dataclass(ClassForTesting2))
        self.assertTrue(is_dataclass(self.ClassForTesting))


if __name__ == "__main__":
    unittest.main()
