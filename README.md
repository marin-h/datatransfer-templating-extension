
# DataTransfer templating extension

![python](https://img.shields.io/badge/made%20with-python-blue)
 
Massively fill in mediawiki templates from any spreadsheet very easily using this script with DataTransfer and Mediawiki.

Output UTF-16 CSV files with the format [explained here](https://www.mediawiki.org/wiki/Extension:Data_Transfer#Importing_CSV_files).

Then use DataTransfer to import content to mediawiki. 

## Usage

```
$ cd /path/to/script && python format.py filename.csv template_name
```

## Mediawiki template setup

#### <template_name>
You should create a template page with the same name in the mediawiki instance for the data to appear readable. You can create this template page before or after importing the csv with DataTransfer.

#### Import using UTF-16
The formatted csv file will be UTF-16 encoded, because of some DataTransfer limitation it will not render special characters if you use UTF-8.

This script works with [DataTransfer](https://www.mediawiki.org/wiki/Extension:Data_Transfer) and is tested with Google Sheets.
