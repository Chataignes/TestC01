import ex9_code as f
import unittest


class TestHeap(unittest.TestCase):
    def setUp(self):
        insert_list = [5, 9, 4, 6, 7, 2, 1, 8, 3]
        self._small_heap = f.Heap(insert_list)
        self._empty_heap = f.Heap([])

    def tearDown(self):
        print("Test Done")

    def test_default(self):
        self.assertEqual(self._small_heap._heap,
                         [9, 8, 4, 7, 6, 2, 1, 5, 3],
                         "__init__ method after inserting elements")
        self.assertEqual(self._empty_heap._heap,
                         [],
                         "__init__ method after inserting empty")

    def test_is_empty(self):
        self.assertTrue(self._empty_heap.is_empty(),
                        "False != True, it's an empty heap")
        self.assertFalse(self._small_heap.is_empty(),
                         "True != False, it's not an empty heap")

    def test_insert(self):
        self._small_heap.insert(0)
        self.assertEqual(self._small_heap._heap,
                         [9, 8, 4, 7, 6, 2, 1, 5, 3, 0],
                         "Inserting small element")
        self._small_heap.insert(10)
        self.assertEqual(self._small_heap._heap,
                         [10, 9, 4, 7, 8, 2, 1, 5, 3, 0, 6],
                         "Inserting big element")
        self._empty_heap.insert(10)
        self.assertEqual(self._empty_heap._heap,
                         [10],
                         "Inserting to an empty heap")

    def test_swap_and_violates(self):
        self._small_heap._swap(1, 2)
        self.assertEqual(self._small_heap._heap,
                         [9, 4, 8, 7, 6, 2, 1, 5, 3],
                         "Swaping elements")
        self.assertTrue(self._small_heap._violates(1), "Violates!")
        self.assertFalse(self._small_heap._violates(5),
                         "Doesn't Violate!")
        self.assertRaises(f.HeapEmptyError,
                          self._empty_heap._swap, 1, 2)

    def test_remove_top(self):
        self.assertRaises(f.HeapEmptyError, self._empty_heap.remove_top)
        top = self._small_heap.remove_top()
        self.assertEqual(self._small_heap._heap,
                         [8, 7, 4, 5, 6, 2, 1, 3],
                         "wrong heap after remove_top")
        self.assertEqual(top,
                         9,
                         "Return wrong top")

unittest.main(exit=False)
