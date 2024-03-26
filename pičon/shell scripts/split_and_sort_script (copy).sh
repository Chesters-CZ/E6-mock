#!/bin/bash

split -a 3 -d -u -l 1000000 user_ids.csv uids_split_

mv uids_split_* ./split_userids/
echo "Files have been split"

cd ./split_userids/
echo "Files have been moved"

for file in uids*; do
  if [[ -f "$file" ]]; then
    sort "$file" -o "$file"
    echo "Sorted file: $file"
  fi
done

