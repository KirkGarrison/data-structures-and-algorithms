from code_challenges.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest


def test_instance_psuedo_queue():
    assert PseudoQueue()

def test_is_psuedo_queue_enqueue():
    assert PseudoQueue.enqueue

def test_is_psuedo_queue_dequeue():
    assert PseudoQueue.dequeue

def test_psuedo_queue_enqueue():
    temp_queue = PseudoQueue()
    temp_queue.enqueue("1")
    actual = temp_queue.dequeue()
    expected = "1"
    assert actual == expected

def test_psuedo_queue_enqueue_multiple():
    temp_queue = PseudoQueue()
    temp_queue.enqueue("1")
    temp_queue.enqueue("2")
    temp_queue.enqueue("3")
    actual = temp_queue.dequeue()
    expected = "1"
    assert actual == expected

def test_psuedo_queue_enqueue_and_dequeue_multiple():
    temp_queue = PseudoQueue()
    temp_queue.enqueue("1")
    temp_queue.enqueue("2")
    temp_queue.enqueue("3")
    temp_queue.dequeue()
    temp_queue.dequeue()
    actual = temp_queue.dequeue()
    expected = "3"
    assert actual == expected

def test_psuedo_queue_dequeue_empty():
    temp_queue = PseudoQueue()
    with pytest.raises(IndexError):
        temp_queue.dequeue()
   
