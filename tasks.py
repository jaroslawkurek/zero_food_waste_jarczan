from invoke import task


@task
def format(c):
    """Format code with Black."""
    c.run("black .")


@task
def pylint(c):
    """Lint code with Pylint ."""
    c.run("pylint .")


@task
def flake8(c):
    """Lint code with Flake8."""
    c.run("pflake8 .")


@task
def lint(c):
    """Lint code with Flake8 and Pylint."""
    c.run("pflake8 .")
    c.run("pylint .")
