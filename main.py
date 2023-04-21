import collections
import typing

list_1 = [
	{
		"id": "1",
		"name": "Shrey",
		"age": 25
	},
	{
		"id": "3",
		"age": 10,
		"name": "Hello"
	},
	{
		"id": "2",
		"name": "World",
		"age": 24
	},
]

list_2 = [
	{
		"id": "1",
		"marks": 100
	},
	{
		"id": "3",
		"marks": 90,
		"roll_no": 11,
		"extra_info": {
			"hello": "world",
		},
	},
]

STUDENT_ID = str
STUDENT_INFO = typing.Dict


def merge_lists(list_1: typing.List[STUDENT_INFO], list_2: typing.List[STUDENT_INFO]) -> typing.List[STUDENT_INFO]:
	"""
	Complete this function, by merging the information from list_1 and list_2
	to create a new list, which has all the information about each student from
	both lists in one single dict.

	- Both lists are unsorted
	- Both lists can have missing values (for ex list_2 has missing id=2)
	"""
	student_id__student_info__mapper: typing.DefaultDict[STUDENT_ID, STUDENT_INFO] = collections.defaultdict(dict)
	for data in list_1 + list_2:
		id = data["id"]
		mapper_data = student_id__student_info__mapper[id]
		mapper_data.update(data)

	list_3: typing.List[STUDENT_INFO] = list(student_id__student_info__mapper.values())
	## uncomment below line if want a sorted result based on student id
	# list_3.sort(key=lambda x: x["id"])
	return list_3


list_3 = merge_lists(list_1, list_2)
print(list_3)
