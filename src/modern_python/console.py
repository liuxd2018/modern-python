import click
from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """现代化python工程"""
    click.echo("你好👋 !")
