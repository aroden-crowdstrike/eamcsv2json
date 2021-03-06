
EAM CSV to JSON
=================

Example script for converting data from EAM, i.e. splunk, CSV files to json. 
This provides a useful example of how to export and use data.

    usage: eamcsv2json [-h] -i INPUT [-o OUTPUT] [-e ERRORS] [-l LOG] [-c CONFIG]
                       [-t TYPE_COLUMN]

    EAM (Splunk) CSV to JSON conversion script meant to handle larger files with
    potential errors. New lines and quotes are handled gracefully when data
    fields are quoted in double quotes (") and escaped with backslash (\).
    This is outside RFC-4180 specification

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            CSV file name to be read
      -o OUTPUT, --output OUTPUT
                            (optional) Output file name; else stdout
      -e ERRORS, --errors ERRORS
                            (optional) Error file name; when provided CSV 3 lines
                            of context will be printed. Default is content to log
                            file only
      -l LOG, --log LOG     (optional) Log file name; when provided log message
                            will go to file. Default is stderr
      -c CONFIG, --config CONFIG
                            (optional) Configuration for type mappings; else first
                            row is considered for labels. When provided type
                            column setting is used
      -t TYPE_COLUMN, --type-column TYPE_COLUMN
                            (optional) When config set use this column to expect
                            type mapping. Default 4

Install
-------

    pip install eamcsv2json


Library
-------
Available for usage as library

    from eamcsv2json.eamcsv2dict import EamCsv2Dict
    
    type_mappings = {
        'TypeA': ['field1', 'field2'],
        'TypeB': ['fieldA', 'fieldB'],
    }
    converter = EamCsv2Dict('input.csv', 'error.csv', type_mappings, 2)
    for a_dict in converter.covert():
        print(a_dict)


Examples
-------

Convert data with first row as columns

    eamcsv2json --input ./data/20180629_test2.csv -e ./errors.txt


Convert data with a type mapping and CSV error lines going to a file

    eamcsv2json \
        --input ./data/main10M.csv \
        --errors ./data/main10M-errors.txt \
        --config ./data/transforms.conf \
        --output ./data/main10M.json
