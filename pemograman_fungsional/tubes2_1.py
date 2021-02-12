#import pandas untuk meload data csv di program
import pandas as pd
#import os untuk membuat fungsi clear screen dalam python
import os
#import matplotlib untuk menampilkan grafik di program
import matplotlib.pyplot as plt
#variabel data csv yang di impor menggunakan pandas
data_covid_csv = pd.read_csv('covid_19_indonesia_time_series_all.csv', delimiter=',')

case_per_day = data_covid_csv.groupby("Date").TotalCases.sum().reset_index()
data_covid_dict = case_per_day.to_dict('Records')
data_dict = list(filter(lambda x: x['Date'] == 1, data_covid_dict))
result = pd.DataFrame.from_dict(data_dict)
print(result)

case_per_day = data_covid_csv.groupby("Location").TotalDeaths.max().reset_index()
data_covid_dict = case_per_day.to_dict('Records')
data_dict = list(sorted(data_covid_dict, key=lambda x: x['TotalDeaths'], reverse=True))
result = pd.DataFrame.from_dict(data_dict)
print(result)

case_per_day = data_covid_csv.groupby("Date").TotalDeaths.sum().reset_index()
case_per_day_dict = case_per_day.to_dict('Records')
Date = list(map(lambda x: x.get('Date'), case_per_day_dict))
mean = list(map(lambda x: x.get('TotalDeaths'), case_per_day_dict))
# grafik matplotlib
ax = plt.subplot()
plt.xlabel("tanggal (Januari)")
plt.ylabel("jumlah kasus")
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
plt.plot(Date, mean)
plt.show()
#%%
#import pandas untuk meload data csv di program
import pandas as pd
#import os untuk membuat fungsi clear screen dalam python
import os
#import matplotlib untuk menampilkan grafik di program
import matplotlib.pyplot as plt
#variabel data csv yang di impor menggunakan pandas
df = pd.read_csv('covid_19_indonesia_time_series_all.csv', delimiter=',')

#membuat fungsi menu, untuk menampilkan menu di awal program
def menu():
    clear_screen()
    print("APLIKASI CEK DATA COVID-19 INDONESIA JANUARI 2021")
    print("1. CEK KASUS COVID-19 (filter(lambda))")
    print("2. CEK URUTAN KASUS COVID-19 (sorted(lambda))")
    print("3. CEK GRAFIK KASUS COVID-19 (map(lambda))")
    #membuat variabel inputan untuk user
    selected_menu = input("PILIH MENU : ")
#pengkondisian menggunakan if,else dan elif
    if selected_menu == "1":
        #jika user memasukan inputan 1, maka program akan mengeksekusi fungsi cari_data
        cari_data()
    elif selected_menu == "2":
        #jika user memasukan inputan 2, maka program akan mengeksekusi fungsi urutan_data
        urutkan_data()
    elif selected_menu == "3":
        #jika user memasukan inputan 3, maka program akan mengeksekusi fungsi grafik_data
        grafik_data()
        exit()
    else:
        #jika inputan tidak sesuai, maka program akan otomatis mengeksekusi fungsi kembali_ke_menu
        print("PILIHAN MENU SALAH!")
        kembali_ke_menu()
#membuat fungsi kembali_ke_menu untuk mengeksekusi fungsi menu
def kembali_ke_menu():
    print("\n")
    input("TEKAN ENTER UNTUK KEMBALI KE MENU")
    menu()
#membuat fungsi clear_screen untuk menghapus output yang sebelumnya ditampilkan ke user
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#membuat fungsi cari_data yang di eksekusi dalam pilihan menu 1
def cari_data():
    clear_screen()
    print("CEK KASUS BERDASARKAN :")
    print("1. TANGGAL (JANUARI)")
    print("2. PROVINSI")
    #membuat variabel inputan untuk user
    sub_menu = input("PILIH MENU : ")
    pilihan = input("MASUKAN DATA : ")
    if sub_menu == "1":
        #membuat variabel kolom untuk mengambil kolom date dan kolom TotalCases
        kolom = df.groupby("Date").TotalCases.sum().reset_index()
        #membuat variabel dict untuk merubah tipe data dataframe menjadi dictionary
        dict = kolom.to_dict('Records')
        #membuat variabel fungsi filter,lambda yang berfungsi untuk mengakses dictionary pada variabel dict
        fungsi = list(filter(lambda x: x['Date'] == int(pilihan), dict))
        #membuat variabel hasil yang berfungsi merubah tipe data dictionary ke dataframe supaya mudah dibaca user
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)

    elif sub_menu == "2":
        #membuat variabel lokasi untuk mengambil kolom lokasi dan kolom TotalCases
        lokasi = df.groupby("Location").TotalCases.max().reset_index()
        #membuat variabel dict untuk merubah tipe data dataframe menjadi dictionary
        dict = lokasi.to_dict('Records')
        #membuat variabel fungsi filter,lambda yang berfungsi untuk mengakses dictionary pada variabel dict
        fungsi = list(filter(lambda x: x['Location'] == pilihan, dict))
        #membuat variabek hasil yang berfungsi merubah tipe data dictionary ke dataframe supaya mudah dibaca user
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    kembali_ke_menu()

