import os
import sys

def add_frontmatter_to_files(directory_path):
    """Add front matter (---\n---) to the top of each markdown file in the directory."""
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return
    
    # Get all markdown files in the directory
    files = [f for f in os.listdir(directory_path) if f.endswith('.md')]
    
    if not files:
        print(f"No markdown files found in '{directory_path}'.")
        return
    
    # Process each file
    for filename in files:
        file_path = os.path.join(directory_path, filename)
        
        # Read the current content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Add front matter if it doesn't already exist
        if not content.startswith('---\n'):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('---\n---\n\n' + content)
            print(f"Added front matter to {filename}")
        else:
            print(f"Front matter already exists in {filename}")

if __name__ == "__main__":
    directory = "objects/letters/"
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    
    add_frontmatter_to_files(directory)
    print("Done!")