#!/bin/bash
source processknols.rc
TEMPDIR=$(mktemp -d)

cd $TEMPDIR

wget $SOURCE -O - | xpath -q -e '//div[@id="knol-collection-container"]//a[@class="knol-search-knol-title"]/@href' | sed -e 's/.*href="//' -e 's/"//' > urls

NUMBER=0
for url in $(cat urls); do
	echo -n "Retrieving $url... "
	NUMBER=$((NUMBER + 1))
	FILENAME=$(printf "%03d.html" $NUMBER)
	wget "$BASE$url" -O $FILENAME 2>/dev/null
	
	sed -i '/\<head/ a\
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">' $FILENAME

	echo "done."
done

zip $ZIPFILE *html

rm -rf $TEMPDIR

