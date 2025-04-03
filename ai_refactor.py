import os
import openai
import subprocess

# Set your OpenAI API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Directory where Java files are stored
PROJECT_DIR = "C:\DHATHRI\GitHub Automation"

def get_java_files(directory):
    """Find all Java files in the project directory."""
    java_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files

def refactor_code(file_path):
    """Send Java code to AI for refactoring suggestions."""
    with open(file_path, "r") as f:
        code = f.read()
    
    # Use AI to improve the code
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that improves Java code for readability, best practices, and optimization."},
            {"role": "user", "content": f"Refactor the following Java code:\n{code}"}
        ]
    )

    # Extract AI-generated code
    improved_code = response["choices"][0]["message"]["content"]
    
    # Write back the improved code
    with open(file_path, "w") as f:
        f.write(improved_code)

def main():
    """Process all Java files and refactor them."""
    java_files = get_java_files(PROJECT_DIR)
    
    for java_file in java_files:
        print(f"Refactoring: {java_file}")
        refactor_code(java_file)
    
    # Commit and push the changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Automated AI code refactoring"])
    subprocess.run(["git", "push", "origin", "master"])

if __name__ == "__main__":
    main()
