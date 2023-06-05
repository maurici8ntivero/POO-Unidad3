from zope.interface import Interface

class Icoleccion(Interface):
    #a- insertarElemento: para insertar un objeto en una posición determinada en una colección, 
    # teniendo en cuenta el manejo de excepciones cuando la posición donde se vaya a insertar no sea válida.
    def insertarElemento(elemento,posicion):
        pass
    #b-  agregarElemento: para agregar un elemento al final de una colección.
    def agregarElemento(elemento):
        pass
    #c- mostrarElemento: dada una posición de la colección, mostrar los datos del elemento almacenado
    #  en dicha posición si esa posición es válida, en caso de que no sea válida lanzar una excepción que controle el error.
    def mostrarElemento(posicion):
        pass
    