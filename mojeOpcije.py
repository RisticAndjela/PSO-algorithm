import math
class mojeOpcije:
    def __init__(self):
        self.broj_cestica = 34
        self.broj_iteracija = 50
        self.cbi = 2.5      # Početna vrednost faktora ubrzanja za individualno najbolje rešenje.
        self.cbf = 0.5      # Konačna vrednost faktora ubrzanja za individualno najbolje rešenje.
        self.cgi = 0.5      # Početna vrednost faktora ubrzanja za globalno najbolje rešenje.
        self.cgf = 2.5      # Konačna vrednost faktora ubrzanja za globalno najbolje rešenje.
        self.pocetni_iner_faktor = 0.9            # Početna vrednost inercijalnog faktora.
        self.konacni_iner_faktor = 0.4            # Konačna vrednost inercijalnog faktora.
        self.max_brzina = math.inf     # Apsolutno ograničenje brzine. To je primarno ograničenje brzine.
        self.max_brzina_relativna = float('nan')   # Relativno ograničenje brzine. Koristi se samo ako apsolutno ograničenje nije specificirano.
        self.pocetni_opseg_brzine = 1        # Početni opseg brzine. Početne brzine se inicijalizuju
        self.pocetna_populacija = float('nan') 
        self.pocetni_pomeraj = 0       # Pomeraj početne populacije.
        self.raspon_pocetne_populacije = 1         # Raspon početne populacije.
        self.poverenje_u_pomeraj = 0      # Ako je postavljeno na 1 (istina) i pomeraj je vektor, tada se smatra da je pomeraj dobro rešenje, pa se uključuje u početno jato.
        self.dimenzija = 60