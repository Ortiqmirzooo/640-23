# -*- coding: utf-8 -*-
"""ortiqmirza

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FHqkcaOuaQECrLap5-EWzCb9rkNrdEHa
"""

import pandas as pd

baza={
    'ismi':['mavludaxon','munavvarxon','ortiqmirzo','bekzod','sunnatbek','samandar','asadbek','abdurahmon','boburjon','jamshid'],
    'yoshi':[35,14,28,19,30,21,12,22,39,20],
    'shahar':['fargona','toshkent','namangan','guliston','navoiy','fargona','margilon','urganch','fargona','andijon']
}
mb=pd.DataFrame(baza)

print(mb)

yosh_odamlar=mb[mb['yoshi']<25]
print("\n 30 yoshdan kichiklar:\n",yosh_odamlar)

mb['yoshi']+=1
print("\n yangilangan dataframe:\n",mb)

print(mb['shahar']=='fargona')

import numpy as np
# 1. massiv yaratish

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# 2. Matematik operatsiyalar
yigindi_array = np.sum(array_1d)
ortachaqiymat_array = np.mean(array_1d)
kopaytma_array = np.prod(array_1d)

print("1d Massiv: ", array_1d)
print("2d Massiv:\n ", array_2d)
print("Massivlar yig'indisi: ", yigindi_array)
print("O'rtacha qiymat: ", ortachaqiymat_array)
print("Ko'paytma: ", kopaytma_array)