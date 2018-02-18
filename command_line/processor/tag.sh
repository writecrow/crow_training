# Prepend the filename as a tag into the file
echo "Tagging file..."
echo "<Filename : $1>" > output/tempfile
cat output/$1 >> output/tempfile
mv output/tempfile output/$1