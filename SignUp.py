from Akun import akun 
from time import sleep 
from HomeScreen import HomeScreen
import MainMenu
import os

def SignUp():
    try: #error handling jika ada kesalahan input
        username = str(input("Masukkan Username: "))
        nama = str(input("Masukkan Nama: "))
        npm = int(input("Masukkan NPM: "))

        if username != username.lower(): #statement jika username tidak sama denngan username.lower(convert string ke lower case)
            os.system('cls') #membersikan layar console
            print("Username Tidak Valid!")
            print("Username harus dalam lower case!")
            sleep(3) #memberi delay atau jeda
            os.system('cls')
            MainMenu.Menu() #perintah menuju file Menu bagian fungsi Menu
        else:    
            nama = nama.capitalize() # huruf pertama isi dari variabel nama akan di convert ke kapital
            akun.update(akun = {"Username":username, "name": nama, "NPM":npm}) #file akun akan di update, dan ditambahkan data key dan value sesuai input
            os.system('cls')
            HomeScreen(nama) #perintah menuju file HomeScreen
    except: #error handling akan memanggil kembali fungsi
        os.system('cls')
        SignUp() #memanggil fungsi SignUP