# Capstone data pekerja

dk = {
    "NIP" : [1001,1002,1003,1004,1005], 
    "Nama": ["Budi Santoso", "John Doe", "Hanako Yamada", "Erika Mustermann", "Anna Kowalska"],
    "Umur": [35, 28, 33, 20, 40],
    "Jabatan": ["Manager", "Akuntan", "Supir", "Admin", "Satpam"],
    "Gaji": [10000000, 8000000, 5000000, 4000000, 5000000]
}
gaji = lambda gaji: f"Rp {gaji:,.0f}".replace(",", ".")

def generate_nip():
    if dk["NIP"]:
        return max(dk["NIP"]) + 1  

def mdp():
    print("\nDaftar Pekerja")
    print(f" {'NIP':<7} | {'Nama':<20} | {'Umur':<7} | {'Jabatan':<15} | {'Gaji':<12} |")
    print("-" * 76)
    for index, nip in enumerate(dk["NIP"]):
        print(f" {nip:<7} | {dk['Nama'][index]:<20} | {dk['Umur'][index]:<7} | {dk['Jabatan'][index]:<15} | {gaji(dk['Gaji'][index]):<12} |")
    print("-" * 76)

def addp():
    pekerja_baru = input("Masukkan nama Pekerja: ")
    nama = pekerja_baru.title()
    if nama in dk["Nama"]:
        print("Nama sudah ada dan tidak dapat diduplikat. Silakan input nama lain.")
        return addp()
    try:
        umur = int(input("Masukkan Umur Pekerja: "))
        gaji_pekerja = int(input("Masukkan Gaji Pekerja: "))
    except ValueError:
        print("Umur dan gaji harus berupa angka!")
        return addp()
    while True:
        jbp = input("Masukkan Jabatan Pekerja: ")
        jabatan = jbp.title()
        if jabatan in dk["Jabatan"]:
            print("Jabatan telah diisi oleh pekerja lain.")
            continue
        break
    nip_baru = generate_nip()
    dk["NIP"].append(nip_baru)
    dk["Nama"].append(nama)
    dk["Umur"].append(umur)
    dk["Jabatan"].append(jabatan)
    dk["Gaji"].append(gaji_pekerja)
    mdp()
    print("\nPekerja telah ditambahkan!\n")

def LOP():
    mdp()  
    try:
        nip = int(input("Masukkan NIP Pekerja yang ingin diberhentikan: "))
        if nip in dk["NIP"]:
            index =  dk["NIP"].index(nip)
            nama_terhapus = dk["Nama"].pop(index)
            dk["NIP"].pop(index)
            dk["Umur"].pop(index)
            dk["Jabatan"].pop(index)
            dk["Gaji"].pop(index)
            mdp()
            print(f"\nPekerja {nama_terhapus} telah diberhentikan!\n")
        else:
            print("NIP tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")
        return LOP()

def promote():
    mdp()
    try:
        nip = int(input("Masukkan NIP Pekerja yang akan dipromosikan: "))
        if nip in dk["NIP"]:
            index = dk["NIP"].index(nip)
            jabatan_lama = dk["Jabatan"][index]
            gaji_lama = dk["Gaji"][index]     
            jabatan_baru = input(f"Masukkan jabatan baru untuk {dk['Nama'][index]} (Jabatan lama: {jabatan_lama}): ")
            jabatan = jabatan_baru.title()
            try:
                gaji_baru = int(input(f"Masukkan gaji baru untuk {dk['Nama'][index]} (Gaji lama: {gaji(gaji_lama)}): "))
                if gaji_baru > gaji_lama:
                    dk["Jabatan"][index] = jabatan
                    dk["Gaji"][index] = gaji_baru
                    mdp()
                    print(f"\n{dk['Nama'][index]} telah dipromosikan menjadi {jabatan} dengan gaji {gaji(gaji_baru)}!\n")
                else:
                    print("Gaji baru harus lebih tinggi dari gaji lama!")
                    return promote()
            except ValueError:
                print("Masukkan angka yang valid untuk gaji!")
                return promote()
        else:
            print("Index tidak valid!")
    except ValueError:
        print("Masukkan Value yang Valid!")
        return promote()

def prog():
    while True:
        print("\nSelamat datang di Program Manajemen Pekerja Perusahaan!")
        print("List Menu:")
        print("1. Menampilkan Daftar Pekerja")
        print("2. Menambah Pekerja")
        print("3. Pemberhentian Pekerja")
        print("4. Promosi Pekerja")
        print("5. Exit Program")
        pilihan = input("Masukkan angka menu yang ingin dijalankan: ")
        if pilihan == "1":
            mdp()
        elif pilihan == "2":
            addp()
        elif pilihan == "3":
            LOP()
        elif pilihan == "4":
            promote()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("\nMenu tidak valid! Silakan coba lagi.\n")

if __name__ == "__main__":
    prog()