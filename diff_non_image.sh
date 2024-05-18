#!/bin/sh
set -e

# Check if a filename is provided as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <file_name>"
  exit 1
fi

# Use the first command line argument as the file name
FILE_NAME=$1

git diff HEAD --unified=0 -- "$FILE_NAME" > diff.txt
echo -------- diff.txt --------
cat diff.txt
grep -E '^[+-][^+-]' diff.txt > diff_filtered.txt
echo -------- diff_filtered.txt --------
cat diff_filtered.txt
grep -v -E '^[+-]!\[image\]' diff_filtered.txt > diff_non_image.txt
echo -------- diff_non_image.txt --------
cat diff_non_image.txt
