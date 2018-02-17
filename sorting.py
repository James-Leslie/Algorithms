def bubble_sort(unsorted):

    """ BUBBLE SORT ALGORITHM O(n^2)

    1. Start at beginning of data set
    2. Compare first two elements
        if first > second: swap elements
    3. Compare next two elements, repeat until end of data set
    4. Repeat steps 1 - 3 until no more swaps means list is sorted"""

    changed = True

    while changed:
        changed = False
        for i in range(len(unsorted) - 1):
            if unsorted[i] > unsorted[i+1]:
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
                changed = True

    return None


array = [2, 6, 1, 7, 3, 9, 2, 1]

bubble_sort(array)

print(array)
