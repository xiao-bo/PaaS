#cat data.txt |tr -d ["\n"]|tr -s "sensor" "\n" |tr -d " ="|tr -s '\r' " " >a.txt
cat data.txt |tr -d ["\n"]|tr -s "s=" "\n" |tr -s '\r' " " >a.txt
sed '1d' a.txt >new.txt
rm a.txt