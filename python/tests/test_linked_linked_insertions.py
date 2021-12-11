from linked_list.linked_list import Node, LinkedList
import pytest

def test_node_value():
    node = Node("testing")
    actual = node.value
    expected = "testing"
    assert actual == expected

# @pytest.mark.skip('pending')
def test_node_next():
    node = Node("testing2")
    node2 = Node("testing2", node)

    actual = node2.next
    expected = node
    assert actual == expected


@pytest.fixture
def base_list():
    linkedlist = LinkedList()
    linkedlist.insert("astronaut")
    linkedlist.insert("pilot")
    return linkedlist

# @pytest.mark.skip('pending')
def test_append(base_list):
    base_list.append("crewman")

    current_node = base_list.head
    actual = current_node.value
    expected = "pilot"
    assert actual == expected

    current_node = current_node.next
    actual = current_node.value
    expected = "astronaut"
    assert actual == expected

    current_node = current_node.next
    actual = current_node.value
    expected = "crewman"
    assert actual == expected

    actual = current_node.next
    expected = None
    assert actual == expected

# @pytest.mark.skip('pending')
def test_append_multiple(base_list):
    base_list.append("crewman")
    base_list.append("cadet")

    actual = str(base_list)
    expected = "{ pilot } -> { astronaut } -> { crewman } -> { cadet } -> NULL"
    assert actual == expected

# @pytest.mark.skip('pending')
def test_insert_before_middle(base_list):
    base_list.append("crewman")
    base_list.insert_before("astronaut", "lieutenant")

    actual = str(base_list)
    expected = "{ pilot } -> { lieutenant } -> { astronaut } -> { crewman } -> NULL"
    assert actual == expected


# @pytest.mark.skip('pending')
def test_insert_before_first(base_list):
    base_list.insert_before("pilot", "crewman")

    actual = str(base_list)
    expected = "{ crewman } -> { pilot } -> { astronaut } -> NULL"
    assert actual == expected

# @pytest.mark.skip('pending')
def test_insert_after_middle(base_list):
    base_list.append("crewman")
    base_list.insert_after("astronaut", "lieutenant")

    actual = str(base_list)
    expected = "{ pilot } -> { astronaut } -> { lieutenant } -> { crewman } -> NULL"
    assert actual == expected

# @pytest.mark.skip('pending')
def test_insert_end(base_list):
    base_list.insert_after("astronaut", "lieutenant")

    actual = str(base_list)
    expected = "{ pilot } -> { astronaut } -> { lieutenant } -> NULL"
    assert actual == expected

# @pytest.mark.skip('pending')
def test_insert_before(base_list):
    base_list.insert_before("pilot", "lieutenant")

    actual = str(base_list)
    expected = "{ lieutenant } -> { pilot } -> { astronaut } -> NULL"
    assert actual == expected
# @pytest.mark.skip('pending')
def test_no_match(base_list):
    base_list.insert_after("captain", "lieutenant")

    actual = str(base_list)
    expected = "{ pilot } -> { astronaut } -> NULL"
    assert actual == expected
# @pytest.mark.skip('pending')
def test_insert_before_match(base_list):
    base_list.insert_before("captain", "lieutenant")

    actual = str(base_list)
    expected = "{ pilot } -> { astronaut } -> NULL"
    assert actual == expected
