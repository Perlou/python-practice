# python 快速排序
# @author Perlou<perloukevin@gmail.con>

def quickSort(num_list):
    less = []
    pivotList = []
    more = []

    if len(num_list) <= 1:
        return num_list
    else: 
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)

        return less + pivotList + more
