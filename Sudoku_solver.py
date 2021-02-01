#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:00:40 2020

@author: Félix_Bommier
"""
# Ein grosser Teil des Programmes besteht darin, die Daten entsprechend
# für den Computer vorzubereiten, zu prüfen und ausszugeben.
# Das eigentliche Programm ist nur die solve()-Funktion.

import sys, time
# from S_Vorlagen import * #Zustatz

# ===== Erstellt eine Hauptliste von Zeilen-Listen ============================
def hauptliste_erstellen():
    global hauptliste, zeilen_liste
    print ("\nGib unten Zeile für Zeile deine Sudoku-Zahlen ein.")
    print ("Da, wo nichts steht gibst du einfach 0 ein.")
    print ("Trenne die Zahlen immer mit einem Komma und einem Leerzeichen(1, 2, 3...):")
    for i in range (1, 10):
        zeile = input("Zeile " + str(i) + ": ")
        zeilen_liste = zeile.split(", ") # erstellt für jede Zeile eine Liste
        hauptliste.append(zeilen_liste)  # Tut diese 9 Listen in eine Hauptliste
        
# ===== Schaut, ob es keine "Tippfehler" gibt =================================
def fehler_meldung():
    global hauptliste, fehler, Spalte
    for zeile in hauptliste:
        for zahl in zeile:
            Spalte += 1
            try:
                something = int(zahl)   # Schaut, dass es eine Zahl ist.
                if something < 0 or something > 9: # Schaut, dass die Zahl
                    fehler = True                  # zwischen 0 und 9 liegt.
            except:
                fehler = True
        if not Spalte == 9:   #Achtet darauf, dass es genug Zahlen gibt (81)
            fehler = True
        Spalte = 0

# ===== Erstellt eine Klasse für jede Zahl ====================================
class ZahlenKlasse():
    def __init__(self, wert, y_pos, x_pos):
        self.wert = int(wert)
        self.zeile = y_pos
        self.spalte = x_pos
        self.position = [y_pos, x_pos]
        if self.wert == 0: #
            self.existenz = False
        if self.wert != 0: #
            self.existenz = True
        if 0 <= y_pos <= 2: b_spalte = 1
        elif 3 <= y_pos <= 5: b_spalte = 2
        elif 6 <= y_pos <= 8: b_spalte = 3
        if 0 <= x_pos <= 2: b_zeile = 1
        elif 3 <= x_pos <= 5: b_zeile = 2
        elif 6 <= x_pos <= 8: b_zeile = 3
        self.block = [b_spalte,  b_zeile]
        
# ===== Methode, die Regeln prüft (2 Varianten: mit 0 und ohne 0) =============
# ===== mit_0 und ohne_0 machen es möglich, die Regel auf ehmalige 0 ==========
# ===== oder nur auf normale Zahlen anzuwenden. ===============================

    def regeln_bruch_0(self): # Achtet darauf, dass es die Zahl nur 1 Mal in 
        l_fehler = False     # einer Zeile [1], einer Spalte [2] oder
        for i in range (9):  # eine Block [3] gibt.
            if self.wert == hauptliste[self.zeile][i].wert and \
            self.position != hauptliste[self.zeile][i].position: # [1]
                l_fehler = True
            if self.wert == hauptliste[i][self.spalte].wert and \
            self.position != hauptliste[i][self.spalte].position: # [2]
                l_fehler = True
            for j in range (9): 
                if self.block == hauptliste[i][j].block and \
                self.position != hauptliste[i][j].position:    # [3]
                    if self.wert == hauptliste[i][j].wert:
                        l_fehler = True
        return l_fehler
    
    def regeln_bruch(self):
        l_fehler = False
        if self.existenz:
            for i in range (9):
                if self.wert == hauptliste[self.zeile][i].wert and \
                self.position != hauptliste[self.zeile][i].position: # [1]
                    l_fehler = True
                if self.wert == hauptliste[i][self.spalte].wert and \
                self.position != hauptliste[i][self.spalte].position: # [2]
                    l_fehler = True
                for j in range (9): 
                    if self.block == hauptliste[i][j].block and \
                    self.position != hauptliste[i][j].position:    # [3]
                        if self.wert == hauptliste[i][j].wert:
                            l_fehler = True
        return l_fehler

# ===== Kern des Programmes, löst das Sudoku ==================================
def solve():
    global hauptliste
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            zaehler = True   
            if not hauptliste[i][j].existenz:
                hauptliste[i][j].wert += 1
                while hauptliste[i][j].regeln_bruch_0():
                    hauptliste[i][j].wert += 1
                if hauptliste[i][j].wert > 9:
                    zaehler = False
                    hauptliste[i][j].wert = 0
                    if j != 0:
                        j -= 1
                    else:
                        j = 8
                        i -= 1
                    while hauptliste[i][j].existenz:
                        if j != 0:
                            j -= 1
                        else:
                            j = 8
                            i -= 1

            if zaehler: j += 1
        i += 1
        
# ===== Stellt das Ergebnis schön dar =========================================
def ausgeben():
    global hauptliste
    for zeile in hauptliste:
        for i in zeile:
            print (i.wert, end = ", ")
        print ()

# ===== Hauptprogramm =========================================================
hauptliste = []
fehler = False
Spalte = 0
logik_fehler = 0
# """
hauptliste_erstellen() #Erstellt mit input alle Listen und tut sie in Hauptliste
fehler_meldung() #Schaut bei jedem String, ob es nicht den Normen entspricht

if fehler == True:  #Lässt Programm abbrechen, falls es äusere Fehler  gibt
    print ("\nEin Fehler ist aufgetaucht!", end = "\n\n")
    sys.exit()
# """    
# hauptliste = S_other_0 #Zustatz
for i in range (9):                         #*********************************
    for j in range (9):                     # Nimmt jede Zahl aus der Liste
        wert = hauptliste[i][j]             # heraus, erstellt dafür eine
        del hauptliste[i][j]                # Instanz der ZahlenKlasse und
        instanz = ZahlenKlasse(wert, i, j)  # tut diese am selben Ort hinein
        hauptliste[i].insert(j, instanz)    #*********************************
        
for zeile in hauptliste:           #******************************************
    for element in zeile:          # Schaut für jede Instanz, ob es keine 
        if element.regeln_bruch(): # Logikfehler gibt, damit es lösbar ist
            logik_fehler += 1      #******************************************
            
if logik_fehler > 0:  #Lässt Programm abbrechen, falls es Logik-Fehler  gibt
    print ("\nDas Sudoku ist unlösbar!", end = "\n\n")
    sys.exit()
    
print ("\nDer Computer rechnet...")

start = time.time()
solve() #Kern des Programmes
end = time.time()

print ("\nGelöstes Sudoku:")
ausgeben() #Schreibt die Liste schön auf

print ("\nBenötigte Zeit:", end = " ")
print (end - start)

print("\nFertig!")
