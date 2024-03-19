from invoke import task


@task
def style(context, hide=False, path="."):
    context.run(f"black {path}", hide=hide)
    context.run(f"isort {path}", hide=hide)


@task
def flake8(context, hide=False, path="."):
    context.run(f"pflake8 {path}", hide=hide)


@task
def pylint(context, hide=False, path="."):
    context.run(f"pylint {path}", hide=hide)


@task(aliases=["pr"])
def pull_request(context):
    green = "\033[32m"
    white = "\033[37m"

    print("```")
    style(context, hide=True)
    print(f"{green}Style: Done")

    print("```")
    flake8(context, hide=True)
    print(f"Linting with Flake8: Done{white}")

    print("```")
    pylint(context, hide=True)
    print(f"Linting with Pylint: Done{white}")
    print("```")
