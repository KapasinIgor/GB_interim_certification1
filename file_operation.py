import Note


def write_file(arr, mode):
    file = open("notes.csv", mode='w')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode)
    for notes in arr:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close()


def read_file():
    try:
        arr = []
        file = open("notes.csv", "r")
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(id=split_n[0], title=split_n[1], text=split_n[2], date=split_n[3])
            arr.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return arr