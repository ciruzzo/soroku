# sh mkGenzo.sh | python replaceImage.py > result/正法眼蔵.html && mv statfile.txt result/stat_正法眼蔵.txt

basedir="shomonji_org/genzou"

cat kindleHtml.tmpl | sed 's/TITLE/正法眼藏/'

echo "<ol>"

for f in $(ls $basedir)
do
  t=$(cat $basedir/$f/index.html | iconv -f sjis | grep bgcolor |
    sed 's/color="#000000"//' |
    sed 's/color="#0000ff"//' |
    sed 's/<body bgcolor="#ffffff"><font size=\"+2\" >//' | 
    sed 's/<\/font><br>/<\/a><\/li>/')
  echo "<li><a href=\"#$f\">$t"
done 

echo "</ol>"

echo "<hr>"


for f in $(ls $basedir)
do 

  title=$(cat $basedir/$f/index.html | iconv -f sjis| grep "bgcolor" | sed 's/<body bgcolor=\"#ffffff\"><font size=\"+2\" color=\"#0000ff\">//' | sed 's/<body bgcolor=\"#ffffff\"><font size=\"+2\" color=\"#000000\">//' |sed 's/<\/font><br>//')

  echo "<h3 id=\""$f"\">"$title"</h3>"
  cat $basedir/$f/index.html | iconv -f sjis | head -n -2 | tail -n +6 

done 

echo "</body>"
echo "</html>"


