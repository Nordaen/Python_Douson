#
print("Создаю текстовый файл методом вайрлайнес")
text_file = open("write_it.txt","w",encoding='utf-8')
lines=["Строка 1\n",
"stroka 2\n"
"stroka 3\n"]
text_file.writelines(lines)
text_file.close()

print("Читаю свою ебатню")
text_file = open("write_it.txt","r",encoding='utf-8')
print(text_file.read())
text_file.close()


