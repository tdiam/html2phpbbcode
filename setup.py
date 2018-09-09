import sys

from setuptools import setup


setup(
    name="html2phpbbcode",
    version="0.1.0",
    packages=["html2phpbbcode"],
    license="BSD",
    url="https://lib.ece.ntua.gr/git/tdiam/html2phpbbcode",
    author="Theodoros Diamantidis",
    author_email="diamaltho@gmail.com",
    description="HTML to phpBB BBCode converter",
    package_data={"html2phpbbcode": ["data/defaults.conf"]},
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ]
)