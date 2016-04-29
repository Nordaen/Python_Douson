#
message = input("Введите текст. \n")
new_message = ""
VOWELS = "aeiouaeёиоуыэюя"
print()
for letter in message :
    if letter.lower() not in VOWELS:
        new_message +=letter
        print("Создана новая строка:",new_message)
    print("\nВот ваш текст с изъятыми гласными буквами:",new_message)
