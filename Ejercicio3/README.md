### Clase asociación

Con su grupo de trabajo deben desarrollar una aplicación para manejar las
inscripciones de las personas a los talleres de capacitación que se dictan en unaescuela complementaria. Al momento de la inscripción la persona puede o no abonar el costo del taller.

**a-** Defina las clases involucradas en el siguiente diagrama.

**a-** Defina una clase con un atributo arreglo para almacenar instancias de la
clase TallerCapacitacion. El archivo “Talleres.csv” contiene en la primera línea la
cantidad de talleres, y a continuación los datos de cada uno de ellos.

**b-** Defina una clase colección (manejador), tipo lista para almacenar las instancias
de la clase Persona.

**c-** Defina una clase colección (manejador), tipo arreglo para almacenar instancias
de la clase Inscripcion.

**d-** Implementar un programa que permita:
1. Cargar los datos de los talleres en la clase TallerCapacitacion a partir de los
datos registrados en el archivo.
2. Inscribir una persona en un taller: Se registra la inscripción (con el atributo
pago en False) y la cantidad de vacantes del taller debe ser actualizada.
3. Consultar inscripción: Ingresar el DNI de una persona, si está inscripta mostrar
el nombre del taller en el que se inscribió y el monto que adeuda.
4. Consultar inscriptos: Ingresar el identificador de un taller y listar los datos de
los alumnos que se inscribieron en él.
5. Registrar pago: Ingresar el DNI de una persona y registrar el pago (dar al
atributo pago el valor True).
6. Guardar inscripciones: Generar un nuevo archivo que contenga los siguientes
datos de las inscripciones: DNI de la persona, idTaller, fechaInscripcion y pago.