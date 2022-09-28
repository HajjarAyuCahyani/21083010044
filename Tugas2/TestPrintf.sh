#!/bin/bash

a=6
b=13
distroLinux="Ubuntu 19.04 LTS";
let c=a%b;

printf "OS : $distroLinux \n";
printf "$c \n";
printf "%.2f float \n" $a;
printf "%.1f float \n" $a;
