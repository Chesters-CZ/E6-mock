#!/bin/bash

cd ./split_tags/

for file in tags*; do
  if [[ -f "$file" ]]; then
    uniq "$file" "$file""uniqed"
    mv "$file""uniqed" "$file"
    echo "Uniqed file: $file"
  fi
done

