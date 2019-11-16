
# mediawiki-csv-formatter

![python](https://img.shields.io/badge/made%20with-python-blue)
[![datatransfer](https://img.shields.io/badge/works%20with-datatransfer-green)](https://www.mediawiki.org/wiki/Extension:Data_Transfer)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 
A simple script for pre processing .CSV files when importing content in [Mediawiki](https://www.mediawiki.org) with [DataTransfer](https://www.mediawiki.org/wiki/Extension:Data_Transfer).
Important: this script is tested and mantained only to work with google spreadsheet .CSV files.

The script will output a new .CSV file with the format [explained here](https://www.mediawiki.org/wiki/Extension:Data_Transfer#Importing_CSV_files).

Usage
-----

1. Clone repository and place the script wherever you want.
2. In command line, do:

`$ cd /path/to/script && python format.py <filename.csv> "<template_name>"`

#### <template_name>
You should create a template page with the same name in the mediawiki instance for the data to appear readable. You can create this template page before or after importing the csv with DataTransfer.

#### Import using UTF-16
The formatted csv file will be UTF-16 encoded, because of some DataTransfer limitation it will not render special characters if you use UTF-8.

License
-------

GPLv3
