#!/usr/bin/env python3

import os
import click
from executor import execute


def python_source_files():
    import glob

    include_paths = glob.glob("*.py")
    exclude_paths = []

    return [x for x in include_paths if x not in exclude_paths]


@click.group()
def cli():
    pass


@cli.command()
def start():
    execute("pipenv run gunicorn app:run")


@cli.command()
def black():
    execute("pipenv", "run", "black", *python_source_files())


@cli.command()
def black_check():
    execute("pipenv", "run", "black", "--check", *python_source_files())


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    cli()
