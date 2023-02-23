import os, json
import collections

speakerId_and_gender = []

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json" and f[0] != ".":
            with open (file_path, "r", encoding="utf-8") as json2:
                json_data = json.load(json2)
                for speakerInfo in json_data["speaker"]:
                    speakerId = speakerInfo["speakerId"]
                    gender = speakerInfo["gender"]
                    if gender == None :
                        print("null")
                    #if residencePeriod > 500 :
                    # print(file_path)
                    speakerId_and_gender.append([speakerId, gender])
                    
#print(dict(speakerId_and_residencePeriod))
a = dict(speakerId_and_gender)
print(collections.Counter(a.values()))
d1 = sorted(collections.Counter(a.values()).items())
print(d1)