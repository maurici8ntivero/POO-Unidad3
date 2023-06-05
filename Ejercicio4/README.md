### Herencia y métodos con ligadura dinámica
#### Descripción del sistema
1. En una empresa constructora existen tres tipos de empleados: de planta,
contratados y externos.
2. De cada empleado se registra: DNI, nombre, dirección y teléfono.
3. Si el empleado es de planta, además de los datos de empleado, se registra:
sueldo básico y antigüedad.
4. Si el empleado es contratado, además de los datos de empleado, se registra:
fecha de inicio y de finalización de contrato, cantidad de horas trabajadas y valor
por hora (es el mismo para todos los empleados contratados).
5. Los empleados externos realizan tareas especiales estas tareas pueden ser
carpintería, electricidad, plomería. Para este tipo de empleados, además de los
datos de empleados, se registra: tarea, fecha de inicio, fecha de finalización, monto
viático, el costo de la obra y monto del seguro de vida.
6. El sueldo de un empleado contratado se calcula con la siguiente fórmula:
Sueldo = cantidad de horas trabajadas * valor de la hora
7. El sueldo de un empleado de planta se calcula con la siguiente fórmula:
Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad
8. El sueldo de un empleado externo se calcula:
Sueldo = costo de la obra - viático- monto del seguro de vida

Para el desarrollo del sistema requerido usted debe:

**a-** Definir la jerarquía de clases correspondiente a la descripción dada.

**b-** Definir una clase colección basada en un arreglo Numpy, cuyo tamaño se debe
ingresar por teclado, para almacenar los empleados de la empresa.

**c-** Almacenar en memoria principal los empleados de la empresa, obteniendo lopos
datos de los archivos “planta.csv”, “contratados. csv”, “externos. csv” que contienen
los datos de cada uno de los tipos de empleados.

**d-** Implementar un programa que a partir de la información almacenada en
memoria permita:

1. Registrar horas: Ingresar el DNI de un empleado y la cantidad de horas trabajadas
en el día de la fecha e incrementar la cantidad de las horas trabajadas del empleado.
2. Total de tarea: Dada una tarea mostrar el monto a pagar para ella. Solo se
consideran las tareas que no han finalizado.
3. Ayuda Económica: La empresa dará una ayuda solidaria a los empleados cuyo
sueldo sea inferior a $150000; listar nombre, dirección y DNI de los empleados que
les corresponde la ayuda.
4. Calcular sueldo: Mostrar nombre, teléfono y sueldo a cobrar de todos los
empleados.