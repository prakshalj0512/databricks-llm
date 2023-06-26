import git
import requests

# Set up OpenAI API credentials
openai_api_key = "YOUR_OPENAI_API_KEY"

# Initialize the Git repository
repo = git.Repo()

# Get the latest commit diff
diff = repo.git.diff("HEAD")
print(diff)

# Make a request to the OpenAI API to generate a commit message
headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json"
}
data = {
    "prompt": diff,
    "max_tokens": 20,
    "temperature": 0.8
}
# response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", json=data, headers=headers)
# response.raise_for_status()
# commit_msg = response.json()["choices"][0]["text"]

commit_msg = 'test'

# Print the generated commit message
print(f"Generated commit message: {commit_msg}")

# Prompt the user for approval
user_approval = input("Does the commit message look good? (y/n): ")

if user_approval.lower() == "y" or user_approval.lower() == "yes":
    # Commit the changes
    repo.index.commit(commit_msg)
    print("Changes committed successfully.")
else:
    print("Changes not committed.")
