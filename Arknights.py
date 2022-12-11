import requests #import module requests
import os #import module os
import time #import module time

ark = requests.get('https://raw.githubusercontent.com/Aceship/Arknight-Data-Convert/master/json/akhr.json') #mengambil API arknights dari link github
arkSuccess = ark.json() #menampung API ke dalam variabel arkSuccess

Name,Camp,Role,Rarity,Gender,Trait,Tags = ',,,,,,,' #deklarasi variabel untuk menampung API yang akan dimasukkan ke dalam File txt

class Character: #class Character
    def __init__(self, name): #sebagai constructor
        self.name = name
    
    def info(self):
        os.system('cls') #berfungsi sebagai clear screen pada layar
        for op in arkSuccess: #melooping isi dari API
            if op['name'] == self.name: #cek apakah nama yang diinput terdapat dalam API atau tidak
                print('Name\t\t:', op['name'])
                print('Camp\t\t:', op['camp'])
                print('Role\t\t:', op['type'])
                print('Rarity\t\t:', op['level'])
                print('Gender\t\t:', op['sex'])
                print('Trait\t\t:', op['characteristic'])
                print('Tags\t\t:', op['tags'])
                break #memberhentikan jika nama yang diinput terdapat dalam API
        else: #jika nama yang diinput tidak terdapat dalam API
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3) #memberika jeda selama 3 detik
            Arknights() #memanggil fungsi Arknights

    def infoTxt(self):
        try: #error handling apakah inputan benar atau tidak
            pilih = ['1. Yes', '2. No'] #list yang berisikan yes dan no
            print('Apakah ingin menyimpan dalam file')
            for i in pilih:
                print(i) #print isi dari list
            choose2 = int(input('Masukkan pilihan : '))
            if choose2 == 1: #jika memilih choose2 = 1
                for op in arkSuccess: #melooping isi dari API
                    if op['name'] == self.name: #cek apakah nama yang diinput terdapat dalam API atau tidak
                        Name = op['name']
                        Camp = op['camp']
                        Role = op['type']
                        Rarity = op['level']
                        Gender = op['sex']
                        Trait = op['characteristic']
                        Tags = op['tags']

                op_Bio = ['Name\t\t:' + Name, 
                            'Camp\t\t:' + Camp,
                            'Role\t\t:' + Role,
                            'Rarity\t\t:' + str(Rarity),
                            'Gender\t\t:' + Gender,
                            'Trait\t\t:' + Trait,
                            'Tags\t\t:' + str(Tags)] #variabel yang menampung data API untuk disimpan dalam file

                with open('C:\\Users\\Lenovo\\Documents\\Python\\PI\\UAP\\readme.txt','w') as f: #membuka file
                    f.write('\n'.join(op_Bio)) #menulis/menimpa file dengan data API

                os.system('cls')
                print('Berhasil memasukkan data dalam file')
            elif choose2 == 2: #jika choose2 = 2
                exit() #keluar dari program
        except IOError: #error handling saat terjadi IOError
            exit()
        except ValueError: #error handling saat terjadi ValueError
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3)
            Arknights()

def Arknights():
    os.system('cls')
    print('Welcome to Arknights Wiki')
    for i in arkSuccess: #melooping isi dari API
        print(i['name']) #print isi dari nama di dalam API
    print('Pilih info character yang ingin dilihat')
    choose = str(input('Input name: ')) #input string
    ak = Character(choose) #inisialisasi class dengan parameter
    ak.info() #memanggil fungsi info di dalam class Arknights
    ak.infoTxt() #memanggil fungsi infoTxt di dalam class Arknights