def shelve_csv_dictionary(csv_reader, shelve_filename, values_as_lists=False, value_map=str):
    d = shelve.open(shelve_filename)
    for row in csv_reader:
    try:
        key = str(row[0]) # Shelve keys are strings.
    except IndexError:
        print row
        continue
    try:
        if values_as_lists:
        value = map(int, row[1:])
        else:
        #value = int(row[1])
        value = value_map(row[1])
            d[key] = value
    except ValueError:
        pass
    d.close()

def create_shelves():
    # Create shelves.
    names = ['target_counts', 'category_target_counts', 'article_categories', 'category_articles', 'category_in_links', 'in_links']
    for name in names:
        print "Shelving:", name
        values_as_lists = not ('counts' in name)
        reader = csv.reader(codecs.open(name + '.csv', encoding='ascii'))
        shelve_csv_dictionary(reader, name + ".shelve", values_as_lists=values_as_lists)

def invert_csv_dict(reader, writer):
    inv = dict()
    for row in reader:
        source = int(row[0])
        targets = map(int, row[1:])
        for target in targets:
            inv.setdefault(target, []).append(source)
        keys = inv.keys()
        keys.sort()
        for key in keys:
            values = inv[key]
            values.sort()
            row = [key]
            row.extend(values)
        writer.writerow(row)

def invert_csv_dicts():
    ## Invert dictionaries
    reader = csv.reader(codecs.open('article_categories.csv', encoding='ascii'))
    writer = csv.writer(codecs.open('category_articles.csv', mode='w', encoding='ascii'))
    invert_csv_dict(reader, writer)
    reader = csv.reader(codecs.open('category_out_links.csv', encoding='ascii'))
    writer = csv.writer(codecs.open('category_in_links.csv', mode='w', encoding='ascii'))
    invert_csv_dict(reader, writer)
    reader = csv.reader(codecs.open('out_links.csv', encoding='ascii'))
    writer = csv.writer(codecs.open('in_links.csv', mode='w', encoding='ascii'))
    invert_csv_dict(reader, writer)
