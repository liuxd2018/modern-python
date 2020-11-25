import click


import textwrap

from . import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Lanuage edition of wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language):
    """现代化python工程"""
    
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

