#!/usr/bin/env python
###############################################################################
# Import library's
import argparse
from jinja2 import Environment, FileSystemLoader
import yaml
import os

###############################################################################
# Global Variables


###############################################################################
# Scripted Actions

def Render(yaml, template, template_directory):
	template = load_template(template, template_directory)
	print template.render(yaml)


def Template(template, template_directory):
	loader = FileSystemLoader(template_directory)
	env = Environment(loader=loader, lstrip_blocks=True, trim_blocks=True)
	return env.get_template(template)


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
		help='Input yaml variable/data file to override default setting. Defaults to Network-Command-Cheat-Sheet.yaml in the current working directory.',
		default="Network-Command-Cheat-Sheet.yaml",
		required=False)

	parser.add_argument(
		'-m', '--md',
		help='Output md variable/data file to override default setting. Defaults to Network-Command-Cheat-Sheet.md in the current working directory.',
		default="Network-Command-Cheat-Sheet.md",
		required=False)

	parser.add_argument(
		'-o', '--output-directory',
		help='Directory where the output file will be saved. Defaults to the current working directory.',
		default=os.getcwd(),
		required=False)

	parser.add_argument(
		'-t', '--template',
		help='Jinja template to be used. Defaults to md-template.j2 in the current working directory.',
		default="md-template.j2",
		required=False)

	parser.add_argument(
		'-d', '--template_directory',
		help='Directory where the Jinja template to be used is located. Defaults to the current working directory.',
		default=os.getcwd(),
		required=False)

	args = parser.parse_args()
	return args


def main():
	args = Args()
	print args.template_directory
	template = Template(args.template, args.template_directory)
	print template
	Render(args.yaml, template, args.template_directory)


if __name__ == '__main__':
	main()

###############################################################################
#
