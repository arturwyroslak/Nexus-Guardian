import typer
from nexus_guardian.core import Guardian

app = typer.Typer()

@app.command()
def start(
    path: str = typer.Option(".", help="Path to the repository to scan"),
    mode: str = typer.Option("auto-fix", help="Operation mode: 'scan-only' or 'auto-fix'")
):
    """
    Start the Nexus-Guardian autonomous agent.
    """
    guardian = Guardian(target_path=path)
    if mode == "scan-only":
        guardian.scan()
    else:
        guardian.run()

if __name__ == "__main__":
    app()
