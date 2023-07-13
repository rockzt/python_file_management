import file_actions as m
import json


user1 = {"username": "rock", "name":"rodri", "l_name":"zav"}
user2 = {"username": "rock2", "name":"rodri2", "l_name":"zav2"}
user_list = [user1, user2]
json_user_list = json.dumps(user_list)

try:
  m.create_file("sample.txt","")
except OSError as error:
  print("Could not create file -> ", error)


try:
  m.modify__file("sample.txt", json_user_list, False)
except ValueError as error:
  print("Could not update file -> " , error)


try:
  output = m.read_file("sample.txt")
  print(f'Text Contained -> {output}')
except ValueError as error:
  print("Could not read file -> " , error)

print("Program Done!!")
