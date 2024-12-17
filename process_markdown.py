import os
import re

def process_markdown(folder_path):
    """Process markdown files in the specified folder and extract data."""
    story_data = []

    # Loop through all markdown files in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".md"):  # Only process markdown files
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                content = f.read()

                # Extract chapter headings
                chapters = re.findall(r"^# (.+)", content, re.MULTILINE)
                
                # Extract subheadings (scenes)
                scenes = re.findall(r"^## (.+)", content, re.MULTILINE)
                
                # Extract tagged paragraphs
                paragraphs = re.findall(r"\[(P\d+)\]: (.+)", content)
                
                # Extract tags
                tags = re.findall(r"\[Tags\]: (.+)", content)

                # Store the extracted data
                story_data.append({
                    "file": file,
                    "chapters": chapters,
                    "scenes": scenes,
                    "paragraphs": paragraphs,
                    "tags": tags
                })

    return story_data

# Define your markdown folder
markdown_folder = "C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Storys\The Veil and the Machine\markdown\chapters_md"

# Process the markdown files
data = process_markdown(markdown_folder)

# Output the results
for item in data:
    print(f"File: {item['file']}")
    print(f"Chapters: {item['chapters']}")
    print(f"Scenes: {item['scenes']}")
    print(f"Paragraphs: {item['paragraphs']}")
    print(f"Tags: {item['tags']}")
    print("===")
