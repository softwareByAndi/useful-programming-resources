#!/usr/bin/env bash

# Change directory to be where the command is.
cd "$(cd "$(dirname "$0")" > /dev/null && pwd)"
if [[ $? != 0 ]]; then
  echo "ERROR: failed to cd into current directory"
  pwd
  read
  exit
fi
cd "tw_files"
if [[ $? != 0 ]]; then
  echo "ERROR: failed to cd into tw_files"
  pwd
  read
  exit
fi

OUTPUT_FILE_NAME="tw-compiled.css"

echo ""
echo "deleting $OUTPUT_FILE_NAME"
rm "../$OUTPUT_FILE_NAME"

echo ""
touch "../$OUTPUT_FILE_NAME"

echo "found the following files:"
for FILE in *; do 
echo "    $FILE"; 
cat $FILE >> "../$OUTPUT_FILE_NAME";
echo >> "../$OUTPUT_FILE_NAME";
echo >> "../$OUTPUT_FILE_NAME";
done;

echo ""
echo "file created: '$OUTPUT_FILE_NAME'";
echo "compilation complete"
echo ""

# read