#cat data.txt |tr -d ["\n"]|tr -s "sensor" "\n" |tr -d " ="|tr -s '\r' " " >a.txt
cat old.txt |tr -d ["\n"]|tr -s "s=" "\n" >a.txt |tr -s '\r' " " >a.txt
sed '1d' a.txt >data.txt
rm a.txt
