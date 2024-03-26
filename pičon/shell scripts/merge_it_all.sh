#!/bin/bash

echo "Merging..."
sort -o tags_unique.csv ./split_tags/tags_split_*

echo "Uniqing..."
uniq tags_unique.csv tags_unique_unique.csv
mv tags_unique_unique.csv tags_unique.csv

