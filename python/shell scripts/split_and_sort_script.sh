#!/bin/bash

split -a 3 -d -u -l 1000000 tags.csv tags_split_

mv tags_split_* ./split_tags/
echo "Files have been split"

cd ./split_tags/
echo "Files have been moved"

for file in tags*; do
  if [[ -f "$file" ]]; then
    sort "$file" -o "$file"
    echo "Sorted file: $file"
  fi
done

