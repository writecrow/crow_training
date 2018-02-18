echo "Performing deidentification..."
while read -r var
do
  var=${var//Lawrence/<NAME>}
  var=${var//Reggie/<NAME>}
  var=${var//Lefferts/<NAME>}
  echo ${var//Chivers/<NAME>}
done < "output/$1" >> output/tempfile
mv output/tempfile output/$1
