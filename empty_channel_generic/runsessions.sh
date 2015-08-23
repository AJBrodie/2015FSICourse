#!/bin/bash
j=0
for file in *.in; do
	
echo $file
mv "$file" "File.in"
js=$(printf '%02d' $j)
python3 empty_channel.py

mkdir ${js}
mv File.in ${js}/
mv *.msh ${js}/
mv *.res ${js}/
mv LOG.txt ${js}/
((j++))

done
