import sqlite3
from sqlite3 import Error


# Clean results for tuple and string var formats
def clean_drop(d_input):
    if type(d_input) is float:
        # do nothing for floats???
        lol = 'ok'
    if type(d_input) is tuple and len(d_input) < 2:
        d_input = d_input[0]
    if type(d_input) is str:
        d_input = d_input.replace("('", "").replace("',)", "")
    return d_input


# Connection manager
def conn_manager(query, args=None):
    conn = sqlite3.connect("AsgDB.db")
    c = conn.cursor()
    # print(query, args)
    if args is None:
        try:
            c.execute(query)
        except 'Query Error':
            print("QueryError")
    else:
        try:
            c.execute(query, args)
        except 'Query Error':
            print("QueryError")
    q_result = c.fetchall()
    cleaned = []
    if len(q_result) > 0:
        for cleaner in q_result:
            clean = clean_drop(cleaner)
            cleaned.append(clean)
    conn.commit()
    conn.close()
    return cleaned


# ------------------------------------------ The Beast Query -----------------------------------------------------------
# Function that will do all queries to the datasets
def cp_db_query(**kargs):
    # Used in cp Ping!!!
    q_type = kargs.get("q_type")
    query_string = ''
    if q_type == "Show_cp":
        query_string = f"SELECT rowid, * FROM RemoteServers"

    elif q_type == "Table_columns":
        # Display table columns
        q_table = kargs.get('q_table')
        query_string = f"PRAGMA table_info('{q_table}')"

    result = conn_manager(query_string)
    return result


# Query parametrized...
def cp_db_query_p(**kargs):
    q_type = kargs.get("q_type")
    query_string = ''
    args = ''

    if q_type == "Show_cp_where":
        args = kargs.get('q_cp_id')
        query_string = f"SELECT rowid, * FROM RemoteServers WHERE rowid = ?"
    # Update cradle point on ping
    elif q_type == "update_cp_ping":
        args = kargs.get('q_cp_args')
        query_string = f"UPDATE RemoteServers SET wbctrl_stat = ?, wbctrl_stat_ls= ?, hs_stat = ?, rd_stat = ?, " \
                       f"last_ref = ? " \
                       f"WHERE rowid = ?"
    elif q_type == "update_cp_info":
        # Update database values
        args = kargs.get('q_cp_args')
        query_string = f"UPDATE RemoteServers SET project= ?, programmer = ?, notes = ? " \
                       f"WHERE rowid = ?"
    elif q_type == "Delete_cp_ID":
        # Delete using id
        args = kargs.get('q_cp_args')
        query_string = f"DELETE FROM RemoteServers WHERE rowid = ?"
    elif q_type == "New_cp":
        # Add New Entry to database
        args = kargs.get('q_cp_args')
        query_string = f"INSERT INTO RemoteServers (ip_add, project, programmer, notes)" \
                       f"VALUES(?, ?, ?, ?)"

    # Perform Query
    result = conn_manager(query=query_string, args=args)
    return result
