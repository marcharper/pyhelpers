# -*- coding: utf-8 -*-
import pyExcelerator

def xls_to_rows(filename):
    """(Generator) Parses .xls files to list of rows."""
    parsed_xls = pyExcelerator.parse_xls(filename, 'cp1251')
    for name, values in parsed_xls:
        result = list()
        current_row = 0
        for row, col in sorted(values.keys()):
            cell = str(values[(row, col)])
            if row > current_row:
                yield result
                current_row = row
                result = [cell]
            else:
                while col > len(result):
                    result.append('')
                result.append(cell)
