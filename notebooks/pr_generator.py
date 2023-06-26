import git
from github import Github
import yaml


def generate_github_pr(pr_title, pr_body):
    # GitHub access token
    # Load the GitHub access token from the YAML file
    with open("conf/config.yaml", "r") as file:
        config = yaml.safe_load(file)
    access_token = config["github"]["access_token"]

    # Initialize the Git repository
    repo = git.Repo()

    # Get the current branch
    current_branch = repo.active_branch

    # Get the diff between the current branch and main
    diff = repo.git.diff('main', current_branch)

    # Print the diff
    print(diff)

    # Create a new GitHub instance
    github = Github(access_token)

    # Get the repository
    repo_name = "prakshalj0512/databricks-llm"
    repository = github.get_repo(repo_name)

    # Specify the base branch and head branch for the pull request
    base_branch = "main"
    head_branch = current_branch.name

    # Push code to origin
    repo.remote("origin").push(f"refs/heads/{head_branch}")

    # Create the pull request
    pull_request = repository.create_pull(title=pr_title, body=pr_body, base=base_branch, head=head_branch)

    # Print the pull request number
    print("Pull Request Created - Number:", pull_request.number)
