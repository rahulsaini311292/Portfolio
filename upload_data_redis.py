"""
    This file will run before running portfolio app.
    Objective of this fill is to add data in redis.
    This data will later be retrieved via apis.

"""

import redis
import json


class RedisData:

    def __init__(self):
        self.redis_obj = redis.Redis(db=0)
        self.data = {
            "name": "Your Name",
            "email": "yourname@gmail.com",
            "linkedin": "https://www.linkedin.com/in/yourid/",
            "github": "https://github.com/yourid",
            "summary": [
                "6+ years of extensive experience in development of web applications.",
                "Domain knowledge: Supply Chain Management, web applications, Integration.",
                "Good understanding of core Python and OOPS concepts.",
                "Good understanding of SDLC",
                "Experience in testing processes-Test Scenario and Test Case Creation, Test Case Execution and Defect "
                "Logging, Tracking and Closure, Reporting.",
                "Experience in API Development using REST and Postman."
            ],
            "skills": [
                "Python",
                "FastAPI",
                "Django",
                "Redis",
                "Celery",
                "MongoDB",
                "REST",
                "Unit Test",
                "HTML/CSS",
                "jQuery",
                "ReactJS",
                "MySQL",
                "PostgreSQL",
                "GIT",
                "AGILE",
                "Postman",
                "Elasticsearch"
            ],
            "experience": [
                {
                    "Company Name 1": {
                        "period": "MAY 2017 - JUNE 2019",
                        "designation": "Software Engineer",
                        "project": "Project Name",
                        "client": "Client Name",
                        "about_app": "Description",
                    },
                    "Company Name 2": {
                        "period": "JULY 2019 - JUNE 2021",
                        "designation": "Application Developer 2",
                        "project": "Project Name",
                        "about_app": "Description",
                    },
                    "Company Name 3": {
                        "period": "JULY 2021 - Present",
                        "designation": "Software Developer 2",
                        "project": "Project Name",
                        "about_app": "Description",
                    }
                }
            ],
            "education": "BTech 2011-2015"
        }

    def add_data_to_redis(self):
        self.redis_obj.set("about_me", json.dumps(self.data))
        print("data added")


# class object

redis_data_obj = RedisData()
redis_data_obj.add_data_to_redis()
