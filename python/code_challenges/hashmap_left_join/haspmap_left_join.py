def left_join(table1, table2):

    joined_table = {}
    for key, value in table1.items():
        if table2.get(key):
            joined_table[key] = [value, table2.get(key)]
        else:
            joined_table[key] = [value, None]
    return joined_table
