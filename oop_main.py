import json
class Message:
    def __init__(self,file_path):
        self.path=file_path
        self.data:dict=None
    def open_json(self):
        with open(self.path,'r',encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data
    def count_total_messages(self):
        return len(self.data)
    def count_person_message(self):
        dict_count_mess={}
        for message in self.data:
            dict_count_mess[message["from"]] = 0
        for message in self.data:
            if message["from"] in dict_count_mess.keys():
                dict_count_mess[message["from"]] += 1
        return dict_count_mess
    def calc_percentage_message(self,count_message_person:dict,total_messages):
        dict_p={}
        for person,count in count_message_person.items():
            percent = f"{(count / total_messages) * 100:.1f}"
            dict_p[person] = percent
        return dict_p

    def separate_time(self):
        dict_t = {}
        for message in self.data:
            message_time = message["time"][:2]
            dict_t[message_time] = 0
        return dict_t
    def find_busiest_hour(self):
        dict_t = self.separate_time()
        for message in self.data:
            msg_time=message["time"][:2]
            if msg_time in dict_t.keys():
                dict_t[msg_time] +=1
        return max(dict_t.values())

    def count_letter(self):
        dict_m={}
        for message in self.data:
            dict_m[message["from"]] = 0
        for message in self.data:
            dict_m[message["from"]] += len(message["text"])
        return dict_m
    def coung_avg_message(self):
        count_message_char = self.count_letter()
        count_message_person = self.count_person_message()
        dict_y={}
        for person, char_count in count_message_char.items():
            message_count = count_message_person[person]
            avg = f"{char_count / message_count:.1f}"
            dict_y[person] = avg
        return dict_y

    
path_f = "chat.json"
message = Message(path_f)
data = message.open_json()
total_messages = message.count_total_messages()
count_m_p = message.count_person_message()
percentage = message.calc_percentage_message(count_m_p,total_messages)

print(count_m_p)
print(percentage)

busy_hour = message.find_busiest_hour()
print(busy_hour)

print(message.count_letter())
print(message.coung_avg_message())