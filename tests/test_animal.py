import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.bob = Dog("Bob")


  def test_animal_creation(self):
    murph = Dog("Murph")
    self.assertIsInstance(murph, Dog)


  def test_dog_has_name(self):
    result = self.bob.get_name()
    expected = "Bob"
    self.assertEqual(result, expected)

  def test_can_set_species(self):
   self.assertEqual(self.bob.get_species(), "Dog")
   self.bob.set_species("Canine")
   self.assertEqual(self.bob.get_species(), "Canine")

  def test_animal_walking(self):
    animal = Animal()
    with self.assertRaises(ValueError):
      animal.walk()

  def test_set_legs(self):
    animal = Animal()
    animal.set_legs(12)
    animal.walk()
    speed = animal.speed
    # self.assertEqual(round(speed, 1), 1.2)
    self.assertEqual(speed, 1.2)


  # def test_dog_walk_when_no_legs(self):



if __name__=='__main__':
  unittest.main()