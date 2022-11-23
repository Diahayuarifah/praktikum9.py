def tulis(nama, umur, alamat, email, dosen):
    with open("bio.txt", "w") as f:
        f.write(f"Nama: {nama}\n")
        f.write(f"Umur: {umur}\n")
        f.write(f"Alamat: {alamat}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Dosen Wali: {dosen}\n")
        f.close()

def baca():
    with open("bio.txt", "r") as f:
        print(f.read())
        f.close()

if __name__ == "__main__":
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    email = input("Email: ")
    dosen = input("Dosen Wali: ")
    tulis(nama, umur, alamat, email, dosen)
    baca()
