#!/usr/bin/env python3

import os
import re
from pathlib import Path
from collections import defaultdict

class RSTFixer:
    def __init__(self):
        self.label_locations = defaultdict(list)
        self.all_labels = set()
        
    def fix_list_formatting(self, content):
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
                
            # Check for list items with bold text or normal text
            if re.match(r'^\* (?:\*\*.*\*\*:?|[^*].*)$', stripped):
                new_lines.append(line)
                
                # Add blank line before next list item if needed
                if i + 1 < len(lines) and re.match(r'^\s*[-*]\s+\S', lines[i + 1].rstrip()):
                    if not (i + 1 < len(lines) and not lines[i + 1].strip()):
                        new_lines.append('')
                        
            # Check for sublist items
            elif re.match(r'^\s*[-*]\s+\S', stripped):
                # Ensure proper indentation (2 spaces for sublists)
                indent_level = len(re.match(r'^\s*', stripped).group())
                if indent_level == 0:
                    line = '  ' + stripped
                new_lines.append(line)
                
                # Handle spacing between list items
                if i + 1 < len(lines):
                    next_line = lines[i + 1].rstrip()
                    if not re.match(r'^\s*[-*]\s+\S', next_line) and next_line:
                        new_lines.append('')
                    
            # Check for numbered list items
            elif re.match(r'^\d+\.\s+\S', stripped):
                new_lines.append(line)
                
                # Add blank line before next list item if needed
                if i + 1 < len(lines) and re.match(r'^\s*[-*]\s+\S', lines[i + 1].rstrip()):
                    if not (i + 1 < len(lines) and not lines[i + 1].strip()):
                        new_lines.append('')
                        
            # Definition lists
            elif re.match(r'^[A-Za-z].*$', stripped) and i + 1 < len(lines):
                next_line = lines[i + 1].rstrip()
                if next_line.startswith('    '):
                    new_lines.append(line)
                    new_lines.append(next_line)
                    if i + 2 < len(lines) and re.match(r'^\s*[-*\d+\.]\s+\S', lines[i + 2].rstrip()):
                        new_lines.append('')
                    i += 1
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
                
            i += 1
        
        return '\n'.join(new_lines)

    def fix_list_table(self, content):
        """Fix list-table formatting issues."""
        pattern = r'(\.\. list-table::.+?)(?=\n\n|\Z)'
        
        def fix_table_structure(table_match):
            lines = table_match.group(1).split('\n')
            directive_line = lines[0]
            
            # Extract header rows and widths
            header_rows = 1
            widths = []
            for line in lines[1:]:
                if ':header-rows:' in line:
                    header_rows = int(line.split(':')[-1].strip())
                elif ':widths:' in line:
                    widths = [int(w) for w in line.split(':')[-1].strip().split()]
            
            # Find the first row to determine column count
            first_row = None
            for line in lines:
                if line.strip().startswith('* -'):
                    first_row = line
                    break
                    
            if not first_row:
                return table_match.group(1)
                
            # Count columns in first row
            column_count = len(first_row.split('- ')) - 1
            
            # Rebuild table with consistent columns
            new_lines = [directive_line]
            if header_rows:
                new_lines.append('   :header-rows: {}'.format(header_rows))
            if widths:
                new_widths = widths[:column_count] if len(widths) > column_count else widths + [100//column_count] * (column_count - len(widths))
                new_lines.append('   :widths: {}'.format(' '.join(map(str, new_widths))))
            new_lines.append('')
            
            # Process rows
            current_row = []
            for line in lines:
                line = line.rstrip()
                if line.strip().startswith('* -'):
                    if current_row:
                        # Pad previous row if needed
                        while len(current_row) < column_count:
                            current_row.append('')
                        new_lines.append('   * - ' + '\n     - '.join(current_row))
                    current_row = [line.split('- ', 1)[1].strip()]
                elif line.strip().startswith('- '):
                    current_row.append(line.split('- ', 1)[1].strip())
                    
            # Add final row
            if current_row:
                while len(current_row) < column_count:
                    current_row.append('')
                new_lines.append('   * - ' + '\n     - '.join(current_row))
                
            return '\n'.join(new_lines)
        
        return re.sub(pattern, fix_table_structure, content, flags=re.DOTALL)

    def fix_cross_references(self, content, file_path):
        """Fix cross-reference issues."""
        dir_name = os.path.basename(os.path.dirname(file_path))
        
        def make_unique_label(label):
            return f"{dir_name}_{label}"
        
        # Fix label definitions
        pattern = r'(^\s*\.\.\s+_)([^:]+)(:\s*$)'
        def replace_label(match):
            label = match.group(2)
            if len(self.label_locations[label]) > 1:
                return f"{match.group(1)}{make_unique_label(label)}{match.group(3)}"
            return match.group(0)
        
        content = re.sub(pattern, replace_label, content, flags=re.MULTILINE)
        
        # Fix references to labels
        pattern = r':ref:`([^`]+)`'
        def replace_ref(match):
            label = match.group(1)
            if label not in self.all_labels:
                # Try to find similar labels
                similar_labels = [l for l in self.all_labels if label.lower() in l.lower()]
                if similar_labels:
                    return f":ref:`{similar_labels[0]}`  .. Original reference was: {label}"
                return f"``{label}``  .. TODO: Reference not found"
            if len(self.label_locations[label]) > 1:
                return f':ref:`{make_unique_label(label)}`'
            return match.group(0)
        
        return re.sub(pattern, replace_ref, content)

    def collect_labels(self, docs_dir):
        """Collect all labels and their locations from RST files."""
        label_pattern = r'^\s*\.\.\s+_([^:]+):\s*$'
        
        for rst_file in docs_dir.rglob('*.rst'):
            try:
                with open(rst_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                labels = re.findall(label_pattern, content, re.MULTILINE)
                for label in labels:
                    self.label_locations[label].append(rst_file)
                    self.all_labels.add(label)
            except Exception as e:
                print(f"Error reading {rst_file}: {str(e)}")

    def process_file(self, file_path):
        """Process a single RST file to fix all formatting issues."""
        print(f"Processing {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply all fixes
            modified_content = content
            modified_content = self.fix_list_formatting(modified_content)
            modified_content = self.fix_list_table(modified_content)
            modified_content = self.fix_cross_references(modified_content, file_path)
            
            # Only write back if changes were made
            if modified_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"Fixed formatting in {file_path}")
            else:
                print(f"No changes needed in {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    def process_all_files(self, docs_dir):
        """Process all RST files in the docs directory."""
        # First collect all labels
        self.collect_labels(docs_dir)
        
        # Then process all files
        for rst_file in docs_dir.rglob('*.rst'):
            self.process_file(rst_file)

def main():
    """Main function to fix RST formatting issues."""
    docs_dir = Path('source/docs')
    fixer = RSTFixer()
    fixer.process_all_files(docs_dir)

if __name__ == '__main__':
    main() 