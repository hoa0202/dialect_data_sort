import os, json

dialect = []
all_dialect_count = 0

for curDir, dirs, files in os.walk("./2-018/"):
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json":
            with open (file_path, "r", encoding="utf-8") as json2:
                json_data = json.load(json2)
                for dialectInfo in json_data["transcription"]["segments"]:
                    if dialectInfo["pronunciation"] != None:
                        all_dialect_count += len(dialectInfo["dialect"].replace(' ',''))

print (all_dialect_count)