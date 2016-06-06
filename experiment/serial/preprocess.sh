#cat data.txt |tr -d ["\n"] >a.txt
:s/sensor = / \r /g

cat a.txt | tr -d '\r' >new.txt
rm a.txt
