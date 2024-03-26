#!/bin/bash

echo "Merging..."
sort -o user_ids_unique.csv ./split_userids/uids*

echo "Uniqing..."
uniq user_ids_unique.csv user_ids_unique_unique.csv
mv user_ids_unique_unique.csv user_ids_unique.csv

