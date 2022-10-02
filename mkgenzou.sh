# sh mkgenzou.sh > Kindle_html/正法眼蔵.html

basedir="html/genzou"

cat kindleHtml.tmpl | sed 's/TITLE/正法眼藏/'

grep bgcolor $basedir/genzou*/index.html | 
sed 's/html\/genzou\//<li><a href="#/' | 
sed 's/color="#000000"//' |
sed 's/color="#0000ff"//' |
sed 's/\/index.html:<body bgcolor="#ffffff"><font size=\"+2\" >/">/' | 
sed 's/<\/font><br>/<\/a><\/li>/'


echo "<hr>"


for f in $(ls $basedir)
do 

title=$(cat $basedir/$f/index.html | grep "bgcolor" | sed 's/<body bgcolor=\"#ffffff\"><font size=\"+2\" color=\"#0000ff\">//' | sed 's/<body bgcolor=\"#ffffff\"><font size=\"+2\" color=\"#000000\">//' |sed 's/<\/font><br>//')


echo "<h3 id=\""$f"\">"$title"</h3>"
cat $basedir/$f/index.html | head -n -2 | tail -n +6 

done

echo "</body>"
echo "</html>"


