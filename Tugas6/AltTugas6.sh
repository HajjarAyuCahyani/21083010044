#!/bin/bash

echo "masukkan nilai IPS: "
read -a angka

t=0
for i in ${angka[@]}
do
    let t+=$i 
done

p=${#angka[@]}

echo "IPS mhs = $t / $p"
echo "IPK mhs = $((t / p))"
