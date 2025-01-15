#!/usr/bin/env python3

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_labels(content):
    """Extract all labels from RST content."""
    label_pattern = r'^\s*\.\.\s+_([^:]+):\s*$'
    return re.findall(label_pattern, content, re.MULTILINE)

def extract_references(content):
    """Extract all cross-references from RST content."""
    ref_pattern = r':ref:`([^`]+)`'
    return re.findall(ref_pattern, content)

def fix_duplicate_labels(content, file_path, label_locations):
    """Fix duplicate labels by making them unique."""
    # Get the file's directory name to use as a prefix
    dir_name = os.path.basename(os.path.dirname(file_path))
    
    def replace_label(match):
        label = match.group(1)
        # If this label appears in multiple files
        if len(label_locations[label]) > 1:
            # Create a unique label by prefixing with directory name
            new_label = f"{dir_name}_{label}"
            return f".. _{new_label}:"
        return match.group(0)
    
    # Fix label definitions
    label_pattern = r'^\s*\.\.\s+_([^:]+):\s*$'
    content = re.sub(label_pattern, replace_label, content, flags=re.MULTILINE)
    
    def replace_ref(match):
        ref = match.group(1)
        # If this reference points to a label that appears in multiple files
        if len(label_locations[ref]) > 1:
            # Update the reference to use the prefixed label
            new_ref = f"{dir_name}_{ref}"
            return f":ref:`{new_ref}`"
        return match.group(0)
    
    # Fix references to labels
    ref_pattern = r':ref:`([^`]+)`'
    content = re.sub(ref_pattern, replace_ref, content)
    
    return content

def fix_missing_references(content, available_labels):
    """Fix missing references by suggesting alternatives or removing them."""
    def replace_ref(match):
        ref = match.group(1)
        if ref not in available_labels:
            # Try to find a similar label
            similar_labels = [l for l in available_labels if l.lower() == ref.lower()]
            if similar_labels:
                # Use the first similar label found
                return f":ref:`{similar_labels[0]}`"
            # If no similar label found, comment out the reference
            return f"``{ref}``"  # Replace with literal text
        return match.group(0)
    
    ref_pattern = r':ref:`([^`]+)`'
    return re.sub(ref_pattern, replace_ref, content)

def process_file(file_path, label_locations, all_labels):
    """Process a single RST file to fix cross-reference issues."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix duplicate labels
        fixed_content = fix_duplicate_labels(content, file_path, label_locations)
        
        # Fix missing references
        fixed_content = fix_missing_references(fixed_content, all_labels)
        
        # Only write back if changes were made
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed reference issues in {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def main():
    """Main function to process all RST files in the docs directory."""
    docs_dir = Path('source/docs')
    
    # First pass: collect all labels and their locations
    label_locations = defaultdict(list)
    all_labels = set()
    
    for rst_file in docs_dir.rglob('*.rst'):
        try:
            with open(rst_file, 'r', encoding='utf-8') as f:
                content = f.read()
            labels = extract_labels(content)
            for label in labels:
                label_locations[label].append(rst_file)
                all_labels.add(label)
        except Exception as e:
            print(f"Error reading {rst_file}: {str(e)}")
    
    # Second pass: fix cross-reference issues
    for rst_file in docs_dir.rglob('*.rst'):
        process_file(rst_file, label_locations, all_labels)

if __name__ == '__main__':
    main() 