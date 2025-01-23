from typing import List

class SortUtility:
    """
    A utility class to implement sorting algorithms for lists of integers.

    Methods:
    --------
    insertion_sort(arr: List[int]) -> List[int]:
        Sorts the given list of integers in decreasing order using the 
        Insertion Sort algorithm.

        Parameters:
        -----------
        arr : List[int]
            A list of integers to be sorted.

        Returns:
        --------
        List[int]
            A new list containing the integers sorted in decreasing order.

    merge_sort(arr: List[int]) -> List[int]:
        Sorts the given list of integers in decreasing order using the 
        Merge Sort algorithm.

        Parameters:
        ----------- 
        arr : List[int]
            A list of integers to be sorted.

        Returns:
        --------
        List[int]
            A new list containing the integers sorted in decreasing order.
    """
    def insertion_sort(self, arr: List[int]) -> List[int]:
        # Implement Insertion Sort to sort arr in decreasing order
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def merge_sort(self, arr: List[int]) -> List[int]:
        # Implement Merge Sort to sort arr in decreasing order

        #base case -> array of length <= 1 is already sorted
        if len(arr)<=1:
            return arr
        
        #recursive case -> split array recursively into two halves
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        sorted_arr = []
        i = j = 0

        #merge the sorted halves according to decreasing order
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        #append leftover elements from lefta and right halves
        while i < len(left):
            sorted_arr.append(left[i])
            i += 1

        while j < len(right):
            sorted_arr.append(right[j])
            j += 1
        
        return sorted_arr


