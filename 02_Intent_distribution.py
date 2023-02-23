import os, json


EMOTIONS_NAME = ["REP", "EXP", "DES", "INT", "DIR", "PRO", "ETC"]

rep_emotions_count = 0
exp_emotions_count = 0
des_emotions_count = 0
int_emotions_count = 0
dir_emotions_count = 0
pro_emotions_count = 0
etc_emotions_count = 0

all_emotions_count = 0

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json" and f[0] != ".":
            with open (file_path, "r", encoding='UTF-8') as json2:
                json_data = json.load(json2)
                emotions_list = json_data["annotation"]["intents"]

                all_emotions_count += len(emotions_list)

                for emotion in emotions_list:
                    if emotion["tagType"] == "REP":
                        rep_emotions_count += 1
                    elif emotion["tagType"] == "EXP":
                        exp_emotions_count += 1
                    elif emotion["tagType"] == "DES":
                        des_emotions_count += 1
                    elif emotion["tagType"] == "INT":
                        int_emotions_count += 1
                    elif emotion["tagType"] == "DIR":
                        dir_emotions_count += 1
                    elif emotion["tagType"] == "PRO":
                        pro_emotions_count += 1
                    elif emotion["tagType"] == "ETC":
                        etc_emotions_count += 1                            
                    else:
                        print(file_path)


print("all emotions count: ", all_emotions_count)
print("rep emotions count: ", rep_emotions_count)
print("exp emotions count: ", exp_emotions_count)
print("des emotions count: ", des_emotions_count)
print("int emotions count: ", int_emotions_count)
print("dir emotions count: ", dir_emotions_count)
print("pro emotions count: ", pro_emotions_count)
print("etc emotions count: ", etc_emotions_count)   

if all_emotions_count == rep_emotions_count + exp_emotions_count + des_emotions_count + int_emotions_count + dir_emotions_count + pro_emotions_count + etc_emotions_count:
    print("ok")
