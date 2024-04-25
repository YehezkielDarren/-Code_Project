def Pesanan(total_pesanan:list,baru:list):
    if len(total_pesanan)==0:
        total_pesanan.append(baru)
    else:
        for i in range(len(total_pesanan)):
            if total_pesanan[i][0]==baru[0]:
                for y in range(len(total_pesanan[i][1])):
                    if y%2==0 and total_pesanan[i][1][y]==baru[1][0]:
                        total_pesanan[i][1][y+1]+=baru[1][1]
                        break
                else:
                    total_pesanan[i][1]+=baru[1]
                break
        else:
            total_pesanan.append(baru)
    return total_pesanan

def TambahMakanan():
    lst=[]
    lst1=[]
    nama=input("Nama Pemesan (Nama Lengkap) >> ")
    menu=input("Menu yang Diorder >> ").lower()
    jumlahPesanan=int(input(f"Jumlah pesanan '{menu}' >> "))
    print()
    lst1.append(menu), lst1.append(jumlahPesanan), lst.append(nama), lst.append(lst1)
    return lst #mengembalikan nilai ["nama",["menu",total pesanan]]

def MelihatPesanan(arr:list):
    index=1
    lihat_data=input("Masukkan nama pemesannya (sesuai dengan awal pesan) >> ")
    for i in range(len(arr)):
        if arr[i][0]==lihat_data:
            print("======================")
            print(f"Nama Pemesan >> {arr[i][0]}")
            print("Menu >> ")
            for menu in range(len(arr[i][1])):
                if menu%2==0:
                    print(f"\tMenu {index} >> {arr[i][1][menu]}")
                    print(f"\tJumlah pesanan >> {arr[i][1][menu+1]}")
                    index+=1
            print("======================")
            break
    else:
        print("======================")
        print("Data Tidak di Temukan")
        print("======================")

def main():
    data_base=[]
    yes_no=["Y","N"]
    while True:
        print("=====================")
        print("1. Pesan Makanan")
        print("2. Melihat Pesanan")
        print("3. Exit")
        print("=====================")
        try:
            option=int(input("Pilih 1-3 >> "))
        except ValueError:
            print("Opsi Hanya Berbentuk Angka")
            continue
        else:
            if option==1:
                while True:
                    try:
                        tambah=TambahMakanan()
                        Pesanan(data_base,tambah)
                    except ValueError:
                        print("=====================")
                        print("Anda tidak mengisi semuanya, Ulangi!!")
                        print("=====================")
                    else:    
                        print("Pesanan telah di update")
                        print()
                        lanjut_=input("Apakah ingin lanjut ? (Y/N) ").upper()
                        if lanjut_==yes_no[0]:
                            continue
                        else:
                            break
                        
            elif option==2:
                MelihatPesanan(data_base)
            elif option==3:
                print("Terima Kasih")
                break
            else :
                print("Opsi hanya 1-3, Ulangi !!")
                continue

main()


