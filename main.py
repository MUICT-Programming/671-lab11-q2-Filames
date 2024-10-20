list1 = []
list2 = []
ip = int(input())

for i in range(ip):
    member = input()
    list1.append(member)

for i in range(ip):
    member = input()
    list2.append(member)

def summation(list1, list2):
    updated_list = []
    for i in range(ip):
        newmember = int(list1[i]) + int(list2[i])
        updated_list.append(newmember)
    print(updated_list)
    return updated_list

def find_min_max(updated_list):
    updated_list.sort()
    print(f'({updated_list[0]}, {updated_list[-1]})')

updated_list = summation(list1, list2)
find_min_max(updated_list)
