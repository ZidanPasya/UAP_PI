from SignUp import SignUp #import fungsi Signup pada file SignUp
from Login import Login #import fungsi login pada file Login
import os #import module os
import time #import module time

def Menu(): #fungsi Menu
    os.system('cls')
    try:
        menu = ["Selamat Datang","1. Sign-Up", "2. Login", "3. Exit"] #list menyimpan data
        for i in range(4): # for loop untuk meng output isi list
            print(menu[i])

        pilih = int(input("Masukkan Pilihan: "))
        if pilih == 1:
            SignUp() #perintah ke menu file SignUp bagian fungsi SignUp
        elif pilih == 2:
            nama = str(input("Masukkan Nama: "))
            npm = int(input("Masukkan NPM: "))
            Login(nama, npm) #perintah ke fungsi Login
        elif pilih == 3:
            print('Terima kasih') #keluar dari program
        else:
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3)
            Menu() #kembali ke fungsi Menu
    except: #error handling bila input tidak sesuai
        os.system('cls')
        Menu() #kembali ke fungsi Menu