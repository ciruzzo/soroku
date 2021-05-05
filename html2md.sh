# genzo
basedir="html/soroku/"
todir="md"
for d in $(ls $basedir)
do
  infile=$basedir/$d/index.html
  tmpfile=/tmp/tmp.txt
  tofile=$todir/$(basename $d).md
  echo $tofile

  # cat $infile | sed '/^<!DOCTYPE HTML PUBLIC/d' | sed '/^<body bgcolor="#ffffff"><font size="+2" color="#0000ff">/d'  > $tmpfile
  cat $infile | sed '/^<!DOCTYPE HTML PUBLIC/d' | sed '/^<title/d'  > $tmpfile

  python3 html2md.py $tmpfile $tofile
done


# others
basedir="ls html/*_files"
basedirs=$(ls -d html/*_files)
todir="md"
for basedir in $basedirs
do
  infile=$basedir/$(basename $(ls $basedir/*html))
  tmpfile=/tmp/tmp.txt
  tofile=$todir/$(basename $basedir | sed 's/_files//').md
  echo $tofile

  cat $infile | sed '/^<!DOCTYPE HTML PUBLIC/d'  \
              | sed '/^<!DOCTYPE html PUBLIC/d' \
              | sed '/^<body bgcolor="#ffffff"><font size="+2" color="#0000ff">/d'  > $tmpfile

  python3 html2md.py $tmpfile $tofile
done
