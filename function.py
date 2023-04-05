import file_operation
import Note
import ui

min_num_char = 6


def add():
    note = ui.create_note(min_num_char)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    flag = True
    array = file_operation.read_file()
    for notes in array:
        if text == 'all':
            flag = False
            print(Note.Note.map_note(notes))
    if flag:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = file_operation.read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            flag = False
            if text == 'edit':
                note = ui.create_note(min_num_char)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_text(notes, note.get_text())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
    if flag:
        print('Заметки с таким id не найдено!')
    file_operation.write_file(array, 'a')
