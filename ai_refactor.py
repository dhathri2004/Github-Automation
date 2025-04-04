import os
import subprocess
from datetime import datetime
from openai import OpenAI  # ✅ Import the OpenAI client properly

# Set your OpenAI API key
client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  # ✅ Initialize OpenAI client correctly

# Directory where Java files are stored
PROJECT_DIR = r"C:\DHATHRI\GitHub Automation"

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
    
    # Use OpenAI API to refactor the code
    response = client.chat.completions.create(  
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that improves Java code for readability, best practices, and optimization."},
            {"role": "user", "content": f"Refactor the following Java code:\n{code}"}
        ]
    )

    # Extract AI-generated code
    improved_code = response.choices[0].message.content  # ✅ Fix response parsing
    
    # Write back the improved code
    with open(file_path, "w") as f:
        f.write(improved_code)

def create_branch():
    """Create a new branch dynamically."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    branch_name = f"refactor_{timestamp}"  # Example: refactor_20250403_1430

    # Create and switch to the new branch
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    return branch_name

def main():
    """Process all Java files, refactor them, and push changes to a new branch."""
    java_files = get_java_files(PROJECT_DIR)
    
    for java_file in java_files:
        print(f"Refactoring: {java_file}")
        refactor_code(java_file)
    
    # Create a new branch before committing
    new_branch = create_branch()

    # Commit and push the changes
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Automated AI code refactoring"], check=True)
    subprocess.run(["git", "push", "origin", new_branch], check=True)

    print(f"Changes pushed to new branch: {new_branch}")

if __name__ == "__main__":
    main()
