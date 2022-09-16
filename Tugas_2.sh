#!/bin/bash
clear

printf "Halo, selamat datang di kalkulator dua variabel!\n"
echo -n "Silahkan masukkan angka 1: "
read a1;

echo -n "Silahkan masukkan angka 2: ";
read a2;

printf "Aritmatika apa yang ingin dipakai?\n"
printf "jumlah?\n"
printf "kurang?\n"
printf "kali?\n"
printf "bagi?\n"

read mat;

let j="$a1+$a2"
let k="$a1-$a2"
let l="$a1*$a2"
let b="$a1/$a2"

case "$mat" in 
  "jumlah")
    echo "$j"
    ;;
  "kurang")
    echo "$k"
    ;;
  "kali")
    echo "$l"
    ;;
  "bagi")
    echo "$b" 
    ;;
  *)
    echo "Maaf aku ga mampu"
    ;;
esac
