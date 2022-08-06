

dial_codes = [(1, "USA"), (4, "UK"), (6, "Sweden"), (7, "France"), (8, "Zimbabwe"), (9, "Montreal"), (12, "Greenland")]

def data():
    return {code: country for code, country in dial_codes}