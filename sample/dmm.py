#! /usr/bin/python
# -*- encoding: utf-8 -*-
import urllib2
import BeautifulSoup
import time

url_t="http://www.dmm.co.jp/digital/videoa/-/actress/=/keyword={id}/"

ids=["a","i","u","e","o",
"ka","ki","ku","ke","ko",
"sa","si","su","se","so",
"ta","ti","tu","te","to",
"na","ni","nu","ne","no",
"ha","hi","hu","he","ho",
"ma","mi","mu","me","mo",
"ya","yu","yo",
"ra","ri","ru","re","ro",
"wa"]


f = open("tmp.txt","w")
for i in ids:
    url=url_t.format(id=i)
    print i
    lines = urllib2.urlopen(url).read()
    #lines = unicode(lines, chardet.detect(lines)['encoding'])

    soup = BeautifulSoup.BeautifulSoup(lines)
    r = soup(attrs={'class': 'act-box-65 group mg-b20'})
    f.write(str(r[0].find))
    time.sleep(5)

f.close()