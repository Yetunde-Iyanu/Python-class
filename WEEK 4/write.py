# Writing a file in Python
txt_data = "I am a detailed Software Engineer"

file_path = 'Result.txt'
with open(file_path, 'w') as file:
 file.write (txt_data)
 print(f"txt file '{file_path} was created")

 #Reading a file
 txt_data = "Obviously, doing my best to be good at what i do"

file_path = 'Input.txt'
try:
 with open(file_path, 'r') as file:
  file.write (txt_data)
  print(f"txt file '{file_path} was created")
except FileNotFoundError:
    print("File not found ")

