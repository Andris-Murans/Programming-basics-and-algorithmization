# converter.py

# -----------------------------------
# 1. Definējam konversijas konstantes
# -----------------------------------
# Konstantes raksta ar LIELAJIEM BURTIEM.
# Tās ir vērtības, kuras programmā nemainās.

KM_TO_MI = 0.621371      # 1 kilometrs = 0.621371 jūdzes
KG_TO_LB = 2.20462       # 1 kilograms = 2.20462 mārciņas
L_TO_GAL = 0.264172      # 1 litrs = 0.264172 galoni
USD_TO_EUR = 0.84235020  # 1 dolārs = 0.84235020 eiro

# -----------------------------------
# 2. Parādām lietotājam izvēlni
# -----------------------------------
print("Izvēlies konversiju:")
print("1) km <-> mi")       # no km uz jūdzēm
print("2) kg <-> lb")       # no kg uz mārciņām
print("3) L <-> gal")       # no litriem uz galoniem
print("4) $ <-> €")         # no dolāriem uz eiro

# input() nolasa lietotāja ievadi no tastatūras
choice = input("> ")
