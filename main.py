import file_actions as m

m.create_file("sample.txt", "some_text")
m.modify__file("sample.txt", "Some more text added", False)
print(m.read_file("sample.txt"))
