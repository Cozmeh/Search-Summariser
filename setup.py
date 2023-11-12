from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'Search and summarize the web with ease!'

# Setting up
setup(
    name="summer-search",
    version=VERSION,
    author="Cozmic (Hem Sainath)",
    author_email="hemsainath15@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['bs4', 'requests', 'transformers','sentencepiece','tensorflow','torch'],
    keywords=['python', 'search', 'summerisation', 'summary', 'ml', 'information'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

