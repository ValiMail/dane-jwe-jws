"""Setup script for dane-discovery."""
import os
import re
from setuptools import setup


PROJECT_NAME = "dane_jwe_jws"


def get_file_contents(file_name):
    """Return the contents of a file."""
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
        return f.read()


def get_version():
    """Return the package version."""
    init_file = get_file_contents(os.path.join(PROJECT_NAME, "__init__.py"))
    rx_compiled = re.compile(r"\s*__version__\s*=\s*\"(\S+)\"")
    ver = rx_compiled.search(init_file).group(1)
    return ver


def build_long_desc():
    """Return the long description of the package."""
    return "\n".join([get_file_contents(f) for f in ["README.rst"]])


setup(name=PROJECT_NAME,
      version=get_version(),
      author="Ash Wilson",
      author_email="ash.d.wilson@gmail.com",
      description="A library for using DANE for identity-secured JWE and JWS.",
      license="BSD",
      keywords="dane tlsa dns jwe jws",
      url="https://github.com/valimail/{}".format(PROJECT_NAME),
      packages=[PROJECT_NAME],
      long_description=build_long_desc(),
      long_description_content_type="text/x-rst",
      install_requires=["dane_discovery==0.20", 
                        "jwcrypto>=0.7,<2.0"],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security",
        "License :: OSI Approved :: BSD License"
        ],)
