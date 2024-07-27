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


def welcome():
    first_user_enter = ps('Hello!What do you want?:\n1)Add product\n2)Delete product\n3)Update product\n4)Vision products\n>>')
    if first_user_enter == 'Add product' or 1:
        enter_add_product()
    elif first_user_enter == 'Delete product' or 2:
        enter_delete_product()
    elif first_user_enter == 'Update product' or 3:
        enter_update_product()
    elif first_user_enter == 'Vision products' or 4:
        enter_vision_product()
    else:
        pass

    #function add product in data base 
    #add_p('122333','331212',12152,12512,12512,12512)
    #function vision product in data base
    #vis_d()

def enter_add_product():
    #add_d()
    pass

def enter_delete_product():
    #del_d()
    pass

def enter_update_product():
    #up_d()
    pass

def enter_vision_product():
    #vis_d
    pass


welcome()