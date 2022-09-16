#!/bin/bash

printf "Which member do you like?\n"
printf "Jae?\n"
printf "Sungjin?\n"
printf "Brian?\n"
printf "Wonpil?\n"
printf "Dowoon?\n"

read desik

case "$desik" in
  "Jae")
    echo "Jars!Stop Parasocial"
    ;;
  "Sungjin")
    echo "manifesting Sungjin's solo album :))"
    ;;
  "Brian")
    echo "WHO IS BRIAN! YOUNGK!"
    ;;
  "Wonpil")
    echo "Oh My Gawd Jae!"
    ;;
  "Dowoon")
    echo "But I like it!"
    ;; 
  *)
    echo "Who's that?"
    ;;
esac
