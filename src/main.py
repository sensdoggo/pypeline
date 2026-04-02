import typer

app = typer.Typer()

@app.command()
def main():
    print("hello from pypeline")

if __name__ == "__main__":
    app()
