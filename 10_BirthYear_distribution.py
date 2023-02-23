import os, json
import collections

speakerId_and_birthYear = []

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json" and f[0] != ".":
            with open (file_path, "r", encoding="utf-8") as json2:
                json_data = json.load(json2)
                for speakerInfo in json_data["speaker"]:
                    speakerId = speakerInfo["speakerId"]
                    #birthYear = speakerInfo["birthYear"]
                    birthYear = float(speakerInfo["birthYear"])
                    if birthYear >= 1964.0:
                        birthYear= 1
                    elif birthYear >= 1954.0:
                        birthYear= 2
                    elif birthYear >= 1944.0:
                        birthYear= 3
                    elif birthYear >= 1934.0:
                        birthYear= 4
                    elif birthYear >= 1924.0:
                        birthYear= 5
                    speakerId_and_birthYear.append([speakerId, birthYear])
                    
#print(dict(speakerId_and_residencePeriod))
a = dict(speakerId_and_birthYear)
print(collections.Counter(a.values()))
d1 = sorted(collections.Counter(a.values()).items())
print(d1)