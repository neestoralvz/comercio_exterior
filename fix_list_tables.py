import os
import re

def fix_list_table(content):
    # Pattern to match empty list-table directives
    pattern = r'(\.\. list-table::.+?)(?=\n\n|\Z)'
    
    def fix_table(match):
        table_def = match.group(1)
        if not re.search(r'\*\s+-', table_def, re.MULTILINE):
            # Add a minimal table structure if none exists
            fixed_table = table_def + '\n\n   * - Column 1\n     - Column 2\n     - Column 3'
            return fixed_table
        return table_def
    
    return re.sub(pattern, fix_table, content, flags=re.DOTALL)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if file contains list-table directives
        if '.. list-table::' in content:
            modified_content = fix_list_table(content)
            
            # Only write back if changes were made
            if modified_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"Fixed list-table in {file_path}")
            else:
                print(f"No changes needed in {file_path}")
                
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def main():
    docs_dir = 'source/docs'
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.rst'):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == '__main__':
    main() 