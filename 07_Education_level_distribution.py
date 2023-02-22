import os, json
import matplotlib.pyplot as plt
import collections

speakerId_and_academicBackground = []

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json" and f[0] != ".":
            with open (file_path, "r", encoding="utf-8") as json2:
                json_data = json.load(json2)
                for speakerInfo in json_data["speaker"]:
                    speakerId = speakerInfo["speakerId"]
                    academicBackground = speakerInfo["academicBackground"]
                    if academicBackground == None :
                        print("null")
                    # print(file_path)
                    speakerId_and_academicBackground.append([speakerId, academicBackground])

#print(dict(speakerId_and_residencePeriod))
a = dict(speakerId_and_academicBackground)
print(collections.Counter(a.values()))
d1 = sorted(collections.Counter(a.values()).items())
print(d1)
