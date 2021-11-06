from PIL import Image  # Python Imaging Library
import numpy as np

# ---------- wczytywanie obrazu zapisanego w różnych formatach .bmp, .jpg, .png oraz pobieranie informacji o obrazie  -------------------
obrazek = Image.open("jd.bmp")  # wczytywanie obrazu
# obrazek.show()
print("typ", obrazek.mode)
print("format", obrazek.format)
print("rozmiar", obrazek.size)

obrazek2 = Image.open("jd.jpg")  # wczytywanie obrazu
# obrazek.show()
print("typ", obrazek2.mode)
print("format", obrazek2.format)
print("rozmiar", obrazek2.size)

obrazek3 = Image.open("jd.png")  # wczytywanie obrazu
# obrazek.show()
print("typ", obrazek3.mode)
print("format", obrazek3.format)
print("rozmiar", obrazek3.size)

# ---------- wczytywanie obrazu do tablicy oraz pobieranie informacji o tablicach ------------------------------
dane_obrazka = np.asarray(obrazek)
print("typ danych tablicy", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy", dane_obrazka.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka
print("liczba elementow", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("wymiar wyrazu tablicy",
      dane_obrazka.itemsize)  # pokazuje ile współrzednych trzeba do opisania wyrazu tablicy (piksela)
print("pierwszy wyraz", dane_obrazka[0][0])
print("drugi wyraz", dane_obrazka[1][0])
print("***************************************")
# print(dane_obrazka)   # mozna odkomentować, zeby zobaczyć tablicę

dane_obrazka2 = np.asarray(obrazek2)
print("typ danych tablicy", dane_obrazka2.dtype)
print("rozmiar tablicy", dane_obrazka2.shape)
print("liczba elementow", dane_obrazka2.size)
print("wymiar tablicy", dane_obrazka2.ndim)
print("wymiar elementu tablicy", dane_obrazka2.itemsize)
print("pierwszy element", dane_obrazka2[0][0])
print("drugi element", dane_obrazka2[1][0])
# print(dane_obrazka2)

dane_obrazka3 = np.asarray(obrazek3)
print("typ danych tablicy", dane_obrazka3.dtype)
print("rozmiar tablicy", dane_obrazka3.shape)
print("liczba elementow", dane_obrazka3.size)
print("wymiar tablicy", dane_obrazka3.ndim)
print("wymiar elementu tablicy", dane_obrazka3.itemsize)
print("pierwszy element", dane_obrazka3[0][0])
print("drugi element", dane_obrazka3[1][0])
# print(dane_obrazka3)

# ------------------------   wczytywanie obrazu do tablicy z jednoczesnym okresleniem typu danych ---------------------
dane_obrazka1_rob = dane_obrazka * 1  # zmienia typ bool na int
dane_obrazka1 = np.array(dane_obrazka1_rob,
                         dtype='uint8')  # wczytanie tablicy jako uint8 czyli z danymi w zakresie od 0 do 255
# print(dane_obrazka1)

ob_d = Image.fromarray(dane_obrazka)  # tworzenie obrazu z tablicy dane_obrazka (typ bool)
# ob_d.show()

ob_d1 = Image.fromarray(dane_obrazka1)  # tworzenie obrazu z tablicy dane_obrazka1 (typ uint8)
# ob_d1.show()  # dlaczego obraz jest czarny? Nie jest, jest normalny.

dane_obrazka2 = np.array(dane_obrazka1, dtype='bool').astype(
    np.uint8)  # zamiana tablicy zero-jedynkowej (typ uint8) na typ bool
ob_d2 = Image.fromarray(dane_obrazka2)
# ob_d2.show()

dane_obrazka3 = dane_obrazka * 255  # zamiana tablicy na typ uint8 przy czmy obraz będzie typu L - odcienie szarosci , czarny = 0, biały = 255
print(dane_obrazka3.shape)
ob_d3 = Image.fromarray(dane_obrazka2)
# ob_d3.show()

# assert False
## ----- wyswietlanie informacji o obrazie -----------------------------
print("typ", ob_d.mode)
print("format", ob_d.format)
print("rozmiar", ob_d.size)

print("typ1", ob_d1.mode)
print("format1", ob_d1.format)
print("rozmiar1", ob_d1.size)

print("typ2", ob_d2.mode)
print("format2", ob_d2.format)
print("rozmiar2", ob_d2.size)

print("typ3", ob_d2.mode)
print("format3", ob_d2.format)
print("rozmiar3", ob_d2.size)

# wczytywanie tablicy z pliku UWAGA! plik txt powinien zawierac same zera i jedynki oddzielane spacjami bez dodatkowych znaków jak w pliku dane.txt
t1 = np.loadtxt("obrazek.txt", dtype=np.bool_)
t2 = np.loadtxt("obrazek.txt", dtype=np.int_)
t3 = t2 * 255
# w zależnosci od tego, jakie operacje chcemy zrobić na tablicy, wybieramy jedną z powyższych postaci tablicy

# ---- porównywanie tablic ------
nowa_t1 = np.loadtxt("obrazek.txt", dtype=np.bool_)  # wczytanie tablicy z pliku dane1.txt
h, w = nowa_t1.shape
print("wymiary tablicy ", h, w)
nowa_t1_1 = nowa_t1 * 1  # zamiana bool na tablice zero-jedynkową
porownanie = nowa_t1 == nowa_t1_1  # zwraca TRUE jesli tablice są identyczne (przy czym True = 1, False = 0), w przeciwnym przypadku False
czy_rowne = porownanie.all()
print(czy_rowne)


# wersja "ręczna"
def sprawdz_czy_rowne(tab1, tab2):
    odpowiedz = True
    if tab1.shape != tab2.shape:
        odpowiedz = False
        print("tablice maja różne rozmiary")
    else:
        for i in range(h):
            for j in range(w):
                if tab1[i][j] != tab2[i][j]:
                    odpowiedz = False
    return odpowiedz


print("sparwdz czy są równe ", sprawdz_czy_rowne(nowa_t1, nowa_t1_1))

print("------ drugi przykład -------------------")
nowa_t2 = np.loadtxt("obrazek.txt", dtype=np.int_)  # wczytanie tablicy z pliku dane1.txt
print(nowa_t2)
print("--------------")
print(t2)
porownanie = t2 == nowa_t2  # tablica, która ma wartośc True jesli elementy w odpowieednich miejscach sa równe i False w p.p.
print(porownanie)
czy_rowne = porownanie.all()
print(czy_rowne)

# zliczanie równych elementów
print(np.sum(t2 == nowa_t2))  # zlicza ile elementów jest takich samych

# ---------------- zapisywanie obrazu do pliku -----------------
ob_d.save(
    "obraz_zapisany.bmp")  # jako argument podajemy nazwę pliku wraz z rozszerzeniem, bo w zależności od tego w jakim formacie zapiszemy otrzymamy różne tablice obrazu

input()
"""

# programowanie tablic
def rysuj_ramke(w, h, dzielnik):
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = 1  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
    return tab * 255


tab = rysuj_ramke(120, 60, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()

def rysuj_pasy_poziome(w, h, dzielnik): # w, h   -  rozmiar obrazu
    t = (h, w)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)
    # jaki bedzie efekt, gdy np.ones zamienimy na np.zeros?
    grub = int(h / dzielnik)  # liczba pasów = 9 o grubości 10
    print(grub)
    for k in range(dzielnik):  # uwaga k = 0,1,2,3,4,5,8   bez dziewiatki
        for g in range(grub):
            i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for j in range(w):
                tab[i, j] = k % 2  # reszta z dzielenia przez dwa
    tab = tab * 255
    obraz = Image.fromarray(tab)  # tworzy obraz
    obraz.show()
rysuj_pasy_poziome(400, 630, 9)
"""


# wjebalem to do docstringa zeby bylo xD


# dobra, to tera tak


def compute_ramka(w, h, dzielnik=8):
    grubosc_ramki = int(min(w, h) / dzielnik)
    tab = np.zeros((h, w), dtype=np.uint8)
    potrzymaj_h = h
    potrzymaj_w = w
    flip = True
    for i in range(int(w/grubosc_ramki)):
        print(f"iterating on {i=}, gdzie {grubosc_ramki=}")
        z1 = potrzymaj_h - grubosc_ramki
        z1s = grubosc_ramki + h - potrzymaj_h
        z2 = potrzymaj_w - grubosc_ramki
        z2s = grubosc_ramki + w - potrzymaj_w
        tab[z1s:z1, z2s:z2] = int(flip)
        flip = not flip
        potrzymaj_h -= grubosc_ramki * 2
        potrzymaj_w -= grubosc_ramki * 2
    return tab * 255

# TODO: Sprwadz logike, bo cos mi tu nie gra, w sensie te min(w,h)/2 to sraka i strasznie gruba ta linia wychodzi
# TODO: W sensie, w przykladzie jest podany dzielnik 8, co da grubosc 100, czyli z obrazka 800x800,
# TODO:  wpierdala 200 pixeli na iteracje czarnego, przez co tylko dwie czarne iteracje są i powstaje okropna kropa na srodku.

#to sobie odkomentuj, powinno dzialac z bomby.
'''
Pokazywanie ramki w ramce :V logika na flipa,
 mozna jeszcze funkcją matematyczną wyciąć białe z czarnego,
 ale to chlop by sie za glowe zlapal o co tu chodzi.
 
 Ogolnie cos zjebalem, ale dziala XD
 sprawdze jeszcze poza pociągiem, bo troche rozskupienie
'''

#Image.fromarray(compute_ramka(1440,200,8)).show()



def compute_kreseczki(w,h,dzielnik = 8):
    grubosc_kreski = int(w/dzielnik)
    tab = np.zeros((h,w),dtype="uint8")
    flip = False
    for i in range(int(w/grubosc_kreski)):
        tab[0:h, i*grubosc_kreski:w] = int(flip)
        flip = not flip
    return tab * 255

#Image.fromarray(compute_kreseczki(1440,900,16)).show()



# TODO: To samo co wyzej, jak chcesz to Ci opisze o co cho, ale pewnie trzeba fine-tuning tego gowna zrobic, bo na kolanie w pociagu pisane XD

'''

Ogolnie jak lubisz elektronike, to polecam  apollo 440 - the future's what it used to be.
                                            the prodigy - the day is my enemy
                                            the prodigy - thunder
                                            pendulum - witchcraft
                                            infected mushroom - the messanger 2012
                                            XD
'''
#podejscie manualne
def compute_pointcross(w,h,x,y):
    tab = np.zeros((h,w),dtype = "uint8")
    #color q1 top left
    tab[0:y , 0:x] = 1
    #color q2 top right
    tab[0:y, x:w] = 0
    #color q3 bot left
    tab[y:h, 0:x] = 0
    #color q4 bot right
    tab[y:h, x:w] = 1
    return tab * 255
#podejscie skalowalne
def scalable_compute_pointcross(w,h,x,y):
    tab = np.zeros((h,w),dtype="uint8")
    for i in range(2):
        for j in range(2):
            #tab[] = 1
            print(tab)

    return tab * 255

#Image.fromarray(scalable_compute_pointcross(150,150,70,70)).show()
Image.fromarray(compute_pointcross(150,150,70,70)).show()