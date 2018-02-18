# Runs a series of commands against a file, passed as the first parameter

if [ -z "$1" ]
  then
    echo "ERROR: No file provided. Exiting..."
    exit 1
fi

#1 Copy the file
sh copy.sh $1
#2 Deidentify the file
sh deidentify.sh $1
#3 Tag the file
sh tag.sh $1