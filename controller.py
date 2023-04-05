import function as func
import ui


def run():
    input_from_user = ''
    while input_from_user != '5':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            func.show('all')
        if input_from_user == '2':
            func.add()
        if input_from_user == '3':
            func.show('all')
            func.id_edit_del_show('del')
        if input_from_user == '4':
            func.show('all')
            func.id_edit_del_show('edit')
        if input_from_user == '5':
            ui.goodbye()
            break
