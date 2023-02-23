import os, json


EMOTIONS_NAME = ["가족", "농경", "의", "식", "주", "자연", "건강", "풍속", "응급상황"]

family_count = 0
farming_count = 0
dress_count = 0
food_count = 0
house_count = 0
nature_count = 0
health_count = 0
custom_count = 0
emergency_count = 0

all_time_count = 0

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json" and f[0] != ".":
            with open (file_path, "r", encoding='UTF-8') as json2:
                json_data = json.load(json2)
                emotions_list = json_data["script"]
                record_duration_list = json_data["audio"]

                all_time_count += record_duration_list["recordDuration"]

                if emotions_list["domain"] == "가족":
                    family_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "농경":
                    farming_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "의":
                    dress_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "식":
                    food_count += record_duration_list["recordDuration"]                    
                elif emotions_list["domain"] == "주":
                    house_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "자연":
                    nature_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "건강":
                    health_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "풍속":
                    custom_count += record_duration_list["recordDuration"]
                elif emotions_list["domain"] == "응급상황":
                    emergency_count += record_duration_list["recordDuration"]




print("all count: ", all_time_count)
print("family count: ", family_count)
print("farming count: ", farming_count)
print("dress count: ", dress_count)
print("food count: ", food_count)
print("house count: ", house_count)
print("nature count: ", nature_count)
print("health count: ", health_count)
print("custom count: ", custom_count)
print("emergency count: ", emergency_count)
print("null count: ", all_time_count - family_count - farming_count - dress_count - food_count - house_count - nature_count - health_count - custom_count - emergency_count)

