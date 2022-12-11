import requests, os, time #import module requests,os,time

Chara = requests.get('https://api.genshin.dev/characters') #mengambil API Genshin dari link web
Characters = Chara.json() #menampung API ke dalam variable Characters

Rarity,Name,Vision,Weapon,Region,Affiliation = ',,,,,,' #deklarasi variable untuk menampung API yang akan dimasukan ke dalam file txt

class Character: #class Character
    def __init__(self, name): #constructor
        self.name = name

    def info(self):
        os.system('cls') #befungsi sebagai clear screen pada layar
        for cgi in Characters: #melooping isi dari API
            if cgi == self.name: #mengecek apakah nama yang di input dalam API atau tidak
                hero = requests.get('https://api.genshin.dev/characters/' + self.name)
                heroSuccess = hero.json()
                print('Rarity\t\t:',heroSuccess['rarity'])
                print('Name\t\t:',heroSuccess['name'])
                print('Vision\t\t:',heroSuccess['vision'])
                print('Weapon\t\t:',heroSuccess['weapon'])
                print('Region\t\t:',heroSuccess['nation'])
                print('Affiliation\t:',heroSuccess['affiliation'])
                break #memberhentikan jika nama yang diinput terdapat dalam API
        else: #jika nama yang di input tidak terdapat dalam API
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3) #memberikan  jeda selama 3 detik
            GenshinImpact() #memanggil fungsi terdapat dalam API
    
    def infoTxt(self):
        try: #error handling apakah benar atau tidak
            pilih = ['1. Yes', '2. No'] #list yang berisi yes dan no
            print('Apakah ingin menyimpan dalam file')
            for i in pilih:
                print(i) #print isi dari list
            choose2 = int(input('Masukkan pilihan : '))
            if choose2 == 1: #jika memilih choose2 = 1
                hero = requests.get('https://api.genshin.dev/characters/' + self.name)
                heroSuccess = hero.json()
                Rarity = heroSuccess['rarity'] 
                Name = heroSuccess['name'] 
                Vision = heroSuccess['vision'] 
                Weapon = heroSuccess['weapon'] 
                Region = heroSuccess['nation'] 
                Affiliation = heroSuccess['affiliation'] 

                HeroBio = ['Rarity\t\t:'+ str(Rarity),
                        'Name\t\t:'+ Name,
                        'Vision\t\t:'+ Vision,
                        'Weapon\t\t:'+ Weapon,
                        'Region\t\t:'+ Region,
                        'Affiliation\t:'+ Affiliation] #variable yang menampung data API untuk disimpan dalam file
                
                with open('C:\\Users\\Lenovo\\Documents\\Python\\PI\\UAP\\readme.txt','w') as f: #membuka file 
                    f.write('\n'.join(HeroBio)) #menulis/menimpa file dengan data dari API

                os.system('cls')
                print('Berhasil memasukkan data dalam file')
            elif choose2 == 2 : #jika choose2 == 2
                exit() #keluar dari program
        except IOError: #error handling saat terjadi IOError
            exit()
        except ValueError: #error handling saat terjadi ValueError
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3)
            GenshinImpact()

def GenshinImpact():
    os.system('cls')
    print('Welcome to Genshin Impact Wiki')
    for i in Characters: #melooping isi dari API
        print(i) #print isi dari nama di dalam API
    print('Pilih info character yang ingin dilihat')
    choose = str(input('Input name: ')) #input string
    gi = Character(choose) #insialisasi class dengan parameter
    gi.info() #memanggil fungsi di dalam class GenshinImpact
    gi.infoTxt() #memanggil fungsi infoTxt di dalam class GenshinImpact