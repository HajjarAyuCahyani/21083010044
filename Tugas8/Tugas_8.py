from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

x = int(input())

def oddeven(i):
    if (i%2) == 0:
        return "genap"
    else:
        return "ganjil"

def cetak(i):
    print(i+1, oddeven(i+1), "- punya ID proses", getpid())
    sleep(1)

print("Sekuensial")
for i in range(x):
   cetak(i)
print("\n")

print("multiprocessing.Process")
kumpulan_proses = []

for i in range(x):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()

print("\n")

print("Multiprocessing.Pool")
pool = Pool()
pool.map(cetak, range(x,))
pool.close()
