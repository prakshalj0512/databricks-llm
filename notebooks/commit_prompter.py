import git
import requests

# Set up OpenAI API credentials
openai_api_key = ""

# Initialize the Git repository
repo = git.Repo()

# Get the latest commit diff
diff = repo.git.diff("HEAD")

# Make a request to the OpenAI API to generate a commit message
headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json"
}


def generate_git_commit():
    data = {
        "prompt": f"The following is a list of files in diff format.  Do your best to undersand the code changes for all changed files and write a simple one line git commit message that describes the behavior that changed.\n{diff}",
        "max_tokens": 2000,
        "temperature": 0.8
    }
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-003/completions", json=data, headers=headers)
    response.raise_for_status()
    commit_msg = response.json()["choices"][0]["text"]

    # Print the generated commit message
    print(f"Generated commit message: {commit_msg}")


def generate_code_report():
    data = {
        "prompt": f"You are a Python developer.  The following code is in diff format.  Examine the code, identify all logic errors, poor programming style, or security issues.  Produce a report that details the issues and provides possible resolutions.  Include resolution code samples if applicable.\n{diff}",
        "max_tokens": 2000,
        "temperature": 0.8
    }
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-003/completions", json=data, headers=headers)
    response.raise_for_status()
    code_analysis = response.json()["choices"][0]["text"]

    # Print the generated commit message
    print(f"Code Review: {code_analysis}")


def generate_pr():
    data = {
    "prompt": f"You are a Python developer and tech writer.  Use both of these skills to wite an engaging and descriptive Pull Request to explain every detail of your changes so that a human can review text and completely understand what the code is doing. You can use bullet points to help with readability, but make sure you make the PR super interesting and funny.\n{diff}",
    "max_tokens": 2000,
    "temperature": 0.8
    }
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-003/completions", json=data, headers=headers)
    response.raise_for_status()
    pull_request = response.json()["choices"][0]["text"]

    # Print the generated commit message
    print(f"Code Review: {pull_request}")


def whisper():
    generate_code_report()
    user_approval = input("Do still want to commit this code with the identified issues?")

    if user_approval.lower() == "y" or user_approval.lower() == "yes":
        generate_git_commit()
        user_approval = input("Does the commit message look good? (y/n): ")

        if user_approval.lower() == "y" or user_approval.lower() == "yes":
            # repo.index.commit(commit_msg)
            print("Changes committed successfully.")

            generate_pr()
            user_approval = input("Do still want to commit this code with the identified issues?")

            if user_approval.lower() == "y" or user_approval.lower() == "yes":
                print("PR submitted and team notified.")
        else:
            print("Changes not committed.")
    else:
        pass


if __name__ == "__main__":
    whisper()