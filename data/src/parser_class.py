import json
from pprint import pprint

filename = '../courses_with_courseid.json'
data = json.load(open('full_courses.json'))
old_data = json.load(open('courses.json'))
id_to_professor = {}
id_to_nyucourseid = {}
for i in data:
	_id = i['course_id']
	if _id not in id_to_professor:
		_professor = i['instructor_name']
		id_to_professor[_id] = _professor
		print(_id + ', ' + _professor)
	if _id not in id_to_nyucourseid:
		_nyucourseid = i['nyu_course_id']
		id_to_nyucourseid[_id] = _nyucourseid
		
for i in old_data:
	_id = i['course_id']
	if _id in id_to_professor:
		i['instructor_name'] = id_to_professor[_id]
		#print('instructor_name: ' + id_to_professor[_id])
	if _id in id_to_nyucourseid:
		i['nyu_course_id'] = id_to_nyucourseid[_id]
'''
for i in old_data:
	for k, v in i.items():
		if k == 'nyu_course_id':
			print(k + ' / ' + str(v) + '\n')
			break
'''
with open(filename, 'w') as outfile:
	json.dump(old_data, outfile)