import os
import re

def remove_notes_sections(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove notes sections starting with - **Notes** : and ending with --- or ## P
    content = re.sub(r'-\s\*\*Notes\*\*.*?(?=\n---|\n## P|\Z)', '', content, flags=re.DOTALL)

    # Remove standalone markdown-style notes header variations
    content = re.sub(r'-\s\*\*Notes:\*\*\s*', '', content)

    # Remove excessive blank lines
    cleaned_content = "\n".join([line.strip() for line in content.splitlines() if line.strip()])

    # Write the cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

def process_all_chapters(input_folder, output_folder):
    """
    Processes all .md files in the input folder, removes notes, and saves them to the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith("_md.md"):  # Filter for your chapter file naming convention
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace("_md.md", "_cleaned.txt"))
            
            # Remove notes from the file
            remove_notes_sections(input_file, output_file)
            
            print(f"Processed: {filename} -> {os.path.basename(output_file)}")

# Folder paths
input_folder = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters"
output_folder = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters_cleaned"

# Execute the processing for all chapters
process_all_chapters(input_folder, output_folder)
