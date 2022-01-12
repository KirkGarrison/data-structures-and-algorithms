from code_challenges.hashtable.hashtable import HashTable

def test_import():
    assert HashTable

def test_add():
    table = HashTable()
    table.add('cheese', 'blue')

    actual = table.table[470][0]
    expected = ('cheese', 'blue')
    assert actual == expected
def test_get():
    table = HashTable()
    table.add('cheese', 'blue')
    table.add('chese', 'bloo')
    table.add('cheeese', 'bluoe')

    actual = table.get('chese')
    expected = 'bloo'
    assert actual == expected

def test_contains():
    table = HashTable()
    table.add('cheese', 'blue')

    actual = table.contains('cheese')
    expected = True
    assert actual == expected

def test_hash():
    table = HashTable()

    actual = table.hash('cheese')
    expected = 28
    assert actual == expected
