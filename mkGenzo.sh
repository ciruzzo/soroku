# sh XXmkGenzou.sh > Kindle_html/正法眼蔵.html
# set -x

basedir="shomonji_org/genzou"

cat kindleHtml.tmpl | sed 's/TITLE/正法眼藏/'

echo "<ol>"
cat $basedir/genzou*/index.html | iconv -f sjis | 
grep bgcolor |
sed 's/html\/genzou\//<li><a href="#/' | 
sed 's/color="#000000"//' |
sed 's/color="#0000ff"//' |
sed 's/\/index.html:<body bgcolor="#ffffff"><font size=\"+2\" >/">/' | 
sed 's/<\/font><br>/<\/a><\/li>/'
echo "</ol>"


echo "<hr>"


for f in $(ls $basedir)
do 

title=$(cat $basedir/$f/index.html | iconv -f sjis| grep "bgcolor" | sed 's/<body bgcolor=\"#ffffff\"><font size=\"+2\" color=\"#0000ff\">//' | sed 's/<body bgcolor=\"#ffffff\"><font size=\"+2\" color=\"#000000\">//' |sed 's/<\/font><br>//')


echo "<h3 id=\""$f"\">"$title"</h3>"
cat $basedir/$f/index.html | python replaceImage2.py  | head -n -2 | tail -n +6 

done

echo "</body>"
echo "</html>"


