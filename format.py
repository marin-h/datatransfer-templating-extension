#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os
import sys
import unicodedata

rawFile = sys.argv[1]
templateName = sys.argv[2]
newFile = rawFile.replace(".csv", "_to_import_utf8.csv")
newFile_utf16 = rawFile.replace(".csv", "_to_import_utf16.csv")

# validar que estén todos los parámetros que necesita el script,
#    * [1] Archivo de entrada
#    * [2] NombreDeLaPlantilla
if len(sys.argv) is not 3:
    print "Debe indicar primero la ruta del archivo de entrada y en segundo lugar el nombre de la plantilla."
    sys.exit()

if not os.path.exists(rawFile):
    print "El archivo especificado no existe. "
    print os.path.basename(rawFile)
    sys.exit()

print ('# Procesando')

with open(newFile, 'w') as outputcsv:
    with open(rawFile) as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        # Nos aseguramos de que esté entrecomillado el contenido de cada columna
        writer = csv.writer(outputcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # Seteamos headers.
        rawHeaders = next(reader)
        if rawHeaders:
            # Hardcodeamos primer campo, porque si o sí tiene que tener valor "Title"
            titleHeader, fieldNames = 'Title', rawHeaders[1:]
            # Construir headersRow, para esto formateamos los fieldNames así:
            # NombreDeLaPlantilla[fieldName]
            headersRow = [ titleHeader ]
            for columnHeader in fieldNames:
                headersRow.append(
                    templateName + "[" +
                    unicodedata.normalize(
                        'NFKD', unicode(columnHeader, 'utf-8')
                    ).encode('ascii', 'ignore') + "]"
                )
            print ('# Escribiendo headers')
            writer.writerow(headersRow)
        for row in reader:
            newLine = []
            for column in row:
                newLine.append(column)
            writer.writerow(newLine)
print ('# Fin del formateo, todo bien!')

# TODO: Lo que sigue debería estar en otro script,
# y hacer un tercero que corra los dos primeros.

# Reencodear csv de utf-8 a utf-18
print ('# Reencodeando')
f = open(newFile, 'rb')
content= unicode(f.read(), "utf-8")
f.close()
f = open(newFile_utf16, 'wb')
f.write(content.encode("utf-16"))
f.close()

print('# Listo, el archivo a importar en mediawiki es: '+ newFile_utf16)
