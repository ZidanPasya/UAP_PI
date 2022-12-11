from Akun import akun #import dictionaries Akun pada file akun
from time import sleep  #import module time(berkaitan dengan waktu)
from HomeScreen import HomeScreen #import fungsi HomeScreen dari file HomeScreen
import MainMenu #import file MainMenu
import os #import module os

def Login(nama, npm): #fungsi Login dengan paramater 'nama' dan 'npm'

    try: #error handling untuk mengecek apakah akun sudah diupdate dengan data baru atau belum
        if (nama == akun["akun"]["name"] and nama == akun["akun"]["NPM"]) or (nama == akun["akun"]["Username"] and nama == akun["akun"]["NPM"]):
            os.system('cls')
            print('Anda Berhasil login!')
            sleep(3)
            os.system('cls')
            HomeScreen(nama)
        else: #statement bila pernyataan salah
                os.system('cls')
                print("Nama atau Username dan Password tidak cocok!")
                print("Silahkan coba lagi...")
                sleep(3)
                os.system('cls')
                MainMenu.Menu() #memanggil perintah fungsi Menu pada file Menu
    except: #error handling jika data akun belum diupdate
        if (nama == akun["akun1"]["name"] and npm == akun["akun1"]["NPM"] or nama == akun["akun1"]["Username"] and npm == akun["akun1"]["NPM"]) or \
        (nama == akun["akun2"]["name"] and npm == akun["akun2"]["NPM"] or nama == akun["akun2"]["Username"] and npm == akun["akun2"]["NPM"]) or \
        (nama == akun["akun3"]["name"] and npm == akun["akun3"]["NPM"] or nama == akun["akun3"]["Username"] and npm == akun["akun3"]["NPM"]): #statement pengecekan inputan paramaeter sesuai dengan nama/username pada dictionaries        
            os.system('cls') # backslash digunakan untuk perintah bawah teks selanjutnya ada pada di baris baru
            print('Anda Berhasil login!')
            sleep(3)
            os.system('cls')
            HomeScreen(nama)
        else: #statement bila pernyataan salah
            os.system('cls')
            print("Nama atau Username dan Password tidak cocok!")
            print("Silahkan coba lagi...")
            sleep(3)
            os.system('cls')
            MainMenu.Menu()