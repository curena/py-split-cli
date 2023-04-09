import typer

class MyApp:
    app = typer.Typer()

    @app.command(name='hello', no_args_is_help=True)
    @staticmethod
    def hello(name: str):
        """
        Say hello to someone.
        """
        typer.echo(f"Hello, {name}!")

    @app.command(name='goodbye')
    @staticmethod
    def goodbye(name: str, formal: bool = False):
        """
        Say goodbye to someone.
        """
        if formal:
            typer.echo(f"Goodbye, {name}. Have a nice day.")
        else:
            typer.echo(f"See you later, {name}!")

if __name__ == "__main__":
    my_app = MyApp()
    my_app.app() # This will run the Typer app
