# Download all files and remove unnecessary
python download.py
find -type f -name "*_CD*.*" -exec rm -f {} \;
find -type f -name "*_CD32*.*" -exec rm -f {} \;
find -type f -name "*_CDTV*.*" -exec rm -f {} \;
find -type f -name "*_NTSC*.*" -exec rm -f {} \;
find -type f -name "*_AGA*.*" -exec rm -f {} \;
find -type f -name "*_De*.*" -exec rm -f {} \;
find -type f -name "*_Fr*.*" -exec rm -f {} \;
find -type f -name "*_It*.*" -exec rm -f {} \;
rm -f EmeraldMines_v1.zip

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
