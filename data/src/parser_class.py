import json
from pprint import pprint

filename = 'courses_with_instructor.json'
data = json.load(open('full_courses.json'))
old_data = json.load(open('courses.json'))
id_to_professor = {}
for i in data:
	_id = i['course_id']
	if _id not in id_to_professor:
		_professor = i['instructor_name']
		id_to_professor[_id] = _professor
		print(_id + ', ' + _professor)
for i in old_data:
	_id = i['course_id']
	if _id in id_to_professor:
		i['instructor_name'] = id_to_professor[_id]
		print('instructor_name: ' + id_to_professor[_id])
with open(filename, 'w') as outfile:
	json.dump(old_data, outfile)