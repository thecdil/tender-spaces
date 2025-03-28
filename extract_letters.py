import re
import os
import csv
import sys

def extract_letters_to_csv(markdown_file_path, output_dir="_data/letters/"):
    """Extract letters from markdown file and save them to individual CSV files."""
    # Read the markdown file
    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Split the content by headers starting with ## gae
    # This pattern matches: ## gaeXXX followed by content until the next ## gae or end of file
    pattern = r'## (gae\d+)\s*\n\n(.*?)(?=\n\n## gae|\Z)'
    letters = re.findall(pattern, content, re.DOTALL)
    
    letter_count = 0
    
    for letter_id, letter_content in letters:
        # Clean up the content - remove extra spaces and normalize line breaks
        cleaned_content = letter_content.strip()
        
        # Create the output CSV file path
        output_file = os.path.join(output_dir, f"{letter_id}.csv")
        
        # Write to individual CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['text'])  # Header row
            writer.writerow([cleaned_content])
        
        letter_count += 1
        print(f"Created {output_file}")
    
    print(f"Extracted {letter_count} letters to individual files in {output_dir}")
    return letter_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        markdown_file_path = sys.argv[1]
    else:
        markdown_file_path = "Letter Transcripts (1).md"
    
    output_dir = "_data/letters/"
    num_letters = extract_letters_to_csv(markdown_file_path, output_dir)