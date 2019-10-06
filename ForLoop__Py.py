#ASSIGNMENT VARIABEL UNTUK BAGIAN 1
Judul1 = "BAGIAN 1"
Garis = ('-')       
Data1 = ('Loudspeaker','Televisi','Radio','Tape','Buku','Meja','Kulkas','Istri','Gelas','Handphone','Tablet','Seng')
Data2 = 'RizkyKhapidsyah'

#ASSIGNMENT VARIABEL UNTUK BAGIAN 2
Judul2 = "BAGIAN 2"

#ASSIGNMENT VARIABEL UNTUK BAGIAN 3 & 4
Judul3 = "BAGIAN 3"
kelasA = ('Rizky-KA','Eciik-KA','Rina-KA','Dina-KA','Falih-KA')
kelasB = ('Mery-KB','Bembeng-KB','Zulfan-KB','Roro-KB','Mesem-KB')
kelasC = ('Token-KC','Rahmat-KC','Maisyarah-KC','Martha-KC','Irfan-KC')
Judul4 = "BAGIAN 4"


#--------
#BAGIAN 1
#--------
#Garis merupakan variabel
#Data1 merupakan variabel
#List pada Data1 berikut sebagai iterable (Data bisa diiterasikan): 

for V1 in Garis:                                    #V1 Merupakan Variabel
    print(V1 * 25, '\n', Judul1, '\n', V1 * 25)

    for V2 in Data1:                                #V2 Merupakan Variabel
        print(V2,':',len(V2),'Karakter')
    
    print(V1 * 25,'\n' * 2)


#--------
#BAGIAN 2
#--------
#String sebagai Iterable
print(V1 * 25, '\n', Judul2, '\n', V1 * 25)

for Huruf in Data2:
    print(Huruf)

print ('\n' * 1)


#--------
#BAGIAN 3
#--------
DaftarKelas = (kelasA, kelasB, kelasC)

print(V1 * 25, '\n', Judul3, '\n', V1 * 25)

for subDaftarKelas in DaftarKelas:
    print(subDaftarKelas)

print ('\n' * 1)


#--------
#BAGIAN 4
#--------
print(V1 * 25, '\n', Judul4, '\n', V1 * 25)

for subDaftarKelas in DaftarKelas:
    print(subDaftarKelas)
    for komponenData in subDaftarKelas:
        print(komponenData)