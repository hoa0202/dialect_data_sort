import os, json

EMOTIONS_NAME = ["positive", "negative", "irrelevant", "netural"]

positive_emotions_count = 0
negative_emotions_count = 0
irrelevant_emotions_count = 0
neutral_emotions_count = 0


all_emotions_count = 0

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json":
            with open (file_path, "r") as json2:
                json_data = json.load(json2)
                emotions_list = json_data["annotation"]["emotions"]

                all_emotions_count += len(emotions_list)

                for emotion in emotions_list:
                    if emotion["tagType"] == "positive":
                        positive_emotions_count += 1
                    elif emotion["tagType"] == "negative":
                        negative_emotions_count += 1
                    elif emotion["tagType"] == "irrelevant":
                        irrelevant_emotions_count += 1
                    elif emotion["tagType"] == "neutral":
                        neutral_emotions_count += 1
                    else:
                        print(file_path)


print("all emotions count: ", all_emotions_count)
print("positive emotions count: ", positive_emotions_count)
print("negative emotions count: ", negative_emotions_count)
print("irrelevant emotions count: ", irrelevant_emotions_count)
print("neutral emotions count: ", neutral_emotions_count)

if all_emotions_count == positive_emotions_count + negative_emotions_count + irrelevant_emotions_count + neutral_emotions_count:
    print("ok")