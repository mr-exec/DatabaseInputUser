import mysql.connector
import time
import  os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_mainan"
)


def insert_data(db):
    nis = int(input("Masukan NIS Anda: "))
    nama = str(input("Masukan Nama Anda: "))
    age = int(input("Masukan Umur Anda:"))
    adress = (input("Masukan Alamat Anda:"))
    val = (nis, nama, age, adress)
    cursor = db.cursor()
    sql = "INSERT INTO customers (NIS, Name, Age, Adress) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))
    #Menu kembali ke menu atau tidak --------------------------------------------------
    print("Apakah anda ingin kembali ke menu [1/0]")
    print("1. untuk kembali ke Menu semula")
    print("0. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == "1":
        show_menu(db)
    else:
        if menu == "0":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")



def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

def update_data(db):
  cursor = db.cursor()
  show_data(db)
  customer = input("pilih id customer> ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE customers SET Name=%s, Adress=%s WHERE NIS=%s"
  val = (name, address, customer)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))
  print("Apakah anda ingin kembali ke menu [1/0]")
  print("1. untuk kembali ke Menu semula")
  print("0. Untuk Keluar")
  menu = str(input("Masukan pilihan anda :"))
  if menu == "1":
      show_menu(db)
  else:
      if menu == "0":
          exit("Terima kasih")
      else:
          print("Maaf input yang anda masukan salah")



def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    nis = input("pilih Dari Nis yg mau di Delete : ")
    sql3 = "DELETE FROM customers WHERE NIS=%s"
    val3 = (nis,)
    cursor.execute(sql3, val3)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
    print("Apakah anda ingin kembali ke menu [1/0]")
    print("1. untuk kembali ke Menu semula")
    print("0. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == "1":
        show_menu(db)
    else:
        if menu == "0":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")


def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql4 = "SELECT * FROM customers WHERE NIS LIKE %s OR Name LIKE %s"
    val4 = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql4, val4)
    results = cursor.fetchall()
    print("Ini hasil pencarian anda")
    time.sleep(4)

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
    print("Apakah anda ingin kembali ke menu [1/0]")
    print("1. untuk kembali ke Menu semula")
    print("0. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == "1":
        show_menu(db)
    else:
        if menu == "0":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")

os.system("clear")

def show_menu(db):
    print("=== Selamat Mencoba ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu : ")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


print (show_menu(db))
