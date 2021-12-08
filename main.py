from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.geometry("590x600")
pencere.config(bg= "black")

baslik = Label(pencere, text="Görseller", bg="black", fg= "#DBD034")
baslik.grid(row=0, column=1, padx= 10, pady=10)
baslik.config(font=("Times New Roman", 30))

kapaklar = ["foto1.jpg", "foto2.jpg","foto3.jpg","foto4.jpg", "foto5.jpg"]
yazilar = ["Duvar Kağıdı","Merdivenler","Hacivat ile Karagöz", "Gökyüzü","Lucifer"]
yazi = 0
kapak = 0

def goster():
    basewidth = 300
    gorsel = Image.open(kapaklar[kapak])
    wpercent = (basewidth / float(gorsel.size[0]))
    hsize = int((float(gorsel.size[1]) * float(wpercent)))
    gorsel = gorsel.resize((basewidth, hsize), Image.ANTIALIAS)
    gorsel.save(kapaklar[kapak])
    gorsel = ImageTk.PhotoImage(Image.open(kapaklar[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=1, padx= 5, pady=5)


goster()

def yazigoster():
    yazim = (yazilar[yazi])
    yaziEntry = Label(pencere, text=yazim, font=("Times New Roman", 10), bg = "black", fg= "#DBD034", width=40)
    yaziEntry.grid(row=2, column=1, padx=5, pady=5)


yazigoster()

def fotosonraki():
    global kapak
    if kapak < len(kapaklar)-1:
        kapak +=1
    else:
        kapak = 0
    print(kapak)
    goster()

def fotoonceki():
    global kapak
    if kapak < len(kapaklar) + 1:
        kapak -= 1
    else:
        kapak = 0
    print(kapak)
    goster()

def yazisonraki():
    global yazi
    if yazi < len(yazilar) - 1:
        yazi += 1
    else:
        yazi = 0
    yazigoster()


def yazionceki():
    global yazi
    if yazi < len(yazilar) + 1:
        yazi -= 1
    else:
        yazi = 0
    yazigoster()


ileributon = Button(text="İleri", command=lambda:[yazisonraki(), fotosonraki()])
geributon = Button(text= "Geri", command=lambda:[yazionceki(), fotoonceki()])
geributon.grid(row=2, column=2, padx= 5, pady=5)
geributon.config(font=("Times New Roman", 20))
ileributon.grid(row=2, column=0, padx= 5, pady=5)
ileributon.config(font=("Times New Roman", 20))
cikisbuton = Button(text= "Çıkış Yapmak İçin Tıklayınız.", command= pencere.destroy)
cikisbuton.grid(row=0, column=0, padx= 5, pady=5)
pencere.mainloop()

