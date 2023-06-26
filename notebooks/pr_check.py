import git

def get_diff_file_from_pr(repository_url, pr_number):
    # Clone the repository locally
    repo = git.Repo.clone_from(repository_url, '<local_directory>')  # Replace '<local_directory>' with your desired local directory

    # Fetch the PR branch
    pr_branch = f'pull/{pr_number}/head'
    repo.git.fetch('origin', pr_branch)

    # Get the diff file
    diff_file = repo.git.diff('origin/main', pr_branch)

    # Save the diff file to a local file
    with open('<output_file_path>', 'w') as file:  # Replace '<output_file_path>' with the desired output file path
        file.write(diff_file)

    print(f"Diff file saved to '{<output_file_path>}'.")

# Example usage
repository_url = 'https://github.com/prakshalj0512/databricks-llm'
pr_number = <pr_number>
get_diff_file_from_pr(repository_url, pr_number)
