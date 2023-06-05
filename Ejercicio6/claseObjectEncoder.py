import json
from pathlib import Path
#asi guardo y leo ...igual que base de datos
class ObjectEncoder(): 
    def guardarJSONArchivo(self,lista,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(lista,destino,indent=4)
            destino.close
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            lista = json.load(fuente)
            fuente.close()
            return lista

    