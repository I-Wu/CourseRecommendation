import json


with open('./title_test/course_batch_final_with_title_space.json') as data_file:    
    data = json.load(data_file)
    print(len(data))
    for k, v in data.items():
        if len(v) < 10:
            print("fuck")
            quit()
        print(k, ": ", len(v))
