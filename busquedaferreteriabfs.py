# Importación de Queue
from queue import Queue


class Grafo:

    """
    Una clase para representar a un grafo
    ...
    Atributos
    ----------
    m_num_de_nodos : int
        número de nodos
    m_nodos : int
        rango de nodos
    m_directo : boolean
        directo o no directo 
    m_list_ady : mutable
        Defino el diccionario para implementar la lista adyacencia
    Métodos
    -------
    agregar_aristas(self, nodo1, nodo2, peso=1):
        Añadir aristas al grafo
    imprimir_lista_de_adj(self):
        Imprime la representación del grafo
    bfs_traversal(self, nodo_inicial):
        Imprime el recorrido del grafo apartir de un nodo dado
    """
    # Constructor

    def __init__(self, num_de_nodos, directo=True):
        '''
        Constructor inicializador de la clase grafo.
            Parámetros:
                m_num_de_nodos : int
                    número de nodos
                m_nodos : int
                    rango de nodos
                m_directo : boolean
                    directo o no directo 
                m_list_ady : mutable
                    Defino el diccionario para implementar la lista adyacencia
                m_ferreterias : mutable
                    Defino el diccionario para implementar las ferreterias
        '''
        try:
            # Número de aristas
            self.m_num_de_nodos = num_de_nodos
            # Inicializa el rango de los nodos
            self.m_nodos = range(self.m_num_de_nodos)
            # Definir el tipo de un grafo
            self.m_directo = directo
            #ferreterias usando diccionario
          
            # Lista de adyacencia usando diccionario
            self.m_list_ady = {nodo: set() for nodo in self.m_nodos}
        except KeyError as e:
            print(e)        

    def agregar_aristas(self, nodo1, nodo2, peso=1):
        """
        Función que agrega una arista al grafo
        Parámetros
        ----------
        nodo1 : int
            nodo de partida
        nodo2 : int
            nodo de llegada
        peso : int
            peso del nodo

        """
        try:
            # Añade la arista del nodo1 al nodo2"""
            self.m_list_ady[nodo1].add((nodo2, peso))

            # Si un grafo es no dirigido, añade la misma arista
            if not self.m_directo:
            # Pero también en la dirección opuesta
                self.m_list_ady[nodo2].add((nodo1, peso))
        except KeyError as e:
            print (e)

    def imprimir_lista_de_adj(self):
        """ Función que imprimir la representación del grafo
        """
        try:
            # Agrega clave y recorre las listas adyacentes
            for clave in self.m_list_ady.keys():
            # Imprimi la lista de nodos con su clave
                print("nodo", clave, ": ", self.m_list_ady[clave])
        except KeyError as e:
            print(e)

    def bfs_traversal(self, nodo_inicial):
        """
        Función que imprime el recorrido del grafo apartir de un nodo dado
        Parámetros
        ----------
        nodo_inicial : int
            nodo de partida del traversal

        """
        # Obtener los nodos visitados
        visitado = set()
        # Inicialización de una cola
        cola = Queue()

        # Agrega el nodo inicial a la cola
        cola.put(nodo_inicial)
        # Agrega el nodo inicial a la lista visitado
        visitado.add(nodo_inicial)

        # Leer desde una cola mientras que no este vacía
        while not cola.empty():
            # Obtener de la cola un nodo actual
            nodo_actual = cola.get()
            # Imprimir el nodo actual
            print(nodo_actual, end=" ")

            # En el siguiente nodo obtener las listas adyacentes de los nodos actuales
            for (siguiente_nodo, peso) in self.m_list_ady[nodo_actual]:
                # Si el siguiente nodo no está marcado como visitado
                if siguiente_nodo not in visitado:
                    # Entonces lo agrega en la cola
                    cola.put(siguiente_nodo)
                    # Debe marcarlo como visitado
                    visitado.add(siguiente_nodo)


# main del programa
if __name__ == "__main__":
    #### Ejemplo #####

    # Crea una instancia para la clase grafo y lo define con 5 nodo y que sea no directo
    g = Grafo(16, directo=False)

# Agregar al grafo las aristas con un peso
    # Agrega la arista (0,1) con peso 1
    g.agregar_aristas(0, 1, 1)
    g.agregar_aristas(1, 3, 2)
    g.agregar_aristas(1, 2, 1)
    g.agregar_aristas(3, 4, 0.5)
    g.agregar_aristas(2, 5, 2)
    g.agregar_aristas(4, 6, 0.5)
    g.agregar_aristas(6, 7, 2)
    g.agregar_aristas(6, 8, 2)
    g.agregar_aristas(5, 9, 2)
    g.agregar_aristas(7, 10, 3)
    g.agregar_aristas(7, 11, 3)
    g.agregar_aristas(9, 12, 3)
    g.agregar_aristas(5, 13, 3)
    g.agregar_aristas(10, 14, 2)
    g.agregar_aristas(12, 15, 2)
    
    
    opcion = '0'
    while not(opcion=='6'):
        print(' 1. Ver el grafo')
        print(' 2. Ver el recorrido')
        print(' 3. Salir')

        opcion=input('  --- ¿Cuál opcion?: ')
    
        if (opcion=='1'):
            print(' **** menu opcion 01 ****')
            # Imprime las lista de adyacencia del nodo con su nodo y peso
            g.imprimir_lista_de_adj()
        
        elif (opcion=='2'):
            print(' **** menu opcion 02 ****')
            # Imprime un mensaje sobre la siguiente ejecución
            print("Lo siguiente es la primera travesía de ancho" " (empezando por el vértice 0)")
            # Imprime la primera travesía
            g.bfs_traversal(0)
                
        elif (opcion=='3'):
            print(' **** Saliendo del menu  ****')
        else:
            print('No existe la opcion')
        break

    #print(Grafo.__doc__)