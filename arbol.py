# -*- coding: utf-8 -*-
#
# Python version: 2.6.6
# Developer by: @itrogeno
# Date: 24-05-2011
# Description: Implementacion de un Arbol Binario en Python.
 
class Tree():
    '''Arbol Binario'''
 
    left  = None
    right = None
    data  = []
 
    def __init__(self, value):
        self.value = value
 
    def append(self, value):
        '''Metodo recursivo que permite anadir nuevos valores al
           arbol binario.
           Si el nuevo valor es mayor que el valor actual se
           inserta en la rama derecha, si es menor se inserta en
           la rama izquierda.'''
        self.__append(['left', 'right'][value > self.value],
                      value)
 
    def __append(self, name, value):
        '''Metodo privado que anade un nuevo nodo'''
        node = getattr(self, name, value)
 
        if node is None:
            node = Tree(value)
        else:
            node.append(value)
        setattr(self, name, node)
 
    def get_data(self):
        '''Devuelve una lista ordernada en forma ascendente
           con todos los valores ingresados.'''
        self.data[:] = []
        self.__order_data(self)
        return self.data
 
    def get_data_inverse(self):
        '''Devuelve una lista ordenada en forma descendente
           con todos los valores ingresados.'''
        return self.get_data()[::-1]
 
    def __order_data(self, node):
        '''Metodo recursivo privado'''
        def a(n):
            if n is not None: self.__order_data(n)
 
        a(node.left)
        self.data.append(node.value)
        a(node.right)
 
    def search(self, value):
        '''Permite buscar valores existentes en el arbol.
           Devuelve un objeto Tree() si encuentra el valor, de
           lo contrario devuelve un None.'''
        parent, node = self.__search(None, self, value)
        return node
 
    def __search(self, parent, node, value):
        '''Metodo recursivo privado que permite buscar valores
           existentes en el arbol.'''
        if node is None: return None, None
 
        if value == node.value:
            return parent, node
 
        parent, result = self.__search(node, node.left, value)
        if result is not None:
            return parent, result
 
        parent, result = self.__search(node, node.right, value)
        if result is not None:
            return parent, result
 
        return None, None
 
    def delete(self, value):
        '''Permite eliminar valores del arbol binario.'''
 
        parent, node = self.__search(None, self, value)
        if node is None:
            return
        # Seleccionamos uno de los dos nodos hijos, por defecto
        # siempre se utiliza el nodo derecho, pero si no existe
        # se utiliza el nodo izquierdo.
        child = getattr(node, ['left', 'right'][node.right
                                                is not None])
        if parent is not None:
            # Si el nodo tiene padre, quiere decir que no es el
            # nodo raiz.
            # Reemplazamos el nodo con su nodo hijo, por defecto
            # se utiliza el nodo derecho si no tiene se utiliza
            # el nodo izquierdo.
            direction = ['left', 'right'][parent.right is node]
            setattr(parent, direction, child)
 
            # Si se reemplazo por el nodo hijo derecho y tenia
            # hijos en el nodo izquierdo estos son heredados al
            # nodo hijo derecho, insertandolos al nivel mas bajo
            # de la rama izquierda.
            if node.left is not None and node.right is not None:
                root.__insert_left(node.right, node.left)
 
            del node
        else:
            # En esta implementacion es imposible eliminar el
            # nodo padre, para ello en vez de reemplazarlo con
            # el nodo hijo, solo heredamos los valores del hijo.
            # Una vez hecho eso eliminamos el nodo hijo.
            if node.left is not None and node.right is not None:
                child.__insert_left(node.right, node.left)
 
            node.value = child.value
            node.left  = child.left
            node.right = child.right
 
            del child
 
    def __insert_left(self, parent, node):
        if parent.left is None:
            parent.left = node
        else:
            self.__insert_left(parent.left, node)
 
    def __str__(self):
        return 'Value: %i' % self.value
 
def main():
    print "1° Insertamos datos al arbol"
 
    tree = Tree(2)
    tree.append(3)
    tree.append(1)
    tree.append(5)
    tree.append(4)
    tree.append(0)
    tree.append(-1)
    tree.append(-4)
    tree.append(-3)
    tree.append(-2)
    tree.append(-5)
    print ''
    print '2° Listamos los datos ordenados'
    print tree.get_data()
    print ''
    print '3° Listamos los datos inversos'
    print tree.get_data_inverse()
    print ''
    print '4° Buscamos los datos en forma individual'
    print '5 %s' % tree.search(5)
    print '1 %s' % tree.search(1)
    print '3 %s' % tree.search(3)
    print '4 %s' % tree.search(4)
    print '2 %s' % tree.search(2)
    print '6 %s' % tree.search(6)
    print ''
    print '5° Eliminamos el numero 2'
    tree.delete(2)
    print ''
    print '6° Volvemos a listar los datos'
    print tree.get_data()
    print tree.get_data_inverse()
    print ''
    print '7° Añadimos el numero 6 y -6'
    tree.append(6)
    tree.append(-6)
    print ''
    print '8° Volvemos a listar los datos'
    print tree.get_data()
    print tree.get_data_inverse()
    print ''
    print '9° Eliminamos el numero 4'
    tree.delete(4)
    print ''
    print '10° Volvemos a listar los datos'
    print tree.get_data()
    print tree.get_data_inverse()
 
if __name__ == '__main__':
    main()