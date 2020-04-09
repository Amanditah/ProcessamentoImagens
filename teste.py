# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:09:34 2020

@author: amand
"""
import numpy as np
import cv2

def AbrirImagem(img):                           #função para abrir a imagem
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #Comando para abrir a imagem colorida
    plt.imshow(img)                             #Montando a plotagem
    plt.show()                                  #Abrindo a imagem

def main():
    from matplotlib import pyplot as plt
    objeto_imagem = cv2.imread("desmatamento.jpg") #Chamando a imagem que deve estar na mesma pasta do código
    Altura, Largura, Canais = objeto_imagem.shape  #Função que pega a largura, altura e os canais de cor da imagem
    print("\nDimesões: " + str(Largura) + "x" + str(Altura))
    print("Canais de Cores: ", Canais, "\n")
    
    #Como a imagem é uma matriz utilizamos dois for para percorrer pixel a pixel
    
    # for y in range(0, Altura):          #eixo y começa em 0 e vai ate a Altura
    #    for x in range(0, Largura):      #eixo x começa em 0 e vai ate a Largura
    #         print("[" + str(x) + "," + str(y) + "] = " + str(objeto_imagem[y][x]))
    #         input()                     #ele vai dar a cor pausadamente esperando o enter para pular 
    #                                     #pro proximo pixel, se você  tirar ele vai ler todos de uma vez
    #                                     #fica ao seu critério
            
    color = ('b', 'g', 'r')             #variavel com parametros de cores
    
    for i, cor in enumerate(color):     #a variavel i e cor vão rodar até o numero de cores
        
        #Criando o histograma
         histograma = cv2.calcHist([objeto_imagem], [i], None, [256], [0,256])
         plt.plot(histograma, color = cor)
         plt.xlim([0, 256])         
            
    plt.show() #plotando o histograma
    
    AbrirImagem(objeto_imagem) #abrindo a imagem
    
main()

