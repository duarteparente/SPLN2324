#!/usr/bin/env python3
'''
NAME
    makepyproject - Python packages template generator

SYNOPSIS
    makepyproject [-n <name>] [-a <author>] [-e <email>] [-d <dep1,dep2,dep3,...>]
    
DESCRIPTION
    Generates a template configuration file and creates a 'pyproject.toml' with it.

    -n      Project name to be added to configuration file
    
    -a      Author name to be added to configuration file
        
    -e      Email to be added to configuration file

    -d      List of dependencies to be added to configuration file
'''
import jinja2, os, json
from jjcli import *
from glob import glob

modes = glob("*.py")

vars = {
    "project": "#FIXME",
    "author": os.getlogin(),
    "email": "#FIXME@",
    "dependencies": []
}

template = jinja2.Template('''[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend= "flit_core.buildapi"

[project]
name ="{{project}}"
authors = [
    {name = "{{author}}", email = "{{email}}"},
]
version = "0.0.1"
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["description"]

dependencies = {{dependencies}}

[project.scripts]
{{project}} = "{{project}}:main"                     
''')


def project_name(cl):
    if "-n" in cl.opt:
        vars["project"] = cl.opt.get("-n")
    elif len(modes) == 1:
        vars["project"] = modes[0].replace(".py","")


def project_dependencies(cl):
    if "-d" in cl.opt:
        vars["dependencies"] = (cl.opt.get("-d")).split(',')


def readMetadata(cl):
    metadata = os.path.expanduser("~/.metadata.json")
    if os.path.isfile(metadata):
        with open(metadata) as f:
                data = json.load(f)
                vars["author"] = data.get("author", os.getlogin())
                vars["email"] = data.get("email", "#FIXME@")
    if "-a" in cl.opt:
        vars["author"] = cl.opt.get("-a")
    if "-e" in cl.opt:
        vars["email"] = cl.opt.get("-e")


def write_config_file():
    file = open("pyproject.toml","w")
    file.write(template.render({
        "project": vars["project"],
        "author": vars["author"],
        "email": vars["email"],
        "dependencies": vars["dependencies"]
    }))


def main():
    cl = clfilter("n:a:e:d:", doc=__doc__)
    project_name(cl)
    project_dependencies(cl)
    readMetadata(cl)
    write_config_file()


if __name__ == "__main__":
    main()