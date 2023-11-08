from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Search and summarize the web with ease!'

# Setting up
setup(
    name="summersearch",
    version=VERSION,
    author="Cozmic (Hem Sainath)",
    author_email="hemsainath15@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests', 'transformers','sentencepiece','tensorflow','torch'],
    keywords=['python', 'search', 'summerisation', 'summary', 'ml', 'information'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)