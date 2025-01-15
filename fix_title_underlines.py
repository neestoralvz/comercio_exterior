#!/usr/bin/env python3

import re
import os
from pathlib import Path

def fix_title_underlines(rst_content):
    """
    Fix RST title underlines to match the length of their titles.
    """
    lines = rst_content.splitlines()
    fixed_lines = []
    
    # Pattern to detect title underlines
    underline_pattern = re.compile(r'^[=\-~]+$')
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        fixed_lines.append(line)
        
        # Check if next line exists and is a title underline
        if i + 1 < len(lines):
            next_line = lines[i + 1].rstrip()
            if underline_pattern.match(next_line):
                # Get the character used for underlining
                char_used = next_line[0]
                # Generate new underline of the same length as the title
                new_underline = char_used * len(line)
                fixed_lines.append(new_underline)
                i += 2
                continue
        
        i += 1
    
    return '\n'.join(fixed_lines)

def process_rst_files(directory):
    """
    Process all RST files in the given directory recursively.
    """
    docs_dir = Path(directory)
    for rst_file in docs_dir.rglob('*.rst'):
        print(f"Processing {rst_file}...")
        try:
            # Read file content
            content = rst_file.read_text(encoding='utf-8')
            # Fix title underlines
            fixed_content = fix_title_underlines(content)
            # Write back to file
            rst_file.write_text(fixed_content, encoding='utf-8')
            print(f"✓ Fixed {rst_file}")
        except Exception as e:
            print(f"Error processing {rst_file}: {e}")

if __name__ == '__main__':
    # Process all RST files in the source directory
    process_rst_files('source') 