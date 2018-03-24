from django.db import models

class Course():

    data = {}

    def __init__(self, cid, title, recommendation):
        """ Initialize a Course recommendation """
        self.id = cid
        self.title = title
        self.recommendation = recommendation

    @staticmethod
    def get_recommend(course_name):
    	return Course.data[course_name].recommendation

    