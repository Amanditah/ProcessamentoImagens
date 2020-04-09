# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:05:11 2020

@author: amand
"""


import numpy as np
import math
import matplotlib
import pylab as pl

x = np.linspace(-np.pi, np.pi) #A função linspace cria uma seqüência de números 
                               #uniformemente espaçados entre os limites dados,
                               #no caso vai de -pi até pi

S = np.sin(x)                  #calcula o seno
D = (np.cos(x) * (-1))         #se a derivada do seno é -cosseno, calculei o 
                               #cos e multipliquei por -1

pl.plot(x, S)                  #plotando o gráfco do seno
pl.plot(x, D)                  #plotando o gráfico do cosseno

#formatação do eixo x
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])


#formatação do eixo y
pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

#plotando
pl.show()