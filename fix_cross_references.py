import os
import re
from collections import defaultdict

def extract_labels(content):
    """Extract all labels from RST content."""
    pattern = r'^\s*\.\.\s+_([^:]+):\s*$'
    return set(re.findall(pattern, content, re.MULTILINE))

def extract_references(content):
    """Extract all cross-references from RST content."""
    pattern = r':ref:`([^`]+)`'
    return set(re.findall(pattern, content))

def fix_duplicate_labels(content, file_path, label_locations):
    """Fix duplicate labels by making them unique."""
    dir_name = os.path.basename(os.path.dirname(file_path))
    
    def make_unique_label(label):
        return f"{dir_name}_{label}"
    
    # Fix label definitions
    pattern = r'(^\s*\.\.\s+_)([^:]+)(:\s*$)'
    def replace_label(match):
        label = match.group(2)
        if len(label_locations[label]) > 1:
            return f"{match.group(1)}{make_unique_label(label)}{match.group(3)}"
        return match.group(0)
    
    content = re.sub(pattern, replace_label, content, flags=re.MULTILINE)
    
    # Fix references to labels
    pattern = r':ref:`([^`]+)`'
    def replace_ref(match):
        label = match.group(1)
        if len(label_locations[label]) > 1:
            return f':ref:`{make_unique_label(label)}`'
        return match.group(0)
    
    return re.sub(pattern, replace_ref, content)

def fix_missing_references(content, available_labels):
    """Fix missing references by suggesting alternatives or commenting them out."""
    def find_closest_match(ref, labels):
        # Simple string similarity - could be improved
        return min(labels, key=lambda x: abs(len(x) - len(ref)))
    
    pattern = r':ref:`([^`]+)`'
    def replace_ref(match):
        ref = match.group(1)
        if ref not in available_labels:
            closest = find_closest_match(ref, available_labels)
            return f'.. TODO: Reference "{ref}" not found. Suggested: ":ref:`{closest}`"'
        return match.group(0)
    
    return re.sub(pattern, replace_ref, content)

def process_file(file_path, label_locations, all_labels):
    """Process a single RST file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix duplicate labels
        content = fix_duplicate_labels(content, file_path, label_locations)
        
        # Fix missing references
        content = fix_missing_references(content, all_labels)
        
        # Only write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed references in {file_path}")
        else:
            print(f"No changes needed in {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def main():
    docs_dir = 'source/docs'
    label_locations = defaultdict(list)
    all_labels = set()
    
    # First pass: collect all labels and their locations
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                labels = extract_labels(content)
                for label in labels:
                    label_locations[label].append(file_path)
                    all_labels.add(label)
    
    # Second pass: fix references
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                process_file(file_path, label_locations, all_labels)

if __name__ == '__main__':
    main() 