# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 20:12:56 2022

@author: rodro
"""

from module.nodo import Nodo

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    
    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, valor):
        self._cabeza = valor
    
    @property
    def cola(self):
        return self._cola
    
    @cola.setter
    def cola(self, valor):
        self._cola = valor
    
    @property
    def tamanio(self):  #modificado
       
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.siguiente 
        self.contador = contador
    
        return  contador
      
    
    def agregar(self, item):
        temp = Nodo(item)
        if self.cabeza == None:  #modificado
            self.cabeza = temp
            self.cola = temp
        else:  
            temp.siguiente = self.cabeza  
            self.cabeza = temp
    
    
    # def anexar(self, item):  #no funciona
    #     temp = Nodo(item)
    #     if self.cola == None:
    #         self.cabeza = temp
    #         self.cola = temp
    #     else:
    #         temp.anterior = self.cola
    #         self.cola = temp
        
    def anexar(self, item): #este si anda
        temp = Nodo(item)
        if self.cabeza == None:  #modificado
            self.cabeza = temp
            return
        else:
            apuntador = self.cabeza  
            while apuntador.siguiente != None:  
                apuntador = apuntador.siguiente
            apuntador.siguiente = temp
            temp.anterior = apuntador
        
   
   
    def estaVacia(self): 
      return self.cabeza == None    #modificado
    

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado
    
    def copiar(self):
        actual  = self.cabeza
        cadena=""
        while actual!= None:
            cadena += " "+ str(actual.dato)
            actual = actual.siguiente
        print(cadena)
        
    def insertar(self, posicion, item):
        nuevoNodo = Nodo(item)
        if  0 < posicion > self.contador:
            raise IndexError
        
        if posicion == 0:
            self.agregar(item)
        
        elif posicion == self.contador:
             self.anexar(item)
        
        else:
            temp = self.cabeza
            for nodo in range(posicion-1):  
                temp = temp.siguiente 
            nuevoNodo.anterior = temp     
            nuevoNodo.siguiente = temp.siguiente
            if temp.siguiente != None:
                temp.siguiente.anterior = nuevoNodo
            temp.siguiente = nuevoNodo
           
      
                
        
            
lis = ListaDoble()

lis.agregar(5)
lis.agregar(6)
        
print(lis.estaVacia())   
print(lis.tamanio) 
print(lis.copiar())
# lis.insertar(, 1)
lis.anexar(1)
print(lis.copiar())
print(lis.tamanio) 
lis.insertar(1, 1)
print(lis.copiar())
