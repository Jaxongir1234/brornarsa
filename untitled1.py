# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T4BJJK2avJJyuf546rDrJfRCPViJR3WG
"""

import pandas as pd
baza={
    "FISH":['Rashidova Muyassar','Ergasheva Gulassal','Xaytaliyev Bekmurod','Ibrohimova Maftuna'],
     "yoshi":[ '12','13','11','11' ],
    "Jinsi": [ 'qiz bola','qiz bola','ogil bola','qiz bola' ],
    "Qaysi maktabda":[ '40-maktab','38-maktab', 'Prizendent maktabi','11-maktab ' ]
}
df=pd.DataFrame(baza)
print(df)

filtr=df[(df['Jinsi']=="ogil bola") &(df['yoshi']>'10')]
print(filtr)
