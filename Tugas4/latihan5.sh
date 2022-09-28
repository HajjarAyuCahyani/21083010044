#!/bin/bash

echo "Silahkan masukkan bilangan positif kelipatan ganjil: "
read angka;
a=$angka
while [ $a -gt 0 ]
do 
  echo $a
  a=$((a - 2))
done
