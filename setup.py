import os
import sys

from setuptools import setup


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "README.md"), encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="html2phpbbcode",
    version="0.1.4",
    packages=["html2phpbbcode"],
    license="BSD",
    url="https://github.com/tdiam/html2phpbbcode",
    author="Theodoros Diamantidis",
    author_email="diamaltho@gmail.com",
    description="HTML to phpBB-compatible BBCode converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"html2phpbbcode": ["data/defaults.conf"]},
    install_requires=[
        "html2bbcode",
        "regex",
    ],
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)