#!/bin/bash

cd ./split_userids/

for file in uids*; do
  if [[ -f "$file" ]]; then
    uniq "$file" "$file""uniqed"
    mv "$file""uniqed" "$file"
    echo "Uniqed file: $file"
  fi
done

