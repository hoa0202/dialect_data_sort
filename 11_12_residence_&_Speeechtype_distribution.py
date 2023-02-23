import os, json


TIME_DATA = ["gw", "gs", "recordDuration_total", "recordDuration_gw", "recordDuration_gs"]

gw_count = 0
gs_count = 0
cc_count = 0
jj_count = 0
jl_count = 0

recordDuration_total = 0

recordDuration_gw = 0
recordDuration_gs = 0
recordDuration_cc = 0
recordDuration_jj = 0
recordDuration_jl = 0

recordDration_Speak = 0
recordDration_speak = 0
recordDration_Read = 0

recordDuration_city = 0

speak_type_count = 0
Speak_type_count = 0
Read_type_count = 0
city_dict = {}

gw_Speak_count = 0
gw_speak_count = 0
gw_Read_count = 0

gs_Speak_count = 0
gs_speak_count = 0
gs_Read_count = 0

cc_Speak_count = 0
cc_speak_count = 0
cc_Read_count = 0

jj_Speak_count = 0
jj_speak_count = 0
jj_Read_count = 0

jl_Speak_count = 0
jl_speak_count = 0
jl_Read_count = 0

recordDration_Speak_gw = 0
recordDration_speak_gw = 0
recordDration_Read_gw = 0

recordDration_Speak_gs = 0
recordDration_speak_gs = 0
recordDration_Read_gs = 0

recordDration_Speak_cc = 0
recordDration_speak_cc = 0
recordDration_Read_cc = 0

recordDration_Speak_jj = 0
recordDration_speak_jj = 0
recordDration_Read_jj = 0

recordDration_Speak_jl = 0
recordDration_speak_jl = 0
recordDration_Read_jl = 0

#for curDir, dirs, files in os.walk("./충청,전라,제주/"):
for curDir, dirs, files in os.walk("./강원,경상/"):
    
    for f in files:
        file_path = os.path.join(curDir, f)
        if file_path[-4:] == "json" and f[0] != ".":
        
            with open (file_path, "r", encoding="UTF-8") as json2:
                json_data = json.load(json2)
                speaker_list = json_data["speaker"]
                speaker_residence = json_data["collector"]["residenceProvince"]
                speaker_city = json_data["collector"]["residenceCity"]
                recordDuration = json_data["audio"]["recordDuration"]
                speak_type = json_data["script"]["speechType"]

                
                for speaker in speaker_list:
                    
                    if speaker["residenceProvince"] == "gw":
                        gw_count += 1
                        recordDuration_gw += recordDuration   
                        if speak_type == "Speak":
                            gw_Speak_count += 1
                            recordDration_Speak_gw += recordDuration
                        elif speak_type == "speak":
                            gw_speak_count += 1
                            recordDration_speak_gw += recordDuration
                        elif speak_type == "Read":
                            gw_Read_count += 1
                            recordDration_Read_gw += recordDuration

                    elif speaker["residenceProvince"] == "gs":
                        gs_count += 1
                        recordDuration_gs += recordDuration
                        if speak_type == "Speak":
                            gs_Speak_count += 1
                            recordDration_Speak_gs += recordDuration
                        elif speak_type == "speak":
                            gs_speak_count += 1
                            recordDration_speak_gs += recordDuration
                        elif speak_type == "Read":
                            gs_Read_count += 1
                            recordDration_Read_gs += recordDuration

                    elif speaker["residenceProvince"] == "cc":
                        cc_count += 1
                        recordDuration_cc += recordDuration
                        if speak_type == "Speak":
                            cc_Speak_count += 1
                            recordDration_Speak_cc += recordDuration
                        elif speak_type == "speak":
                            cc_speak_count += 1
                            recordDration_speak_cc += recordDuration
                        elif speak_type == "Read":
                            cc_Read_count += 1                   
                            recordDration_Read_cc += recordDuration 

                    elif speaker["residenceProvince"] == "jj":
                        jj_count += 1
                        recordDuration_jj += recordDuration
                        if speak_type == "Speak":
                            jj_Speak_count += 1
                            recordDration_Speak_jj += recordDuration
                        elif speak_type == "speak":
                            jj_speak_count += 1
                            recordDration_speak_jj += recordDuration
                        elif speak_type == "Read":
                            jj_Read_count += 1 
                            recordDration_Read_jj += recordDuration

                    elif speaker["residenceProvince"] == "jl":
                        jl_count += 1
                        recordDuration_jl += recordDuration
                        if speak_type == "Speak":
                            jl_Speak_count += 1
                            recordDration_Speak_jl += recordDuration
                        elif speak_type == "speak":
                            jl_speak_count += 1
                            recordDration_speak_jl += recordDuration
                        elif speak_type == "Read":
                            jl_Read_count += 1 
                            recordDration_Read_jl += recordDuration
                
                speaker_count = len(json_data["speaker"])
                if city_dict.get(speaker_city):
                    city_dict[speaker_city] = {
                        "speaker_city_count": city_dict[speaker_city]["speaker_city_count"] + speaker_count,
                        "recordDuration": city_dict[speaker_city]["recordDuration"] + recordDuration
                    }
                else:
                    city_dict[speaker_city] = {
                        "speaker_city_count": speaker_count,
                        "recordDuration": recordDuration
                    }


print("recordDuration_gw: ", recordDuration_gw)
print("recordDuration_gs: ", recordDuration_gs)
print("recordDuration_cc: ", recordDuration_cc)
print("recordDuration_jj: ", recordDuration_jj)
print("recordDuration_jl: ", recordDuration_jl)

print("gw_count: ", gw_count)
print("gs_count: ", gs_count)
print("cc_count: ", cc_count)
print("jj_count: ", jj_count)
print("jl_count: ", jl_count)

print("Speak_type_count: ", Speak_type_count)
print("speak_type_count: ", speak_type_count)
print("Read_type_count: ", Read_type_count)

print("Speak_recordDration: ", recordDration_Speak)
print("speak_recordDration: ", recordDration_speak)
print("Read_recordDration: ", recordDration_Read)

print("city_dict: ", city_dict)

print("gw gs Speak type : ", recordDration_Speak_gw + recordDration_Speak_gs)
print("gw gs speak type : ", recordDration_speak_gw + recordDration_speak_gs)
print("gw gs Read type : ", recordDration_Read_gw + recordDration_Read_gs)

print("cc jj jl Speak type : ", recordDration_Speak_cc + recordDration_Speak_jj + recordDration_Speak_jl)
print("cc jj jl speak type : ", recordDration_speak_cc + recordDration_speak_jj + recordDration_speak_jl)
print("cc jj jl Read type : ", recordDration_Read_cc + recordDration_Read_jj + recordDration_Read_jl)