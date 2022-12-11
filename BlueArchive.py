import requests, os, time #import module requests,os,time

students = requests.get("https://api-blue-archive.vercel.app/api/characters/students") #mengambil API arknights dari link web
studentsSuccess = students.json()#menampung API ke dalam variabel studentSuccess
studentsData = studentsSuccess['data']#menampung file Json ke dalam variabel studentData

Name,Fullname,Age,Birthday,School,Height,DamageType,ArmorType,Weapon = ',,,,,,,,,'#deklarasi variabel untuk menampung API yang akan dimasukkan ke dalam File txt


class Character:#class character
    def __init__(self, name):#Constructor
        self.name = name
    
    def info(self):
        os.system('cls')#berfungsi sebagai clear screen pada layar
        for std in studentsData: #melooping isi dari api
            if std['name'] == self.name:#cek apakah nama yang di input terdapat dalam API atau tidak
                print('Name\t\t:', std['name'])
                print('Fullname\t:', std['names']['firstName'], std['names']['lastName'])
                print('Age\t\t:', std['age'])
                print('Birthday\t:', std['birthday'])
                print('School\t\t:', std['school'])
                print('Height\t\t:', std['height'])
                print('Damage Type\t:', std['damageType'])
                print('Armor Type\t:', std['armorType'])
                print('Weapon\t\t:', std['weapon'])
                break
        else:
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3) #memberikan jeda selama 3 detik
            BlueArchive() #memangil fungsi BlueArchive

    def infoTxt(self):
        try: #error handling apakah inputan benar atau tidak
            pilih = ['1. Yes', '2. No'] #list yang berisikan yes dan no
            print('Apakah ingin menyimpan dalam file')
            for i in pilih:
                print(i) #print isi dari list
            choose2 = int(input('Masukkan pilihan : '))
            if choose2 == 1: #jika memilih choose2 = 1
                for std in studentsData: #melooping list dari API
                    if std['name'] == self.name: #mengecek apakah nama yang di input tedapat dalam api atau tidak
                        Name =  std['name']
                        Fullname =  std['names']['firstName'] + std['names']['lastName']
                        Age =  std['age']
                        Birthday =  std['birthday']
                        School =  std['school']
                        Height =  std['height']
                        DamageType =  std['damageType']
                        ArmorType =  std['armorType']
                        Weapon =  std['weapon']

                Student_Bio = ['Name\t\t:'+ Name,
                    'Fullname\t:'+ Fullname,
                    'Age\t\t:'+ Age ,
                    'Birthday\t:'+ Birthday ,
                    'School\t\t:'+ School ,
                    'Height\t\t:'+ Height ,
                    'Damage Type\t:'+ DamageType ,
                    'Armor Type\t:'+ ArmorType,
                    'Weapon\t\t:'+ Weapon ,] #variable yang di deklarasi kan sebelum nya untuk menampung data api untuk disimpan dalam file
                
                with open('C:\\Users\\Lenovo\\Documents\\Python\\PI\\UAP\\readme.txt','w') as f: #membuka file
                    f.write('\n'.join(Student_Bio)) #menulis/menimpa file dengan data dari API
                
                os.system('cls')
                print('Berhasil memasukkan data dalam file')
            elif choose2 == 2: #jika choose2 = 2
                exit() #keluar dari program
        except IOError: #error handling jika terjadi IOError
            exit()
        except ValueError: #error handling jika terjadi ValueError
            os.system('cls')
            print('Masukkan input dengan benar')
            time.sleep(3)
            BlueArchive()

def BlueArchive():
    os.system('cls')
    print('Welcome to Blue Archive Wiki')
    for i in studentsData: #melooping list dari API
        print(i['name']) #print isi dari nama dalam API
    print('Pilih info character yang ingin dilihat')
    choose = str(input('Input name: ')) #input String
    ba = Character(choose) #inisialisasi class dengan parameter
    ba.info() #memanggil fungsi info di dalam class BlueArchive
    ba.infoTxt() #memanggil fungsi infoTxt di dalama class BlueArchive