process ()
{
title=$1
file=$2
todir=$3
outfile=$3/$title.html
toline=$4
cat kindleHtml.tmpl | sed 's/TITLE/'$title'/' > $outfile
cat $file | python replaceImage2.py | head -n -2 | tail -n +$toline  >> $outfile
echo "</body>" >> $outfile
echo "</html>" >> $outfile
}

process2 ()
{
title=$1
file1=$2
file2=$3
outfile=$4/$title.html
cat kindleHtml.tmpl | sed 's/TITLE/'$title'/' >$outfile
cat $file1 | python replaceImage2.py | head -n -2 | tail -n +7 >>  $outfile
cat $file2 | python replaceImage2.py | head -n -2 | tail -n +7 >>  $outfile
echo "</body>" >>  $outfile
echo "</html>" >>  $outfile
}

todir="Kindle_html/"

fromdir="shomonji_org"
process "普勸坐禪儀" $fromdir/fukan/index.html $todir 8
process "無門關" $fromdir/mumonkan/index.html $todir 7
process "信心銘" $fromdir/shinjinmei/index.html $todir 7
process "證道歌" $fromdir/shodoka/index.html $todir 7


process2 "碧巖録" "$fromdir/hekiganroku/hekigan1.htm"  "$fromdir/hekiganroku/hekigan2.htm" $todir
process2 "從容録" "$fromdir/shoyoroku/shoyo1.htm" "$fromdir/shoyoroku/shoyo2.htm" $todir

