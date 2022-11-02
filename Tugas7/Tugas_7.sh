#!/bin/bash

persegi() {
      echo "Masukkan panjang : "
      read p
      echo "Masukkan lebar : "
      read l
      let c=$p*$l
      echo -e "Luas Persegi : \n$c "
}

persegi
