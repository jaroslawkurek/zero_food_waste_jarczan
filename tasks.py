from invoke import task


@task
def format(c):
    """Format code with Black."""
    c.run("black .")


@task
def lint(c):
    """Format code with Black."""
    c.run("pflake8 .")
