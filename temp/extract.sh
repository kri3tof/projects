# Extract zip files
for zipfile in *.zip; do
  zipdir=$(echo $zipfile | cut -d. -f1)
  mkdir $zipdir
  unzip "$zipfile" -d $zipdir
  if [ "$?" -eq 0 ]
  then
    rm -f $zipfile
  fi
done

# Extract lha files
for lhafile in *.lha; do
  lhadir=$(echo $lhafile | cut -d. -f1)
  mkdir $lhadir
  lha -xw=$lhadir $lhafile
  if [ "$?" -eq 0 ]
  then
    rm -f $lhafile
  fi
done
