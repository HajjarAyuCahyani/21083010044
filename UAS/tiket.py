
tiket= []
all = []
import os
import sys

def kembali():
	print("\n")
	input("Tekan tombol apa saja untuk kembali ke main menu ")
	os.system('clear' if (os.name=='nt') else 'clear')
while True:
	print("\n")
	print("+=============================================================================+")
	print("           SELAMAT DATANG DI APLIKASI AGEN TIKET BUS SINAR JAYA                ")
	print("                        KHUSUS KEBERANGKATAN JAKARTA                           ")
	print(" _____________________________________________________________________________ ")
	print("                            - PLAN.BOOK.TRAVEL -                               ")
	print("+=============================================================================+")
	print("\n")
	print("+=============================================================================+")
	print("                                MAIN MENU                                      ")
	print("+============================================================================= ")
	print("    1. Daftar Rute                                                             ")
	print("    2. Tiket Saya                                                              ")
	print("    3. Informasi Fasilitas Bus						      ")
	print("    4. Exit Program                                                            ")
	print("+=============================================================================+")
	m = int(input("masukan pilihan anda: "))
	if m == 1:
		print("\n")
		print("+===================================================================+")
		print(" 			DAFTAR RUTE DAN HARGA                       ")
		print("+===================================================================+")
		print(" 	RUTE			|	HARGA                       ")
		print(" ------------------------------------------------------------------- ")
		print("  1. Jakarta - Surabaya          |      505.000                      ")
		print("  2. Jakarta - Semarang          |      370.000                      ")
		print("  3. Jakarta - Jogja             |      370.000                      ")
		print("  4. Jakarta - Malang            |      580.000                      ")
		print("  5. Jakarta - Solo              |      370.000                      ")
		print("+===================================================================+")
		k = int(input("masukkan pilihan anda: "))
		if k == 1:
			print("\n")
			print("+===================================================================+")
			print(" 			INFORMASI RUTE PILIHAN                      ")
			print("+===================================================================+")
			print(" 	KEBERANGKATAN		|      WAKTU KEBERANGKATAN          ")
			print(" ------------------------------------------------------------------- ")
			print("  Tanjung Priuk                  |  		15.00               ")
			print("  Pulo Gebang                    |  		15.45               ")
			print("  Kampung Rambutan               |  		16.00               ")
			print("  Kelapa Gading                  |  		18.00               ")
			print("+===================================================================+")
			l = input("Apakah anda ingin menggunakan rute ini? [y/t] ")
			if l == "y":
				h1 = 505000
				j = int(input("Jumlah tiket yang ingin dibeli: "))
				tot1 = h1*j
				tiket.append(["Jakarta - Surabaya", j, tot1])
				all.append(tot1)
				print("Sukses Menambahkan Tiket")
				kembali()
				
		else:
			next
	
		if k == 2:
			print("\n")
			print("+===================================================================+")
			print("                         INFORMASI RUTE PILIHAN                      ")
			print("+===================================================================+")
			print("         KEBERANGKATAN           |      WAKTU KEBERANGKATAN          ")
			print(" ------------------------------------------------------------------- ")
			print("  Kalideres        		|  		16.00               ")
			print("  Lebak Bulus      		|  		17.00               ")
			print("  Kampung Rambutan 		|  		17.30               ")
			print("  Pulo Gebang      		|  		18.15               ")
			print("+===================================================================+")
			t = input("Apakah anda ingin menggunakan rute ini? [y/t] ")
			if t == "y":
				h2 = 370000
				w = int(input("Jumlah tiket yang ingin dibeli: "))
				tot2 = h2*w
				all.append(tot2)
				tiket.append(["Jakarta - Semarang", w, tot2])
				print("Sukses Menambahkan Tiket")
				kembali()
		else:
			next
		if k == 3:
			print("\n")
			print("+===================================================================+")
			print("                         INFORMASI RUTE PILIHAN                      ")
			print("+===================================================================+")
			print(" 	KEBERANGKATAN 		|	WAKTU KEBERANGKATAN	    ")
			print(" ------------------------------------------------------------------- ")
			print("  Lebak Bulus      		|  		16.30               ")
			print("  Pulo Gebang      		|  		18.00               ")
			print("  Kampung Rambutan 		|  		17.15               ")
			print("+===================================================================+")
			s = input("Apakah anda ingin menggunakan rute ini? [y/t] ")
			if s == "y":
				h3 = 370000
				n = int(input("Jumlah tiket yang ingin dibeli: "))
				tot3 = h3*n
				all.append(tot3)
				tiket.append(["Jakarta - Jogja", n, tot3])
				print("Sukses Menambahkan Tiket")
				kembali()
		else:
			next
		if k == 4:
			print("\n")
			print("+===================================================================+")
			print("                         INFORMASI RUTE PILIHAN                      ")
			print("+===================================================================+")
			print("         KEBERANGKATAN           |       WAKTU KEBERANGKATAN         ")
			print(" ------------------------------------------------------------------- ")
			print("  Kampung Rambutan               |               16.00               ")
			print("  Pulo Gebang	                |               16.30               ")
			print("+===================================================================+")
			q = input("Apakah anda ingin menggunakan rute ini? [y/t] ")
			if q == "y":
				h4 = 580000
				c = int(input("Jumlah tiket yang ingin dibeli: "))
				tot4 = h4*c
				all.append(tot4)
				tiket.append(["Jakarta - Malang", c, tot4])
				print("Sukses Menambahkan Tiket")
				kembali()
		
		else:
			next
		if k == 5:
			print("\n")
			print("+===================================================================+")
			print("                         INFORMASI RUTE PILIHAN                      ")
			print("+===================================================================+")
			print("         KEBERANGKATAN           |       WAKTU KEBERANGKATAN         ")
			print(" ------------------------------------------------------------------- ")
			print("  Lebak Bulus                    |               16.30               ")
			print("  Pulo Gebang                    |               17.15               ")
			print("  Kampung Rambutan               |               18.00               ")
			print("+===================================================================+")
			h = input("Apakah anda ingin menggunakan rute ini? [y/t] ")
			if h == "y":
				h5 = 370000
				e = int(input("Jumlah tiket yang ingin dibeli: ")) 
				tot5 = h5*e
				all.append(tot5)
				tiket.append(["Jakarta - Solo", e, tot5])
				print("Sukses Menambahkan Tiket")
				kembali()
		else:
			next

	elif m == 2:
		if len(tiket) != 0:
			print("\n")
			print("+==========================================================+")
			print(" 		      PESANAN ANDA                         ")
			print("+==========================================================+")
			print(" 	Rute & Jumlah	     |          Harga              ") 
			print("----------------------------------------------------------- ")
			for rute, jum, tot in tiket:
				print("   "+ rute + "  ("+str(jum)+")" +"               " +str(tot)+"                ")
			print("----------------------------------------------------------- ")
			print(" 	TOTAL HARGA	     |       " + str(sum(all))      )
			print("+==========================================================+")
			kembali()
		else:
			print("\n")
			print("+===========================================================+")
			print("	         Anda Belum Memesan Tiket                    ")
			print("+===========================================================+")
			kembali()

	elif m == 3:
		print("\n")
		print("+=============================================================================+")
		print(" 			INFORMASI FASILITAS BUS				      ")
		print(" ----------------------------------------------------------------------------- ")
		print("  1. Reclining Seat 1-1							      ")
		print("  2. AC									      ")
		print("  3. Toilet								      ")
		print("  4. LCD TV								      ")
		print("  5. Stop Kontak								      ")
		print("  6. Selimut 								      ")
		print("  7. Bantal 								      ")
		print("  8. Guling								      ")
		print("  9. Port USB								      ")
		print("  10. Snack								      ")
		print("  11. Free Air Mineral							      ")
		print("  12. Free Wifi								      ")
		print("+=============================================================================+")
		kembali()

	elif m == 4:
		if len(tiket) == 0:
			print("\n")
			print("+=============================================================================+")
			print("                 Terima Kasih Telah Menggunakan Layanan Kami                   ")
			print("                     Kepuasan Anda Adalah Prioritas Kami                       ")
			print("+=============================================================================+")
			break

			
		else:
			print("\n")
			print("+=============================================================================+")
			print("                           MOHON LAKUKAN PEMBAYARAN!                           ")
			print(" ----------------------------------------------------------------------------- ")
			print("                 Terima Kasih Telah Menggunakan Layanan Kami                   ")
			print("                      Kepuasan Anda Adalah Prioritas Kami                      ")
			print("+=============================================================================+")
			break

	else:
		print("\n")
		print("+=============================================================================+")
		print(" 			Maaf Pilihan Anda Tidak Ada                          ")
		print("       Silahkan Coba Lagi dan Pastikan Pilihan Anda Terdapat di Main Menu     ")
		print("+=============================================================================+")
		kembali()

	
