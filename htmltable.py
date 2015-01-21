# -*- coding: utf-8 -*-
import re

#Should re-write with BeautifulSoup
def html_table_to_rows(filename):
    """Extracts rows and entries from input html."""
    handle = open(filename)
    data = handle.read()
    regex = dict()
    for x in ['tr', 'td']:
        regex[x] = re.compile("<" + x + ".*?>(?:<B>)*(?:<FONT.*?>)*(.*?)(?:</FONT>)*(?:</B>)*</" + x + ">", re.DOTALL | re.IGNORECASE)
        #regex[x] = re.compile("<" + x + ".*?>(?:<FONT.*?>)*(.*?)(?:</FONT>)*</" + x + ">", re.DOTALL | re.IGNORECASE)
    #rows = []
    html_rows = regex['tr'].findall(data)
    # Find entries of each row.
    for html_row in html_rows:
        entries = regex['td'].findall(html_row)
        # Remove excel formatting.
        if ">" in entries[0]:
            entries[0] = entries[0].split('>')[-1]
        yield entries
        #rows.append(entries)
    #return rows

def rows_to_html_table(rows, headers=None):
    def wrap_html_tag(tag, data, attr=""):
        if attr:
            attr = " " + attr
        return '<%s%s>%s</%s>' % (tag, attr, data, tag)

    def wrap_headers(headers):
        row = []
        for header in headers:
            row.append(wrap_html_tag('th', header))
        html_header = wrap_html_tag('thead',wrap_html_tag('tr',"".join(row)))
        return html_header

    def wrap_row(row):
        row_ = []
        for element in row:
            row_.append(wrap_html_tag('td', element))
            return wrap_html_tag('tr', "".join(row))
    
    html_output = []
    if headers:
        html_output.append(wrap_headers(headers))

    body_rows = []
    for row in rows:
        body_rows.append(wrap_row(row))
    html_output.append(wrap_html_tag('tbody', "".join(body_rows)))
    html_output = wrap_html_tag('table', "".join(html_output))
    return html_output
    
#def detect_keys(rows):
    #mset = Multiset([len(row) for row in rows])
    #largest = mset.largest()
    #for row in rows:
        #if len(row) == largest:
            #return row
