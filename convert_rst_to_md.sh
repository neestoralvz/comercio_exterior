#!/usr/bin/env bash

# Find all .rst files in dev directory and convert them to .md
find ./dev -name "*.rst" | while read file; do
    # Define output filename (replace .rst with .md)
    output="${file%.rst}.md"
    
    echo "Converting: $file -> $output"
    if pandoc -f rst -t gfm "$file" -o "$output"; then
        echo "Deleting: $file"
        rm "$file"
    else
        echo "Error converting $file - skipping deletion"
    fi
done

echo "Conversion and cleanup complete!" 