import os
import re

def clean_content(content):
    # Wrap paragraph tags in brackets
    content = re.sub(r'##\s(P\d+)', r'[\1]', content)

    # Wrap inline tags in brackets (e.g., - #worldbuilding -> [worldbuilding])
    content = re.sub(r'-\s#(\w+)', r'[\1]', content)

    # Remove notes sections starting with - **Notes** : and the text below them until --- or ## P
    content = re.sub(r'-\s\*\*Notes\*\*.*?(?=\n---|\n## P|\Z)', '', content, flags=re.DOTALL)

    # Remove horizontal rules
    content = re.sub(r'^---$', '', content, flags=re.MULTILINE)

    # Remove excessive blank lines
    cleaned_content = "\n".join([line.strip() for line in content.splitlines() if line.strip()])
    return cleaned_content

def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith("_md.md"):  # Process only markdown files
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace("_md.md", "_cleaned.txt"))

            try:
                with open(input_file, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Clean the content
                cleaned_content = clean_content(content)

                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(cleaned_content)

                print(f"Processed: {filename} -> {os.path.basename(output_file)}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Paths
input_folder = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters"
output_folder = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters_cleaned"

# Process all files
process_files(input_folder, output_folder)
