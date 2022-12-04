from setuptools import setup
from setuptools import find_packages


setup(
	name = "snowflake",
	version = "1.0.0",
	description = "This package contains some sample codes",
	author = "Paria Amiri",
	packages = find_packages(),
	entry_points = {
		"console_scripts":[
			"snowflake-cli = snowflake.let_it_snow:main"
		],
)
