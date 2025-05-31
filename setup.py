from setuptools import Extension, find_packages, setup
from Cython.Build import cythonize

import os

_VERSION = "1.2"

# Get the directory of setup.py
SETUP_DIR = os.path.dirname(os.path.abspath(__file__))

def get_extensions():
    # Import numpy here, ensure it's available via setup_requires or [build-system].requires
    import numpy

    # Paths to .pyx files should be relative to setup.py
    extensions = [
        Extension(
            "monotonic_align.core",
            ["monotonic_align/core.pyx"],
            include_dirs=[numpy.get_include()]
        ),
        Extension(
            "monotonic_align.core1alt",
            ["monotonic_align/core1alt.pyx"],
            include_dirs=[numpy.get_include()]
        ),
        Extension(
            "monotonic_align.core2",
            ["monotonic_align/core2.pyx"],
            include_dirs=[numpy.get_include()]
        ),
        Extension(
            "monotonic_align.core2eps",
            ["monotonic_align/core2eps.pyx"],
            include_dirs=[numpy.get_include()]
        ),
    ]
    # Cython will convert .pyx to .c files.
    # Setuptools handles the paths for compilation.
    return cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
        # force=True, # Removed: let Cython decide when to recompile
    )

setup(
  name="monotonic_align",
  version=_VERSION,
  packages=find_packages(),
  # setup_requires ensures numpy and cython are available for setuptools to run this setup.py
  # For PEP 517 builds (e.g. with `python -m build`),
  # [build-system].requires in pyproject.toml is used.
  setup_requires=["numpy", "cython"],
  # ext_modules can be a list or a callable.
  # If callable, it's called by setuptools to get the list of Extension objects.
  # Calling the function directly to provide the list.
  ext_modules=get_extensions(),
  package_data={
      "monotonic_align": ["*.pyx"],
  },
  python_requires='>=3.7',
)
