import os, json
import collections

speakerId_and_job = []

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json":
            with open (file_path, "r", encoding="utf-8") as json2:
                json_data = json.load(json2)
                for speakerInfo in json_data["speaker"]:
                    speakerId = speakerInfo["speakerId"]
                    job = speakerInfo["job"]
                    speakerId_and_job.append([speakerId, job])

#print(dict(speakerId_and_residencePeriod))
a = dict(speakerId_and_job)
print(collections.Counter(a.values()))