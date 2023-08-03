"""4: sort the following list without using sort() function
[1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]"""
l = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
def counting_sort(l):
    count ={0:0, 1:0}
    for num in l:
        count[num] += 1

    sorted_l= []
    for i in range(2):
        sorted_l.extend([i] * count[i])

    return sorted_l


sorted_list = counting_sort(l)
print(sorted_list)
