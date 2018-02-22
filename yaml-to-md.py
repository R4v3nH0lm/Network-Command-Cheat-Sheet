#!/usr/bin/env python
###############################################################################
# Import library's
import argparse
import jinja2
import yaml
import os

###############################################################################
# Global Variables


###############################################################################
# Scripted Actions

def Template():
	loader = FileSystemLoader(template_directory.rstrip('/'))
	template = env.get_template('md-template.j2')


def Args():
	parser = argparse.ArgumentParser(
		description="Python script for converting network commands in a yaml file to markdown for posting on github.",
		epilog="""
		NOTE: The following pre-requisites need to be in place before this script will work.
		1.) A input yaml file in the correct format.
		""",
		formatter_class=argparse.RawDescriptionHelpFormatter
	)
	parser.add_argument(
		'-y', '--yaml',
		help='Input yaml variable/data file to override default setting. Defaults to the current working directory.',
		default="Network-Command-Cheat-Sheet.yaml",
		required=False)

	parser.add_argument(
		'-m', '--md',
		help='Output md variable/data file to override default setting. Defaults to the current working directory.',
		default="Network-Command-Cheat-Sheet.md",
		required=False)

	parser.add_argument(
		'-o', '--output-directory',
		help='Directory where the output file will be saved. Defaults to the current working directory.',
		default=os.getcwd(),
		required=False)

	parser.add_argument(
		'-d', '--template-directory',
		help='Directory where the Jinja template is located. Defaults to the current working directory.',
		default="md-template.j2",
		required=False)

	parser.parse_args()


def main():
	Args()
	Template()


if __name__ == '__main__':
	main()

###############################################################################
# 
