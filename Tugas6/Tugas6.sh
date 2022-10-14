#!/bin/bash

echo -n "Masukkan banyaknya nilai yang dibutuhkan: "
read n
echo "Masukkan nilai: "

declare -a oi

i=0
while [ $i -lt $n ]
do
    read a[$i]
    oi[$i]=${a[$i]}
    i=`expr $i + 1`
done

x=0
for v in ${oi[@]}
do
    let x+=$v
done

echo "IPS mhs = $x / $n"
echo "IPK mhs = $((x / n))"

