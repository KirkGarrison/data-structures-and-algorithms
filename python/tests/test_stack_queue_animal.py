from code_challenges.stack_queue_animal_shelter.stack_queue_animal import AnimalShelter, Dog, Cat
import pytest

def test_animal_shelter():
    animal_shelter = AnimalShelter
    assert animal_shelter

def test_dog():
    dog = Dog
    assert dog

def test_cat():
    cat = Cat
    assert cat


def test_enqueue_dog():
    animal_shelter = AnimalShelter()
    dog = Dog("Felix")
    animal_shelter.enqueue(dog)
    actual = animal_shelter.enqueue_box.peek().name
    expected = "Felix"
    assert actual == expected

def test_enqueue_one_dog_and_cat():
    animal_shelter = AnimalShelter()
    dog = Dog("Felix")
    cat = Cat("snuggles")
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    actual = animal_shelter.enqueue_box.peek().name
    expected = "snuggles"
    assert actual == expected

def test_dequeue_animal():
    animal_shelter = AnimalShelter()
    dog = Dog("Felix")
    animal_shelter.enqueue(dog)
    actual = animal_shelter.dequeue().name
    expected = "Felix"
    assert actual == expected

def test_dequeue_no_animals():
    animal_shelter = AnimalShelter()
    with pytest.raises(IndexError):
        animal_shelter.dequeue("cat")


def test_dequeue_a_cat_and_dogs():
    animal_shelter = AnimalShelter()
    dog = Dog("Felix")
    cat = Cat("snuggles")
    other_dog = Dog("Zeus")
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    animal_shelter.enqueue(other_dog)
    actual = animal_shelter.dequeue("cat").name
    expected = "snuggles"
    assert actual == expected

def test_dequeue_top_priority_animal():
    animal_shelter = AnimalShelter()
    dog = Dog("Felix")
    cat = Cat("snuggles")
    other_dog = Dog("Zeus")
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    animal_shelter.enqueue(other_dog)
    actual = animal_shelter.dequeue().name
    expected = "Felix"
    assert actual == expected

def test_dequeue_a_dog_and_cats():
    animal_shelter = AnimalShelter()
    cat = Cat("Little one")
    dog = Dog("Felix")
    cat = Cat("snuggles")
    animal_shelter.enqueue(cat)
    animal_shelter.enqueue(dog)
    animal_shelter.enqueue(cat)
    actual = animal_shelter.dequeue("dog").name
    expected = "Felix"
    assert actual == expected

