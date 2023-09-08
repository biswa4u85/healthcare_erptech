from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in healthcare_erptech/__init__.py
from healthcare_erptech import __version__ as version

setup(
	name="healthcare_erptech",
	version=version,
	description="Healthcare Mobile Destop",
	author="erptechin@gmail.com",
	author_email="erptechin@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
