"""
Programa para redirigir archivos con una extension especifica
alojados dentro de una carpeta a otra
"""
from shutil import move
import os

ORIGEN = r'C:\Users\pc\Downloads'
DESTINO = r'C:\Users\pc\Documents\Electronic Arts\Los Sims 4\Mods'
EXTENSION = '.package'	#Extension de los archivos a reubicar

def main() -> None:
	for archivo in os.listdir(ORIGEN):
		if os.path.splitext(archivo)[1] == EXTENSION:	#Si la extension del archivo es la que quiero
			move(os.path.join(ORIGEN, archivo), os.path.join(DESTINO, archivo))		
	
main()