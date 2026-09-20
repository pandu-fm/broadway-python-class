
data_from_different_source = ["ktm", "pkr", "bkt", "lalitpur", "pkr",'bkt']

filtered_data = set(data_from_different_source)
print(filtered_data)


numbers_1 = {1,2,3,4}
numbers_2 = {1,6,7,4, 1, 1, 1}

result = numbers_1 | numbers_2
result.add(100)
# result.remove(1)

print(result)

