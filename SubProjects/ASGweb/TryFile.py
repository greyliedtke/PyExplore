from PyAsgDB import *


def temp_funcs():
    q_string = 'ALTER TABLE Poems Add Content'
    q_string = 'CREATE TABLE Poems (poem_id INTEGER PRIMARY KEY, Title TEXT NOT NULL UNIQUE, Author TEXT, Privacy TEXT, Content TEXT, Date TEXT, Category TEXT, Metric TEXT, Comments TEXT, Rating TEXT)'
    # id, title, author, privacy, category, metric, date, comments, likes
    # dataset_query(q_type='Delete_Table', t_delete='State_Capitals_ds')
    cp_db_query(q_type='Custom', q_string=q_string)
    #dataset_query(q_type='Generic_Select_Where', q_table='inject')

temp_funcs()

#Done



"""
#SQL Notes


create table = 'Create TABLE QwhizSets (set_id INTEGER PRIMARY KEY, SetName TEXT NOT NULL UNIQUE, SetType TEXT, Admins TEXT)'
insert table = "INSERT INTO QwhizSets (set_id, SetName, SetType, Admins) VALUES(1, 'Thai_ds', 'Public', 'ADMIN')"

"""