"""Dynamic Array implementation
"""

import ctypes

class DynamicArrray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """returns length of the array

        Returns:
            int: length of the array
        """
        return self._size

    def __getitem__(self, index):
        """returns the element at a given index

        Args:
            index (int): the index at which the element should be returned

        Raises:
            IndexError: if the index is bigger than the array size

        Returns:
            Object: element at the given index
        """
        if not 0 <= index < self._size:
            raise IndexError('invalid index')
        return self._A[index]


    def append(self, element):
        """append an element to the array

        Args:
            element (Object): object to be appended to the array size
        """
        if self._size == self._capacity:
            self._resize_array(2 * self._capacity)
        self._A[self._size] = element
        self._size += 1
    
    def _resize_array(self, capacity):
        """resize the array with the given capacity

        Args:
            capacity (int): new capacity to be allocated
        """
        B = self._make_array(capacity)
        for k in range(self._size):
            B[k] = self._A[k]
        self._A = B
        self._capacity = capacity
    

    def _make_array(self, capacity):
        """function that creates an array

        Args:
            capacity (int): how long the array should be

        Returns:
            List: created array
        """
        return (capacity * ctypes.py_object)()

if __name__ == '__main__':
    dynamic_array = DynamicArrray()

    dynamic_array.append(4)
    print(f"The length of the array is: {len(dynamic_array)}")
    
    for i in range(10, 30, 2):
        dynamic_array.append(i)
    print(f"The length of the array is: {len(dynamic_array)}")

    print(f"The element at index 3 is {dynamic_array[3]}")