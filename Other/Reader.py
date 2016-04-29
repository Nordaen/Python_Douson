print ("Открываю")
text_file = open("read_it.txt","r",encoding='utf-8')
text_file.close()

print("\nЧитаю файл посимвольно.")
text_file = open("read_it.txt","r")
print((text_file.read(1)))
print((text_file.read(5)))
text_file.close()

print("Читаю файл целиком")
text_file = open("read_it.txt","r",encoding='utf-8')
whole_thing=text_file.read()
print(whole_thing)
text_file.close()

print("\nЧитаю одну строку посимвольно")
text_file=open("read_it.txt","r",encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nЧитаю весь файл в список")
text_file = open("read_it.txt","r", encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("Перебираю файл построчно")
text_file = open("read_it.txt","r",encoding='utf-8')
for ine in text_file:
    print(line)
text_file.close()

