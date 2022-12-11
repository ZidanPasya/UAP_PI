
import time #import module time
import os #import module os
from BlueArchive import BlueArchive #import Fungsi BlueArchive dari file BlueArchive
from Arknights import Arknights #import Fungsi Arknights dari file Arknights
from FateGrandOrder import FateGrandOrder #import Fungsi FateGrandOrder dari file FateGrandOrder
from GenshinImpact import GenshinImpact #import Fungsi GenshinImpact dari file GenshinImpact

def HomeScreen(nama): #fungsi HomeScreen dengan parameter nama
    os.system('cls')
    try: #error handling apakah inputan benar atau tidak
        game = ['1. Arknights', '2. Blue Archive', '3. Fate Grand Order', '4. Genshin Impact', '5. Exit'] #list untuk menampung isi game
        print('Selamat Datang', nama,  'di Wiki Game')
        for i in game: 
            print(i) #input semua isi game dalam list
        choose = int(input('Masukkan pilihan : '))
        if choose == 1:
            Arknights() #memanggil fungsi Arknights
        elif choose == 2:
            BlueArchive() #memanggil fungsi BlueArchive
        elif choose == 3:
            FateGrandOrder() #memanggil fungsi FateGrandOrder
        elif choose == 4:
            GenshinImpact() #memanggil fungsi GenshinImpact
        elif choose == 5:
            print('Terima kasih') #keluar dari program
        else:
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3)
            HomeScreen(nama) #mengembalikan kembali ke fungsi HomeScreen
    except: #error handling jika inputan salah
        os.system('cls')
        HomeScreen(nama) #mengembalikan kembali ke fungsi HomeScreen
