#!/bin/sh

# print memory usage for each user on machine
# reference : https://serverfault.com/a/31056

OLDIFS=$IFS
IFS=$'\n'
tempsum=0
totalmem=0
for m in `ps -eo user,rss --sort user | sed -e 's/  */ /g' | awk -F'[ ]' {'print $0'}`; do
  nu=`echo $m|cut -d" " -f1`
  nm=`echo $m|cut -d" " -f2`
  # echo "$nu $nm $nu"
  if [ "$nu" != "$ou" ] && [ $(echo "$nm"|grep -E "^[0-9]+$") ]
  then
    if [ "$tempsum" -ne 0 ]; then echo "memusage for $ou: $((tempsum/1000000))"; fi
    ou=$nu
    tempsum=$nm
    let "totalmem += $nm"
  else
    let "tempsum += $nm"
    let "totalmem += $nm"
  fi
done
  d=$(free | grep Mem: | awk '{print $2}')
echo "Total Memory in Use: $((totalmem/1000000))/$((d/1000000))"
IFS=$OLDIFS