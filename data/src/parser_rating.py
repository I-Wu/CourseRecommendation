import requests
import json

URL = "http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=3966&callback=noCB&q=*%3A*+AND+schoolid_s%3A675&defType=edismax&qf=teacherfirstname_t%5E2000+teacherlastname_t%5E2000+teacherfullname_t%5E2000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=total_number_of_ratings_i+desc&siteName=rmp&rows=10&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s&fq="

r = requests.get(url = URL)
t = r.text
#json_data = json.loads(t)
#blah = requests.map(r)
#print(blah[0].json())
arr = t.split('{')
for i in arr:
	print('new instance\n')
	arr_child = i.split(',')
	for j in arr_child:
		print(j)
#professor = r.content.decode('utf8').replace("'", '"').replace("noCB", "").replace("(", "").replace(")", "").replace(";", "").replace("\n", "").replace("\t", "").strip()
#print(professor)
#professor = "".join(professor.split())
#json.load(professor)
#professor = r.content.decode('utf8')