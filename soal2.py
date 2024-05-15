data_diri = ('Revandra Talenta', '71231041', 'Yogyakarta Indonesia')

nama, nim, alamat = data_diri

nim_tuple = tuple(nim)
nama_depan_tuple = tuple(nama.split()[0])
nama_terbalik_tuple = tuple(nama.split()[::-1])

print("Data:", data_diri)
print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)
print("NIM:", nim_tuple)
print("NAMA DEPAN:", nama_depan_tuple)
print("NAMA TERBALIK:", nama_terbalik_tuple)
