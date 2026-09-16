import json
class Message:
    def __init__(self,file_path):
        self.path=file_path
        self.data=None
    def open_json(self):
        with open(self.file_path,'r',encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data
    def count_total_messages(self):
        return len(self.data)