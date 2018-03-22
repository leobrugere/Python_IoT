#!/usr/bin/env python3.5
#-*- coding: utf-8 -*

import requests
import sys

req = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
data=req.json()
t = data['Data']

while True:
	print("-Voir la liste: Liste \n-Quitter le programme: Quitter \n-Voir une monnaie en renseignant son nom, exemple: BTC")
	demande = input("Que voulez-vous faire?\n")

	if demande == "Liste":
		for Z in t:
			print(Z)

	elif demande == "Quitter":
		print("Vous avez quitté l'application")
		sys.exit()

	else:
		prix = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+demande+'&tsyms=BTC,USD,EUR')
		data2 = prix.json()
		print(data2)
