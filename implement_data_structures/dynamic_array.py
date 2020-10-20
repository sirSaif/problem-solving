import ctypes


class DynamicArray:
    def __init__(self):
        # number of current items
        self._curr_elements_num = 0
        # the capacity of the array
        self._capacity = 1
        # construct low level array using ctype module by non public _make_low_level_arr method
        self._low_level_arr = self._make_low_level_arr(self._capacity)

    def __getitem__(self, item):
        # does not support negative indexing, yet
        if not 0 <= item < self._curr_elements_num:
            raise ImportError("Invalid Index")
        return self._low_level_arr[item]

    def append(self, obj):
        # if all available array cells are exhausted, we double array capacity
        # using private _resize method
        if self._curr_elements_num == self._capacity:
            self._resize(2 * self._capacity)
        # if there is a free cells, _curr_elements_num refers to the index next the last occupied one
        self._low_level_arr[self._curr_elements_num] = obj
        # after appending the obj, _curr_elements_num incremented by one
        self._curr_elements_num += 1

    def _resize(self, capacity):
        # construct new low level array by private _make_low_level_arr method
        new_arr = self._make_low_level_arr(capacity)
        # assigning all values of old array to the new one
        for i in range(self._capacity):
            new_arr[i] = self._low_level_arr[i]
        # reassign reference array to the new one
        self._low_level_arr = new_arr
        # reassign capacity
        self._capacity = capacity

    def _make_low_level_arr(self, capacity):
        return (capacity * ctypes.py_object)()


A = DynamicArray()
A.append(10)