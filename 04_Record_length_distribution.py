import os, json


count_0sec = 0
count_30sec = 0
count_60sec = 0
count_90sec = 0
count_120sec = 0
count_150sec = 0

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

                all_time_count += 1

                if record_duration_list["recordDuration"] < 30:
                    count_0sec += 1
                elif record_duration_list["recordDuration"] >= 30 and record_duration_list["recordDuration"] < 60:
                    count_30sec += 1
                elif record_duration_list["recordDuration"] >= 60 and record_duration_list["recordDuration"] < 90:
                    count_60sec += 1
                elif record_duration_list["recordDuration"] >= 90 and record_duration_list["recordDuration"] < 120:
                    count_90sec += 1                   
                elif record_duration_list["recordDuration"] >= 120 and record_duration_list["recordDuration"] < 150:
                    count_120sec += 1
                elif record_duration_list["recordDuration"] >= 150:
                    count_150sec += 1




print("all count: ", all_time_count)
print("0 count: ", count_0sec)
print("30 count: ", count_30sec)
print("60 count: ", count_60sec)
print("90 count: ", count_90sec)
print("120 count: ", count_120sec)
print("150 count: ", count_150sec)
print("null count: ", all_time_count - count_0sec - count_30sec - count_60sec - count_90sec - count_120sec - count_150sec)

