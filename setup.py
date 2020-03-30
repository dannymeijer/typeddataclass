from setuptools import setup
from sys import version_info, stderr, exit, path
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta

PYTHON_CURRENT = version_info[:2]
PYTHON_REQUIRES = (3, 7)

# This check and everything above must remain compatible with Python 3.7.
if PYTHON_CURRENT < PYTHON_REQUIRES:
    stderr.write("""
==========================
Unsupported Python version
==========================

Sorry!  Typing relies on the Dataclasses library which was introduced in Python 3.7
Please update to a newer version of Python to make use of the Typed Dataclass library.
""")
    exit(1)

# only `requirements.txt` needs to be maintained to install proper requirements

long_description = (CURRENT_DIR / "README.md").read_text(encoding="utf8")

with open("requirements.txt", encoding="utf-8") as reqs:
    requirements = reqs.read().splitlines()


description = (
    "Strongly Typed Data Classes"
)

setup(
    name="typeddataclass",
    version="0.1.0",
    packages=["typeddataclass", "typeddataclasses"],
    include_package_data=True,
    url="https://github.com/dannymeijer/typeddataclass",
    license="MIT",
    py_modules=["typeddataclass", "typeddataclasses"],
    install_requires=requirements,
    zip_safe=True,
    author="Danny Meijer",
    author_email="chilltake@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">={0}.{1}".format(*PYTHON_REQUIRES),
    test_suite="tests"
)
