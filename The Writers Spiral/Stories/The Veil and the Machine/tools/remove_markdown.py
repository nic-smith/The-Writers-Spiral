import re

def remove_markdown_and_save(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Markdown headers and subheaders
    content = re.sub(r'^#.*$', '', content, flags=re.MULTILINE)
    
    # Remove tags or metadata lists (lines starting with '- ' or '* ')
    content = re.sub(r'^\s*[-*]\s+.*$', '', content, flags=re.MULTILINE)
    
    # Remove notes or markdown-specific annotations
    content = re.sub(r'-\s\*\*Notes\*\*:.*$', '', content, flags=re.MULTILINE)
    
    # Remove horizontal rules
    content = re.sub(r'^---$', '', content, flags=re.MULTILINE)
    
    # Strip leading/trailing whitespace and join lines
    cleaned_content = "\n".join([line.strip() for line in content.splitlines() if line.strip()])
    
    # Write the cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

# Paths to your files
input_file = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters\prologue_md.md"
output_file = r"C:\Users\smith\OneDrive\Documents\GitHub\The-Writers-Spiral\The Writers Spiral\Stories\The Veil and the Machine\chapters\prologue_cleaned.txt"

# Execute the cleaning process
remove_markdown_and_save(input_file, output_file)

print(f"Markdown removed. Cleaned text saved to: {output_file}")
