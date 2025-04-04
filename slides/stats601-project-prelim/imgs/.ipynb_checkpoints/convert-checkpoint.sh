#!/bin/sh

for file in *.eps; do
    inkscape --export-filename="${file%.*}.svg" "$file"
done