#---------------------------------------------------------------------------------------------
#membuat fungsi urutan_data yang dieksekusi pada pilihan menu 2
def urutkan_data():
    clear_screen()
    print("URUTAN DATA BERDASARKAN :")
    print("1. TOTAL KEMATIAN")
    print("2. TOTAL KESEMBUHAN")
    print("3. TOTAL KASUS")
    #membuat variabel inputan
    sub_menu = input("PILIH MENU : ")
    if sub_menu == "1":
        # membuat variabel lokasi untuk mengambil kolom date dan kolom TotalDeaths
        lokasi = df.groupby("Location").TotalDeaths.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(sorted(dict, key=lambda x: x['TotalDeaths'], reverse=True))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    elif sub_menu == "2":
        # membuat variabel lokasi untuk mengambil kolom date dan kolom TotalCases
        lokasi = df.groupby("Location").TotalRecovered.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(sorted(dict, key=lambda x: x['TotalRecovered'], reverse=True))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    elif sub_menu == "3":
        # membuat variabel lokasi untuk mengambil kolom date dan kolom TotalCases
        lokasi = df.groupby("Location").TotalCases.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(sorted(dict, key=lambda x: x['TotalCases'], reverse=True))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    kembali_ke_menu()

#-----------------------------------------------------------------------------------------
def grafik_data():
    clear_screen()
    print("LIHAT GRAFIK :")
    print("1. KEMATIAN")
    print("2. KESEMBUHAN")
    print("3. TOTAL KASUS")
    print("4. PENAMBAHAN KASUS PERHARI")
    sub_menu = input("PILIHAN MENU : ")
    if sub_menu == "1":
        kolom = df.groupby("Date").TotalDeaths.sum().reset_index()
        dict = kolom.to_dict('Records')
        date = list(map(lambda x: x.get('Date'), dict))
        death = list(map(lambda x: x.get('TotalDeaths'), dict))
        # grafik matplotlib
        ax = plt.subplot()
        plt.xlabel("tanggal (Januari)")
        plt.ylabel("jumlah kasus")
        plt.title("Grafik Jumlah Kematian Covid-19")
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        plt.plot(date, death)
        plt.show()
    elif sub_menu == "2":
        kolom = df.groupby("Date").TotalRecovered.sum().reset_index()
        dict = kolom.to_dict('Records')
        date = list(map(lambda x: x.get('Date'), dict))
        sembuh = list(map(lambda x: x.get('TotalRecovered'), dict))
        # grafik matplotlib
        ax = plt.subplot()
        plt.xlabel("tanggal (Januari)")
        plt.ylabel("jumlah kasus")
        plt.title("Grafik Jumlah Kesembuhan Covid-19")
        ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
        plt.plot(date, sembuh)
        plt.show()
    elif sub_menu == "3":
        kolom = df.groupby("Date").TotalCases.sum().reset_index()
        dict = kolom.to_dict('Records')
        date = list(map(lambda x: x.get('Date'), dict))
        kasus = list(map(lambda x: x.get('TotalCases'), dict))
        # grafik matplotlib
        ax = plt.subplot()
        plt.xlabel("tanggal (Januari)")
        plt.ylabel("jumlah kasus")
        plt.title("Grafik Jumlah Kasus Covid-19")
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        plt.plot(date, kasus)
        plt.show()
    elif sub_menu == "4":
        kolom = df.groupby("Date").NewCases.sum().reset_index()
        dict = kolom.to_dict('Records')
        date = list(map(lambda x: x.get('Date'), dict))
        kasus = list(map(lambda x: x.get('NewCases'), dict))
        #grafik matplotlib
        ax = plt.subplot()
        plt.xlabel("tanggal (Januari)")
        plt.ylabel("jumlah kasus")
        plt.title("Grafik Penambahan Kasus Harian Covid-19")
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        plt.plot(date, kasus)
        plt.show()
    kembali_ke_menu()

if __name__ == "__main__":
    while True:
        menu()
