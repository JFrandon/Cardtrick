# -*- coding: utf-8 -*-
from __future__ import print_function
from random import shuffle


fids = range(13)
colors = ["♠","♥","♦","♣"]
jokers = ["JB","JR"]
trycnt = 0
trymax = 4
pnum = int(3)

def deckgen():
    deck = []
    for color in colors:
      for fid in fids:
        try:
            crd = str(int(hex(fid)[2:])+1)+color
        except:
            crd = str(hex(fid)[2:])+color
        deck.append(crd)
    return (deck + jokers)[:-3]

def showpils(pls,ui=False):
    for i in range(len(pls[0])):
        for j in range(len(pls)):
            try:
                print(pls[j][i], end='\t')#, flush=True)
            except: pass
        print('\n', end='')#, flush=True)
       
    if ui:
        if [len(a) for a in pls][1:]==[len(a) for a in pls][:-1] and len(pls)%2 == 1:
            pilui(pls,len(pls))
        else:
            raise "DAFUCK"
    else:
        return pls

        
def exactck(deck,div):
    return len(deck)/float(div) == len(deck)/div

def pilgen(deck,div,exact=False):
    if exact and not(exactck(deck,div)):
        raise "Bwaaaaaaaaaaa"
    pils = []
    for _ in range(div):
        pils.append([])
    for i in range(len(deck)):
        pils[i % div].append(deck[i])
    return pils

def pilui(pl,nbr):
    try:
        global trycnt
        global deck
        deck=[]
        pilid = int(input("Dans quelle pille est votre carte? ")) - (nbr/2)
        for i in range(nbr):
            j=int((pilid+i) % nbr)
            deck += pl[j]
        trycnt += 1
    except:
        print("Entrez un nombre bordel")


deck = deckgen()
print("Choisisez une carte (Sans le dire à l'ordi)")
showpils(pilgen(deck,5))
input("Press Enter to continue...")
shuffle(deck)
while trycnt < trymax:
    showpils(pilgen(deck,pnum,True),True)
i=int(pnum/2)
j=int((len(deck)/pnum)/2)
print(pilgen(deck,pnum,True)[i][j],"est votre carte")
