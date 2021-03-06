# coding=utf-8

import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *

class TestImmutableList(unittest.TestCase):
    def test_addNone(self):
        lst = DynamicArray()
        add_to_tail(lst,None)
        self.assertEqual(to_list(lst), [None])
        lst2 = DynamicArray([1,None,2])
        self.assertEqual(to_list(lst2), [1,None,2])

    def test_size(self):
        self.assertEqual(size(DynamicArray([])), 0)
        self.assertEqual(size(DynamicArray([1])), 1)
        self.assertEqual(size(DynamicArray([1, 2])), 2)

    def test_to_list(self):
        lst = [1, 2]
        a = DynamicArray(lst)
        b = to_list(a)
        self.assertEqual(lst, b)

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = from_list(e)
            self.assertEqual(to_list(lst), e)

    def test_add_to_head(self):
        DA1 = add_to_head(DynamicArray([]), 1)
        DA2 = DynamicArray([1])
        self.assertEqual(to_list(DA1), to_list(DA2))

    def test_add_to_tail(self):
        DA1 = add_to_tail(DynamicArray([1, 2]), 1)
        DA2 = DynamicArray([1, 2, 1])
        self.assertEqual(to_list(DA1), to_list(DA2))

    def test_find(self):
        a = DynamicArray([1, 2, 3])
        self.assertEqual(find(a, 1), True)

    def test_remove(self):
        a = DynamicArray([1, 2, 3])
        b = remove(a,1)
        self.assertEqual(to_list(b), [1,3])
        
    def test_filter(self):
        a = DynamicArray([1,2,2])
        b = filter(a,2)
        self.assertEqual(to_list(b), [1])

    def test_map(self):
        a = DynamicArray([1,2,3])
        b = map(a,str)
        self.assertEqual(to_list(b), ['1','2','3'])

    def test_reduce(self):
        # sum of empty list
        lst = DynamicArray()
        self.assertEqual(reduce(lst,(lambda st, e: st + e), 0), 0)
        # sum of list
        lst = DynamicArray()
        a = from_list([1, 2, 3])
        self.assertEqual(reduce(a,(lambda st, e: st + e), 0), 6)

    def test_mconcat(self):
        a = DynamicArray([1,2])
        b = DynamicArray([1,2])
        c = mconcat(a,b)
        self.assertEqual(to_list(c),[1,2,1,2])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)

    @given(st.lists(st.integers(), min_size=100))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        #0+a=a
        self.assertEqual(mconcat(mempty(), a), a)
        #a+0=a
        self.assertEqual(mconcat(a, mempty()), a)

    @given(a=st.lists(st.integers(), min_size=100),b=st.lists(st.integers()),c=st.lists(st.integers()))
    def test_monoid_associativity(self,a,b,c):
        lst1 = from_list(a)
        lst2 = from_list(b)
        lst3 = from_list(c)
        #(a+b)+c
        x = mconcat(mconcat(lst1, lst2),lst3)
        #a+(b+c)
        y = mconcat(lst1,mconcat(lst2, lst3))
        self.assertEqual(x,y)

    def test_iter(self):
        lst = DynamicArray([1,2,3,5])
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual([1,2,3,5], tmp)
        self.assertEqual(to_list(lst), tmp)

        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

if __name__ == '__main__':
    unittest.main()
