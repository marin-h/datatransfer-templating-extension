#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os
import sys
import urllib
import unicodedata
import re

if len(sys.argv) is not 3:
    print "Debe indicar primero la ruta del archivo de entrada y en segundo lugar el nombre de la plantilla."
    sys.exit()

rawFile = sys.argv[1]
templateName = sys.argv[2]

if not os.path.exists(rawFile):
    print "El archivo especificado no existe. "
    print os.path.basename(fn)
    sys.exit()

with open(rawFile.replace(".csv", "_to_import.csv"), 'w') as outputcsv:
    with open(rawFile) as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        writer = csv.writer(outputcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        rawHeaders = next(reader)
        if rawHeaders:
            titleHeader, headers = 'Title', rawHeaders[1:]
            fieldNames = [ titleHeader ]
            for columnHeader in headers:
                fieldNames.append(
                    templateName + "[" +
                    unicodedata.normalize(
                        'NFKD', unicode(columnHeader, 'utf-8')
                    ).encode('ascii', 'ignore') + "]"
                )
            writer.writerow(fieldNames)
        for row in reader:
            newLine = []
            titleColumn, columns = row[0], row[1:]
            #titleColumn = unicodedata.normalize(
            #    'NFKD', unicode(titleColumn, 'utf-8')
            #).encode('ascii', 'ignore')
            #titleColumn = re.sub('[^a-zA-Z0-9\n\.]', ' ', titleColumn)
            titleColumn = titleColumn[:40]
            newLine.append(titleColumn)
            for column in columns:
                newLine.append(urllib.quote(column, safe=" !¡¿?&%$#/,-_.:;()[]{}='\""))
            writer.writerow(newLine)
