#!/bin/sh
#set -e

# Check if a filename is provided as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <file_name>" >&2
  exit 1
fi

# Use the first command line argument as the file name
FILE_NAME=$1

git diff HEAD --unified=0 -- "$FILE_NAME" > diff.txt
#echo -------- diff.txt --------
#cat diff.txt
#echo -------- grep 1 start --------
grep -E '^[+-][^+-]' diff.txt > diff_filtered.txt
GREP_EXIT_CODE=$?
if [ $GREP_EXIT_CODE -eq 2 ]; then
  echo "An error occurred during grep." >&2
  exit 1
fi
#echo -------- grep 1 end --------
#echo -------- diff_filtered.txt --------
#cat diff_filtered.txt
#echo -------- grep 2 start --------
grep -v -E '^[+-]!\[image\]' diff_filtered.txt > diff_non_image.txt
GREP_EXIT_CODE=$?
if [ $GREP_EXIT_CODE -eq 2 ]; then
  echo "An error occurred during grep." >&2
  exit 1
fi
#echo -------- grep 2 end --------
#echo -------- diff_non_image.txt --------
#cat diff_non_image.txt
