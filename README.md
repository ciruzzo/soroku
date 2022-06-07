# 祖録集の文字コード割り当て

shomonji.orgにある祖録集は、埋め込み文字になっているものがあり、それらの
画像になっている文字を、現在のユニコードに置き換えたら、どこまで置き換えられるのかという興味から
作業しました。

といっても旧字体・異字体の細かいところまで区別できるわけがないので、ほぼ同じなら可とする、という緩い方針です。

それでも結構いけるものだなあと思いました、変更後のファイルは
[こちら](soroku.md)にあります。

## 忘備録を兼ねた手順

- shomonji.orgからダウンロードしたファイルをshomonji_orgdataに保存。


- 手作業で画像と、文字を対応付けます。rules.txtがその対応表です。この対応表を使い、以下で
元のファイルの画像を文字に置き換えます。


- 以下で、文字を置き換えた[htmlファイル](html)の生成をします。ShiftJISからUTF8への変更も同時に行います。

``
$ python3 replaceImage.py
``

- 上記で生成したhtmlファイルからmarkdown記法に変換します。

``
$ sh html2md.sh
``

- 結果のファイルは[こちら](soroku.md)に。

- 上記の結果のファイルをごちゃごちゃ変形してKindle用のhtmlに直したものを[こちらに](Kindle_html)に置いた。

- 以下で、rules.txtを見やすくした[対応一覧](rules.md)の生成。

``
$ sh rules.sh
``

## 対応する文字が見つからなかったものと、代替の文字

以下の文字は現在はコード化されていないようなので、他の文字で置き換えました。


![尞頁](images/_cCQv_7X.png)  →顟 

![馬展](images/_cCjVaDr.png) →輾

![扌弃](images/_cKabH-y.png) →拌 

![己の下に十](images/_cM1mr0_.png) →畢

## 画像と選んだ文字の対応

[対応一覧](rules.md)


## 参考情報

### フォント

上記の対応一覧の文字のうち、
見えない文字がある場合、以下のフォントをインストールすると、見えるようになるかもしれません。


[花園フォント](https://ja.osdn.net/projects/hanazono-font/)

### 漢字の検索に便利だったツール

[グリフウィキ(GlyphWiki)](https://glyphwiki.org/wiki/GlyphWiki:%e3%83%a1%e3%82%a4%e3%83%b3%e3%83%9a%e3%83%bc%e3%82%b8)

[漢字辞典オンライン](https://kanji.jitenon.jp/)

[Unicode文字一覧表](https://tools.m-bsys.com/ex/unicode_table.php)


### 現代中国語のデジタルアーカイブ

[万松老人评唱天童觉和尚颂古从容庵录](http://fofa.foxue.org/fjyw/sutra_zzb/792/)

[佛果圜悟禅师碧岩录](http://fofa.foxue.org/fjyw/sutra_zzb/791/)

### 日本のアーカイブ
 
[大正蔵検索](https://21dzk.l.u-tokyo.ac.jp/SAT/satdb2015.php?)
