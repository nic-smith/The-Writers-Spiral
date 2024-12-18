import re

def remove_markdown_and_embedded_notes(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Markdown headers and subheaders
    content = re.sub(r'^#.*$', '', content, flags=re.MULTILINE)
    
    # Remove bullet lists, tags, and metadata
    content = re.sub(r'^\s*[-*]\s+.*$', '', content, flags=re.MULTILINE)
    
    # Identify and remove standalone "notes" lines, even if unmarked
    content = re.sub(r'\bEstablishes\b.*?\.|\bGriffin\'s\b.*?\.|\bSari\'s\b.*?\.', '', content, flags=re.IGNORECASE)

    # Remove horizontal rules
    content = re.sub(r'^---$', '', content, flags=re.MULTILINE)
    
    # Clean up excessive whitespace and empty lines
    cleaned_content = "\n".join([line.strip() for line in content.splitlines() if line.strip()])

    # Write cleaned content to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

# Example usage
input_file = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters\chapter_6_md.md"
output_file = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters\chapter_6_cleaned.txt"

remove_markdown_and_embedded_notes(input_file, output_file)

print(f"Markdown and embedded notes removed. Cleaned text saved to: {output_file}")
