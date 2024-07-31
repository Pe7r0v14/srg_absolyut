#library for using data base
import sqlite3
#library for using output and input data
from prompt import string as ps 
from prompt import integer as pi
#library for using data base method's
from work_in_db import add_data as add_d
from work_in_db import delete_data as del_d
from work_in_db import update_data as up_d
from work_in_db import vision_data as vis_d 
#library for work in operation system
import platform, os
#import win10toast

#functions for work in data bases
def main():
    push('SRG_ABSOLYUT','PROGRAMM START')
    first_user_enter = pi('Hello!What do you want?:\n1)Add product\n2)Delete product\n3)Update product\n4)Vision products\n>>')
    if first_user_enter == 4:
        enter_vision_product()
    elif first_user_enter == 2:
        enter_delete_product()
    elif first_user_enter ==3:
        enter_update_product()
    elif first_user_enter == 1:
        enter_add_product()
    else:
        pass

    #function add product in data base 
    #add_p('122333','331212',12152,12512,12512,12512)
    #function vision product in data base
    #vis_d()

def enter_add_product():

    print('ADD!')
    print("Hello, user, enter the data product!")
    categories = ps('Enter categories product\n>>')
    name_product = ps('Enter name product\n>>')
    code_product = pi('Enter code product\n>>')
    data_start = pi('Enter date start\n>>')
    finished = pi('Enter how month\n>>')
    value = pi('Enter value product\n>>')
    add_d(categories,name_product,code_product,data_start,finished,value)
    print('Product added!')

def enter_delete_product():
    #del_d()
    print('DELETE!')
    pass

def enter_update_product():
    print('UPDATE!')
    #up_d()
    pass

def enter_vision_product():
    print('VISION!')
    vis_d()

#functions for work operation system
def push(title, message):
    plt = platform.system()
    if plt == "Darwin":
        command = '''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
    elif plt == "Linux":
        command = f'''
        notify-send "{title}" "{message}"
        '''
    elif plt == "Windows":
        win10toast.ToastNotifier().show_toast(title, message)
        return
    else:
        return
    os.system(command)

def time_chek(finished):
    pass


if __name__ == '__main__':
    main()