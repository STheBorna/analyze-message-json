import json

CHAT_JSON_PATH = "chat.json"

def open_json(file_path):
    with open(file_path,'r',encoding="utf-8") as f:
        data = json.load(f)
    return data

def count_total_messages(data):
    return len(data)

def count_person_message(data):
    dict_count_mess={}
    for message in data:
        dict_count_mess[message["from"]] = 0
    for message in data:
        if message["from"] in dict_count_mess.keys():
            dict_count_mess[message["from"]] += 1
    return dict_count_mess

def calc_percentage_message(count_message_person,total_messages):
    dict_p={}
    for person,count in count_message_person.items():
        percent = f"{(count / total_messages) * 100:.1f}"
        dict_p[person] = percent
    return dict_p

data = open_json(CHAT_JSON_PATH)
total_messages = count_total_messages(data)
count_m_p = count_person_message(data)
percentage = calc_percentage_message(count_m_p,total_messages)

print(count_m_p)
print(percentage)
#------

def separate_time(data:dict):
    dict_t = {}
    for message in data:
        message_time = message["time"][:2]
        dict_t[message_time] = 0
    return dict_t

def find_busiest_hour(data:dict,times_dict):
    dict_t = times_dict
    # for message in data:
    #     message_time = message["time"][:2]
    #     dict_t[message_time] = 0
    for message in data:
        msg_time=message["time"][:2]
        if msg_time in dict_t.keys():
            # print(message["time"][:2])
            dict_t[msg_time] +=1
    return max(dict_t.values())

dict_times = separate_time(data)
busy_hour = find_busiest_hour(data,dict_times)
print(busy_hour)