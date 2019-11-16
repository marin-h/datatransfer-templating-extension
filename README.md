
# mediawiki-csv-formatter

![python](https://img.shields.io/badge/made%20with-python-blue)
[![datatransfer](https://img.shields.io/badge/works%20with-datatransfer-green)](https://www.mediawiki.org/wiki/Extension:Data_Transfer)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
 
A simple script for formatting a google spreadsheet .csv raw file into a mediawiki compatible csv.
Important: this script is tested and mantained only to work with google spreadsheet .CSV files.

[DataTransfer](https://www.mediawiki.org/wiki/Extension:Data_Transfer) is a [Mediawiki](https://www.mediawiki.org) extension for importing csv files as mediawiki pages. 

This script allows the user to get their data in a DataTransfer-ready formatted csv, as it is explained [here](https://www.mediawiki.org/wiki/Extension:Data_Transfer#Importing_CSV_files).

## Usage

1. Clone repository and place the script wherever you want.

2. In commandline, do:

`$ cd /path/to/script`

`$ python format.py <filename.csv> "<template_name>"`

Notice that you should create a template page with the same name in the mediawiki instance for the data to appear readable. You can create this template page before or after importing the csv with DataTransfer.

3. The formatted csv file will be UTF-16 encoded, because DataTransfer extension will not render special characters if you use UTF-8.

