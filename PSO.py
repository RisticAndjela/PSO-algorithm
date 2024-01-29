import numpy as np
from Error import *
from Cestica import * 

class PSO():
    def __init__(self,broj_dimenzija,opcije):
        fitnes_najbolja_g=-1                   # globalno najbolji fintes
        poz_najbolja_g=[]                      # globalno najbolja pozicija

        broj_iteracija=opcije.broj_iteracija 
        broj_cestica=opcije.broj_cestica  
        populacija=[]  # sve cestice
        if ((~np.isnan(opcije.pocetna_populacija)).all()):  # da li postoji inicijalna populacija koja nije NaN
            b=np.shape(opcije.pocetna_populacija)   
            if(np.size(b)==1):
                pno=b[0]
                pdim=60
            if (pno!=opcije.broj_cestica or (pdim!=opcije.dimenzija)):  # dimenzija za ovaj projekat mora biti 60
                 raise Error("Format početne populacije nije u skladu sa željenom populacijom")
            populacija=opcije.pocetna_populacija; 
        else:            
            for i in range(0,broj_cestica):
                x0= (np.random.rand(broj_dimenzija,1)-0.5)*2*opcije.raspon_pocetne_populacije + opcije.pocetni_pomeraj
                populacija.append(Cestica(x0,broj_dimenzija,opcije))

        
        # Petlja optimizacije
        i=0
        while i < broj_iteracija:
            for j in range(0,broj_cestica):
                populacija[j].izracunaj()

                if populacija[j].fitnes_i < fitnes_najbolja_g or fitnes_najbolja_g == -1:
                    poz_najbolja_g=list(populacija[j].pozicija_i)
                    fitnes_najbolja_g=float(populacija[j].fitnes_i)

            for j in range(0,broj_cestica):
                populacija[j].azuriraj_brzinu(poz_najbolja_g,broj_iteracija,i,opcije)
                populacija[j].azuriraj_poziciju()
            i+=1

        # print final results
        print( 'Optimalna tacka:')
        print( poz_najbolja_g)
        print( 'Optimalna vrednost funkcije u toj tacki je:')
        print (fitnes_najbolja_g)
