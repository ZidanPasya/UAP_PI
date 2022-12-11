import requests, os, time #import module requsest,os,time

fgo = requests.get('https://gist.githubusercontent.com/nisegami/d7eab484484ae8ee1958a09f73207fac/raw/7544537c95a944e951288f34c44ef2cb5526c2bf/fgo.json') #mengambil APi FGO dari link github
fgoSuccess = fgo.json() #menampung API ke dalam variable fgoSuccess

Role,name,Rarity,alignment,Seegs,Seiyuu,Base_ATK,Base_HP = ',,,,,,,,' #mendeklarasi variable untuk menampung API yang akan dimasukan ke dalam file txt

class Character: #class Charcter
    def __init__(self, name): #sebagai  consturctor
        self.name = name
    
    def info(self):
        os.system('cls') #berfungsi sebagai clear screen pada layar
        for servant in fgoSuccess: #meloooping isi dari API
            if servant['name'] == self.name: #cek apakah nama yang di input terdapta dalam API atau tidak
                print('Name\t\t:', servant['name'])
                print('Role\t\t:', servant['class'])
                print('Rarity\t\t:', servant['rarity'])
                print('Alignment\t:', servant['alignment'])
                print('Gender\t\t:', servant['gender'])
                print('VA\t\t:', servant['seiyuu'])
                print('Base ATK\t:', servant['base_atk'])
                print('Base HP\t\t:', servant['base_hp'])
                break
        else:
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3) #memberikan jada selama 3 detik  
            FateGrandOrder() #memanggil fungsi FateGrandOrder
    
    def infoTxt(self):
        try: #error handling apakh inputan benar atau tidak
            pilih = ['1. Yes', '2. No'] #list yang berfungsi berisikan yes dan no
            print('Apakah ingin menyimpan dalam file')
            for i in pilih:
                print(i) #print isi dari list
            choose2 = int(input('Masukkan pilihan : '))
            if choose2 == 1: #jika memilih choose2 = 1
                for servant in fgoSuccess: #melooping list dari API
                    if servant['name'] == self.name: #cek apakah nama yang diinput terdapat dalam API atau tidak
                        Role = servant['class']
                        Rarity = str(servant['rarity'])
                        name = servant['name']
                        alignment = servant['alignment']
                        Seegs = servant['gender']
                        Seiyuu = servant['seiyuu']
                        Base_ATK = str(servant['base_atk'])
                        Base_HP = str(servant['base_hp'])

                Servant_Bio = ['Name\t\t:' + name, 
                            'Role\t\t:' + Role,
                            'Rarity\t\t:' + Rarity,
                            'Alignment\t:' + alignment,
                            'Gender\t\t:' + Seegs,
                            'VA\t\t:' + Seiyuu,
                            'Base ATK\t:' + Base_ATK,
                            'Base HP\t\t:' + Base_HP] #variable yang menampung data API untuk disimpan dalam file

                with open('C:\\Users\\Lenovo\\Documents\\Python\\PI\\UAP\\readme.txt','w') as f: #membuka file
                    f.write('\n'.join(Servant_Bio)) #menulis/menimpa file dengan data API
                
                    os.system('cls')
                    print('Berhasil memasukkan data dalam file')
            elif choose2 == 2: #jika choose2 = 2
                exit() #keluar dari program
        except IOError: #error handling saat terjadi IOError
            exit()
        except ValueError: #error handling jika terjadi ValueError
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3)
            FateGrandOrder()

def FateGrandOrder():
    os.system('cls')
    print('Welcome to Fate Grand Order Wiki')
    for i in fgoSuccess: #melooping list dari API
        print(i['name']) #print list dari nama di dalam API
    print('Pilih info character yang ingin dilihat')
    choose = str(input('Input name: ')) #input string 
    fago = Character(choose) #inisialisai class dengan parameter
    fago.info() #memanggil fungsi info di dalam class FateGrandOrder
    fago.infoTxt() #memanggil fungsi infoTxt di dalam class FateGrandOrder