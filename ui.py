import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите заголовок заметки: '), number)
    text = check_len_text_input(
        input('Введите текст заметки: '), number)
    return Note.Note(title=title, text=text)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:"
          "\n\n1 - вывод всех заметок из файла"
          "\n2 - добавление заметки"
          "\n3 - удаление заметки"
          "\n4 - редактирование заметки"
          "\n5 - выход"
          "\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def goodbye():
    print("До новых встреч!")