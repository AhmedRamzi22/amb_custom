from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amb_custom/__init__.py
from amb_custom import __version__ as version

setup(
	name="amb_custom",
	version=version,
	description="AMB Customizations for ERPNext",
	author="Saudi BTI",
	author_email="devs@thebantoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
