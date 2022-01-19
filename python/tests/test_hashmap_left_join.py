from code_challenges.hashmap_left_join.hashmap_left_join import left_join

def test_import():
    assert left_join

def test_left_join():
    table1 = {'for': "Gondor", 'Comrade': "champion"}
    table2 = {'for': "Rohan", 'Comrade': "warrior"}
    actual = left_join(table1, table2)
    expected = {'for': ["Gondor", "Rohan"], 'Comrade': ["champion", "warrior"]}
    assert actual == expected

def test_left_join_table1_extra():
    table_1 = {'for': "Gondor", 'Comrade': "champion", "soldier": "barrel-chested"}
    table_2 = {'for': "Rohan", 'Comrade': "warrior"}

    actual = left_join(table_1, table_2)
    expected = {'for': ["Gondor", "Rohan"], 'Comrade': ["champion", "warrior"], "soldier": ["barrel-chested", None]}
    assert actual == expected

def test_left_join_no_duplicates():
    table_1 = {'for': "Gondor", 'Comrade': "champion", "soldier": "barrel-chested"}
    table_2 = {'muster-the': "Rohan", 'champion': "warrior"}

    actual = left_join(table_1, table_2)
    expected = {'for': ["Gondor", None], 'Comrade': ["champion", None], "soldier": ["barrel-chested", None]}
    assert actual == expected
