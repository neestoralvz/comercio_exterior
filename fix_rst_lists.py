#!/usr/bin/env python3

import re
import os
from pathlib import Path

def fix_list_formatting(content):
    """Fix RST list formatting issues."""
    lines = content.splitlines()
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        
        # Skip empty lines
        if not stripped:
            new_lines.append(line)
            i += 1
            continue
            
        # Check for main list items with bold text
        if re.match(r'^\* \*\*.*\*\*:?$', stripped):
            new_lines.append(line)
            
            # If next line exists and is a sublist item
            if i + 1 < len(lines) and re.match(r'^\s*[-*]\s+\S', lines[i + 1].rstrip()):
                # Add blank line if not already present
                if not (i + 1 < len(lines) and not lines[i + 1].strip()):
                    new_lines.append('')
                    
        # Check for sublist items
        elif re.match(r'^\s*[-*]\s+\S', stripped):
            # Ensure proper indentation (2 spaces for sublists)
            indent_level = len(re.match(r'^\s*', stripped).group())
            if indent_level == 0:
                line = '  ' + stripped
            new_lines.append(line)
            
            # If next line is also a sublist item, no blank line needed
            if i + 1 < len(lines) and re.match(r'^\s*[-*]\s+\S', lines[i + 1].rstrip()):
                pass
            # If next line is a different type of content, add blank line
            elif i + 1 < len(lines) and lines[i + 1].strip():
                new_lines.append('')
                
        # Check for numbered list items
        elif re.match(r'^\d+\.\s+\S', stripped):
            new_lines.append(line)
            
            # If next line is a sublist item
            if i + 1 < len(lines) and re.match(r'^\s*[-*]\s+\S', lines[i + 1].rstrip()):
                if not (i + 1 < len(lines) and not lines[i + 1].strip()):
                    new_lines.append('')
                    
        # Definition lists
        elif re.match(r'^[A-Za-z].*$', stripped) and i + 1 < len(lines):
            next_line = lines[i + 1].rstrip()
            if next_line.startswith('    '):
                new_lines.append(line)
                new_lines.append(next_line)
                if i + 2 < len(lines) and re.match(r'^\s*[-*]\d+\.]\s+\S', lines[i + 2].rstrip()):
                    new_lines.append('')
                i += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
            
        i += 1
    
    return '\n'.join(new_lines)

def process_rst_files(directory):
    """Process all RST files in the given directory."""
    directory = Path(directory)
    for rst_file in directory.rglob('*.rst'):
        print(f"Processing {rst_file}...")
        
        # Read content
        with open(rst_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix formatting
        fixed_content = fix_list_formatting(content)
        
        # Write back if changed
        if fixed_content != content:
            print(f"Fixing list formatting in {rst_file}")
            with open(rst_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
        else:
            print(f"No changes needed in {rst_file}")

if __name__ == '__main__':
    # Process RST files in the source/docs directory
    process_rst_files('source/docs') 