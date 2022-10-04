process ()
{
title=$1
file=$2
todir=$3
outfile=$3/$title.html
toline=$4
cat kindleHtml.tmpl | sed 's/TITLE/'$title'/' > $outfile
cat $file | head -n -2 | tail -n +$toline  >> $outfile
echo "</body>" >> $outfile
echo "</html>" >> $outfile
cat $outfile | python unicodenormalize.py > /tmp/1
mv /tmp/1 $outfile
}

process2 ()
{
title=$1
file1=$2
file2=$3
outfile=$4/$title.html
cat kindleHtml.tmpl | sed 's/TITLE/'$title'/' >$outfile
cat $file1 | head -n -2 | tail -n +7 >>  $outfile
cat $file2 | head -n -2 | tail -n +7 >>  $outfile
echo "</body>" >>  $outfile
echo "</html>" >>  $outfile
cat $outfile | python unicodenormalize.py > /tmp/1
mv /tmp/1 $outfile
}

todir="Kindle_html/"

process "普勸坐禪儀" html/fukan/index.html $todir 8
process "無門關" html/mumonkan/index.html $todir 7
process "信心銘" html/shinjinmei/index.html $todir 7
process "證道歌" html/shodoka/index.html $todir 7


process2 "碧巖録" "html/hekiganroku/hekigan1.htm"  "html/hekiganroku/hekigan2.htm" $todir
process2 "從容録" "html/shoyoroku/shoyo1.htm" "html/shoyoroku/shoyo2.htm" $todir

