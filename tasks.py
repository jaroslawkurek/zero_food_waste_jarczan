from invoke import task


@task
def pr(c):
    """Format code with Black."""
    c.run("black .")
