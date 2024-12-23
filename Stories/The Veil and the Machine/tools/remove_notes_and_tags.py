import os
import re

def clean_markdown(content):
    """
    Cleans the markdown content by removing Tags and Notes sections,
    preserving only the paragraph numbers and content.
    """
    # Remove Tags sections
    content = re.sub(r'-\s\*\*Tags\*\*:.*?(?=\n- \*\*Content\*\*|\n##|\Z)', '', content, flags=re.DOTALL)

    # Remove Notes sections
    content = re.sub(r'-\s\*\*Notes\*\*:.*?(?=\n##|\Z)', '', content, flags=re.DOTALL)

    # Preserve paragraph numbers and content
    content = re.sub(r'##\s(P\d+)', r'[\1]', content)  # Convert ## P# to [P#]
    content = re.sub(r'-\s\*\*Content\*\*:\s*', '', content)  # Remove "Content" label

    # Remove horizontal rules and extra blank lines
    content = re.sub(r'^---$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n{2,}', '\n', content)

    # Strip leading/trailing whitespace
    cleaned_content = "\n".join(line.strip() for line in content.splitlines() if line.strip())

    return cleaned_content

def process_files(input_folder, output_folder):
    """
    Cleans all markdown files in the input folder and saves them in the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".md"):  # Process only markdown files
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace("_md.md", ".txt"))

            try:
                # Read the input file
                with open(input_file, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Clean the content
                cleaned_content = clean_markdown(content)

                # Write the cleaned content to the output file
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(cleaned_content)

                print(f"Processed: {filename} -> {os.path.basename(output_file)}")
            except FileNotFoundError:
                print(f"File not found: {input_file}")
            except PermissionError:
                print(f"Permission denied: {input_file} or {output_file}")
            except Exception as e:
                print(f"An unexpected error occurred while processing {filename}: {e}")

# Define input and output folder paths
input_folder = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\Stories\The Veil and the Machine\chapters"
output_folder = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\Stories\The Veil and the Machine\chapters\cleaned_chapters"

# Process all markdown files in the input folder
process_files(input_folder, output_folder)
