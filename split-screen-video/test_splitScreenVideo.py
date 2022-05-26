import unittest
from splitScreenVideo import next

class TestNext(unittest.TestCase):

    def test_1(self):
        ordered1 = [1, 2, 3]
        ordered2 = [1, 2, 3]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 0)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 2)
        self.assertEqual(i2, 2)     
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1) )
        self.assertEqual(i2, len(ordered2))

    def test_2(self):
        ordered1 = [1, 2, 3]
        ordered2 = [2, 3]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, -1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 2)
        self.assertEqual(i2, 1)     
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_3(self):
        ordered1 = [20, 30]
        ordered2 = [10, 20, 30]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, -1)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 2)     
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_4(self):
        ordered1 = [1, 2, 3]
        ordered2 = [1, 3]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 2)
        self.assertEqual(i2, 1)     
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_5(self):
        ordered1 = [1, 3]
        ordered2 = [1, 2, 3]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 0)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 2)     
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_6(self):
        ordered1 = [1, 2, 3, 4, 5]
        ordered2 = [2, 4]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, -1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 2)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 3)
        self.assertEqual(i2, 1)     

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 4)
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_7(self):
        ordered1 = [2, 4]
        ordered2 = [1, 2, 3, 4, 5]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, -1)
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 2)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)     
        self.assertEqual(i2, 3)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 4)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_8(self):
        ordered1 = [1, 2]
        ordered2 = [3, 4]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, -1)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, -1)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, 0)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_9(self):
        ordered1 = [3, 4]
        ordered2 = [1, 2]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, -1)
        self.assertEqual(i2, 0)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, -1)
        self.assertEqual(i2, 1)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, len(ordered1))

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, len(ordered1))

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

    def test_10(self):
        ordered1 = [1, 2,    4, 5]
        ordered2 = [1,    3, 4   ]

        i1 = i2 = -1
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 0)
        self.assertEqual(i2, 0)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 0)
        
        i1, i2 = next(ordered1, i1, ordered2, i2)
        # Repeat ordered1's "2" in place of the dropped "3".
        self.assertEqual(i1, 1)
        self.assertEqual(i2, 1)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 2)
        self.assertEqual(i2, 2)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, 3)
        self.assertEqual(i2, 2)

        i1, i2 = next(ordered1, i1, ordered2, i2)
        self.assertEqual(i1, len(ordered1))
        self.assertEqual(i2, len(ordered2))

if __name__ == "__main__":
    unittest.main()