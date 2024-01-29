import numpy as np
import random as random
from ann_criterion import optimality_criterion


class Cestica:
    def __init__(self, x0, broj_dimenzija, opcije):
        #x0: Početna pozicija čestice (2D niz)
        self.pozicija_i = []          # Pozicija čestice
        self.brzina_i = []            # Brzina čestice
        self.poz_najbolja_i = []          # Najbolja pozicija individualne čestice
        self.fitnes_najbolja_i = -1       # Najbolji fitness individualne čestice
        self.fitnes_i = -1            # Fitnes individualne čestice
        self.broj_dimenzija = broj_dimenzija

        # Inicijalizuj pozicije i brzine
        for i in range(0, broj_dimenzija):
            self.brzina_i.append((np.random.rand() - 0.5) * 2 * opcije.pocetni_opseg_brzine)
            self.pozicija_i.append(x0[i][0])
            
            
            
    # izračunaj trenutni fitnes i računanje novih najboljih individualnih vrednosti
    def izracunaj(self,funkcija=optimality_criterion):
        self.fitnes_i = funkcija(self.pozicija_i)
        if self.fitnes_i < self.fitnes_najbolja_i or self.fitnes_najbolja_i == -1:
            self.poz_najbolja_i = self.pozicija_i
            self.fitnes_najbolja_i = self.fitnes_i

    def lin_stopa(self, xmax, xmin, tmax, tmin, t):
        x = xmin + ((xmax - xmin) / (tmax - tmin)) * (tmax - t)
        return x

    def azuriraj_brzinu(self, poz_najbolja_g, maxiter, iter, opt):
        w = self.lin_stopa(opt.konacni_iner_faktor, opt.pocetni_iner_faktor, maxiter, 0, iter)
        cp = self.lin_stopa(opt.cbf, opt.cbi, maxiter, 0, iter)
        cg = self.lin_stopa(opt.cgf, opt.cgi, maxiter, 0, iter)

        for i in range(0, self.broj_dimenzija):
            r1 = random.random()
            r2 = random.random()
            vel_cognitive = cp * r1 * (self.poz_najbolja_i[i] - self.pozicija_i[i])
            vel_social = cg * r2 * (poz_najbolja_g[i] - self.pozicija_i[i])
            self.brzina_i[i] = w * self.brzina_i[i] + vel_cognitive + vel_social

    def azuriraj_poziciju(self):
        for i in range(0, self.broj_dimenzija):
            self.pozicija_i[i] = self.pozicija_i[i] + self.brzina_i[i]
