# def   heapify_down(arr,n,index):
#     lchild_idx = 2 * index + 1
#     rchild_idx = 2 * index + 2
#     largest = index
#     if lchild_idx < n and arr[lchild_idx] > arr[largest]:
#         largest = lchild_idx
#     if rchild_idx < n and arr[rchild_idx] > arr[largest]:
#         largest = rchild_idx
#     if  largest != index:
#         arr[largest],arr[index] = arr[index],arr[largest]
#         heapify_down(arr,n,index)
#
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n // 2 -1,-1,-1):
#         heapify_down(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[i],arr[0] = arr[0],arr[i]
#         heapify_down(arr,i,0)
#
#
#
#
# u = [5,9,7,2,1,3]
# heap_sort(u)
# print(u)








def heapdown(arr,n,index):
    lchild_idx = 2 * index + 1
    rchild_idx =  2 * index + 2
    largest  = index
    if lchild_idx < n and arr[lchild_idx] >  arr[largest]:
        largest = lchild_idx
    if rchild_idx < n and arr[rchild_idx]  > arr[largest]:
        largest  = rchild_idx
    if largest != index:
        arr[largest],arr[index] = arr[index],arr[largest]
        heapdown(arr,n,largest)



def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 -1 ,-1,-1):
        heapdown(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapdown(arr,i,0)



o = [5,3,67,4,36,577,345]
heap_sort(o)
print(o)






























