from tkinter import *
from CNF import convert_CFG2CNF
from AlgorithmCYK import algorithm

#suara burung gagak itu membuat suasana malam mencekam

def clearFrame():
  for widget in UI.frame_table.winfo_children():
    widget.destroy()
  UI.frame_table.pack_forget()

def handle_click(): # Jika tombol cek ditekan
  clearFrame()
  str_terminal = 1
  if UI.txt_user.get() != "": # Program akan mengeksekusi jika terdapat string inputan
    str = UI.txt_user.get()
    cnf = convert_CFG2CNF() # Mendapatkan hasil dari konversi CFG ke CNF
    terminal = [] # Untuk menampung simbol dari Σ
    for i in cnf.keys(): # Untuk mendapatkan Σ dari CNF
      for j in cnf[i]:
        for k in j.split():
          if k not in cnf.keys() and k not in terminal:
            terminal.append(k)
    str = str.lower()
    string = str.split()
    handle_click.lenght = len(string) # Mendapatkan panjang string untuk batas table filling
    for i in string: # Untuk mengecek input-an user
      if i not in terminal: # Apakah terdapat simbol diluar Σ
        str_terminal = 0
        UI.hasil["text"] = "String yang Anda masukkan terdapat diluar Terminal!"  # Menaruh teks ke label hasil
    if str_terminal == 1:
      handle_click.table = algorithm(cnf, string) # Untuk table filling
      tabel()  # Untuk mencetak tabel
      for i in handle_click.table[0][handle_click.lenght-1]:  # Untuk cek string valid atau tidak
        valid = 0
        if i == "K":
          valid = 1
          UI.hasil["text"] = f"String {str} valid!" # Menaruh teks ke label hasil
          break
      if valid != 1:  # Jika string tidak valid
        UI.hasil["text"] = f"String {str} tidak valid!" # Menaruh teks ke label hasil

def tabel():
  for i in range(handle_click.lenght):  # Untuk baris pada tabel
    k = 0 # Untuk jumlah kolom pada tabel dan baris pada tabel CYK
    for j in range(handle_click.lenght - i - 1, handle_click.lenght): # Untuk kolom pada tabel CYK
      frame = Frame(  # Membuat frame di dalam frame table
        master=UI.frame_table,
        relief=RAISED,
        borderwidth=5
      )
      frame.grid(row=i, column=k) # Mengisi baris i kolom k
      label = Label(master=frame, text=handle_click.table[k][j], font=('Yu Gothic UI',7), width=25)
      label.pack()  # Menaruh label ke dalam grid frame [i][k]
      k+=1

def UI():
  #membuat gui tampil
  UI.root = Tk()
  UI.root.title("Program Parsing")
  UI.root.geometry("800x800+100+50")

  #membuat frame
  frame_login = Frame(UI.root,bg="white", highlightbackground="silver", highlightcolor="silver", highlightthickness=5)
  frame_login.place(height=300, width=1500)
  UI.frame_table = Frame(UI.root, bg="white", highlightbackground="silver", highlightcolor="silver", highlightthickness=5)
  UI.frame_table.place(y=300, height=500, width=1500)

  #membuat judul tampil
  title = Label(frame_login, text="Aplikasi Parsing", font=('Bulletto Killa¬',20),
                fg="#000000", bg= "white").place(x=290, y=30)

  #Lable
  str_input = Label(frame_login, text="Masukan kalimat", font=('Bulletto Killa¬',15),
              fg="#000000", bg= "white").place(x=40, y=110)
  UI.txt_user = Entry(frame_login,font=('Yu Gothic UI',10), bg="#E7F6F2")
  UI.txt_user.place(x=250, y=110, width=500, height=30)

  #Lable
  str_hasil = Label(frame_login, text="Hasil", font=('Bulletto Killa¬',15),
              fg="#000000", bg= "white").place(x=145, y=170)
  UI.hasil = Label(frame_login, font=('Yu Gothic UI',10), bg="#E7F6F2")
  UI.hasil.place(x=250, y=170, width=500, height=30)

  button = Button(frame_login, text="Cek", font=('Bulletto Killa¬',15),
          fg="#000000", bg= "white", command=handle_click).place(x=380, y=230)

  UI.root.mainloop()

if __name__ == "__main__":
  UI()