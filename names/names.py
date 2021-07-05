import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2.sort()
names_1.sort()

duplicates = []


# def binary_search(names, name):
#     middle = len(names) // 2
#     while len(names) > 1:
#         if name == names[middle]:
#             return duplicates.append(name)
#         elif name < names[middle]:
#             return binary_search(names[:middle], name)
#         elif name > names[middle]:
#             return binary_search(names[middle:], name)
#     return duplicates


# #duplicates = [x for x in names_1 if x in names_2]
# for n in names_1:
#     binary_search(names_2, n)

def new_binary_search(names, name, start=0, end=None):
    if end is None:
        end = len(names) - 1
    if start > end:
        return
    mid = (start + end) // 2
    if name == names[mid]:
        return duplicates.append(name)
    if name < names[mid]:
        return new_binary_search(names, name, start, mid - 1)
    if name > names[mid]:
        return new_binary_search(names, name, mid + 1, end)
    return duplicates


for n in names_1:
    new_binary_search(names_2, n)


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
