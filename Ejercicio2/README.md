___Agregación___

La heladería “El Conito” requiere una aplicación para el sector de ventas que registre los helados vendidos de modo que facilite el análisis de estos datos. 

#### **Descripción**

    1. La heladería presenta distintos sabores de helado.
    2. Cada sabor tiene asociado un número que comienza en 1 y es correlativo.
    3. De cada sabor se registra el idSabor, el nombre y los ingredientes.
    4. Los helados se distinguen por el peso expresado en gramos y precio.
    5. Los tipos de helados que se venden son de 100gr, 150 gr, 250 gr, 500 gr y 1000gr.
    6. De un helado vendido se registra el peso del helado y el/los sabor/es pedidos.

#### **Diagrama de clases**

[![diagrama.png](https://campusvirtual.unsj.edu.ar/pluginfile.php/156855/mod_assign/intro/Helado-Sabor.drawio.png)](https://campusvirtual.unsj.edu.ar)


> La aplicación que usted debe implementar:

**A.** Implementar las clases del diagrama UML dado.
**B.** Definir una clase ManejaSabores que permita manejar los n sabores que la heladería presenta a la venta.
**C.** Definir una clase ManejaHelados que registre y gestione a través de una lista los helados vendidos.
**D.** Implementar un programa principal que permita:
    **a.** Cargar los datos de los sabores en una instancia de la clase ManejaSabores. Estos datos se encuentran en el archivo sabores.csv.
    **b.** A través de un menú de opciones realice las siguientes funcionalidades:
1. Registrar un helado vendido (instancia de la clase helado).

2. Mostrar el nombre de los 5 sabores de helado más pedidos.
3. Ingresar un número de sabor y estimar el total de gramos vendidos. Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores. Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr.
4. Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.
5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado.