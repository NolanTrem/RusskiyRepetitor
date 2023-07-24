import click

@click.group()
@click.pass_context
def cli(ctx) -> None:
    pass

@cli.command()
def hello():
    print("здравствуйте!")
