import time
user = ["Rafi", "Tunggul", "Lubia"]
password = ["SukaDonat", "Magerbowl", "SukaLumpia"]

while True:
    print("Silahkan Masukkan Username:")
    inputan = input()
    for x in range(len(user)):
        if inputan == user[x]:
            print("silahkan Masukkan Password:")
            inputanpassword = input()
            if inputanpassword == password[x]:
                print("Selamat anda berhasil masuk")
                exit()
            else:
                print("Password atau Username salah silahkan login kembali")
                print("")
                time.sleep(5)
                continue