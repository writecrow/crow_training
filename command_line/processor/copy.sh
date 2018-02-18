# Create the directory "output" and write a file there, from argument.
mkdir output
echo "Copying $1 to 'output' directory..."
cp $1 output/$1