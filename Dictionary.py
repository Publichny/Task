# #Task - 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# res_dict = dict(zip(keys, values))
# print(res_dict)
#
#
# #Task - 2
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)
#
# #Task - 3
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict['class']['student']['marks']['history'])


# #Task - 4
#
# sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# keys = ["name", "salary"]
# res = {k: sample_dict[k] for k in keys}
# print(res)

# #Task-6
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys_to_remove = ["name", "salary"]
# filtered_dict = {}
# for key, value in sample_dict.items():
#     if key not in keys_to_remove:
#         filtered_dict[key] = value
#
# print(filtered_dict)


# #Task - 7
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 present in a dict')


# #Task - 8
# sample_dict = {
#   "name": "Kelly",
#   "age": 25,
#   "salary": 8000,
#   "city": "New York"
# }
#
# sample_dict["location"] = sample_dict["city"]
# del sample_dict["city"]
# print(sample_dict)


# #Task - 9
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# min_key = min(sample_dict, key=lambda k: sample_dict[k])
# print(min_key)
#
# #Solution 2
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# min_key = min(sample_dict, key=sample_dict.get)
# print(min_key)

# #Task - 10
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }
#
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)

