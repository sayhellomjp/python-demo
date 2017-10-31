import pickle, json

# d = dict(name='mjp', age=26)
# with open("D:\development\myCode\gitcode\python\demo\\test\\123.txt", 'wb') as f:
#     pickle.dump(d, f)

with open("D:\development\myCode\gitcode\python\demo\\test\\123.txt", 'rb') as f1:
    d = pickle.load(f1)
    print(d)


me = dict(name='rtt', age=27, address='leshan')
print(json.dumps(me))

str = '{"student_name": "majunpeng", "class": 8}'
python_obj = json.loads(str)
print(python_obj)

class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        "name": std.name,
        "age": std.age,
        "score": std.score
    }

s = Student('mjp', 18, 99)
print(s.name, s.age, s.score)

print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(dt):
    return Student(dt['name'], dt['age'], dt['score'])

json_str = '{"name": "mjp", "age": 18, "score": 99}'
print(json.loads(json_str, object_hook=dict2student))