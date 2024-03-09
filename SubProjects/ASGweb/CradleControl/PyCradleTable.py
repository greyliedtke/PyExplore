from WebGlobals import *


# ----------------------------------------------------------------------------------------------------------------------
# View Cradle Points Page
def cradle_view_f(req):
    if "cradle_ping" in req.form:
        CPPing(req.form["cradle_ping"])
    if "ping_all" in req.form:
        auto_ping()
    cradle_points = cp_db_query(q_type='Show_cp')
    cp_list = []
    for cradle in cradle_points:
        cp = CP(cradle)
        cp_list.append(cp)
    cp_cols = cp_db_query(q_type='Table_columns', q_table='RemoteServers')
    cp_view = CPView(cp_cols, cradle_points)
    return cp_view


# Class to organize cradle point view on web page
class CPView:
    def __init__(self, cp_cols, cp_list):
        self.columns = cp_cols
        self.cradle_points = cp_list


# Class to ping and update database
class CPPing:
    def __init__(self, cp_id):
        self.cp_id = cp_id
        self.time = datetime.now().strftime("%m/%d/%Y %H:%M")
        self.cp_info = cp_db_query_p(q_type='Show_cp_where', q_cp_id=[cp_id])[0]
        self.ip = self.cp_info[1]
        self.web_ctrl_ls = self.cp_info[6]
        self.hotspot = 'Live'
        self.web_ctrl = self.ping_web()
        self.rd_port = self.port_ping(3389)
        self.update_db()

    # Ping website
    def ping_web(self):
        url = 'http://' + self.ip
        try:
            web_ctrl_req = urllib.request.urlopen(url, timeout=3).getcode()
            if web_ctrl_req == 200:
                web_ctrl_status = f'Running'
                self.web_ctrl_ls = self.time
            else:
                web_ctrl_status = f'Down'

        # catch when port is down vs invalid....
        except:
            web_ctrl_status = f'Down'

        # If website unreachable, ping hotspot
        if web_ctrl_status == 'Down':

            self.hotspot = self.port_ping(8080)

        return web_ctrl_status

    # Ping specific Port
    def port_ping(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((self.ip, port))
            port_result = f'Open'
        except socket.error as e:
            port_result = f'Down'
        s.close()
        return port_result

    # Update CP table
    def update_db(self):
        cp_db_query_p(q_type='update_cp_ping', q_cp_args=[self.web_ctrl, self.web_ctrl_ls, self.hotspot,
                                                          self.rd_port, self.time, self.cp_id])


# Mass Ping / Auto Refresh data
# ----------------------------------------------------------------------------------------------------------------------
def auto_ping():
    cradle_points = cp_db_query(q_type='Show_cp')
    for cradle in cradle_points:
        CPPing(cradle[0])


# Scheduling automatic refresh
ping_sched = BackgroundScheduler()
ping_sched.add_job(func=auto_ping, trigger='interval', hours=24)
ping_sched.start()
atexit.register(lambda: ping_sched.shutdown())


# Edit CP data
# ----------------------------------------------------------------------------------------------------------------------
def cradle_edit_f(req):

    # Populate item with current info
    if "edit_cradle" in req.form:
        cradle_edit = req.form["edit_cradle"]
        item_params = EditItemView('RemoteServers', 'CP', cradle_edit)
        return item_params

    elif "new_cradle" in req.form:
        item_params = EditItemView('RemoteServers', 'CP')
        return item_params

    elif "Commit_Edit" in req.form or "Add_Item" in req.form or "del_cp" in req.form:
        change = CommitDsChange(req)
        return 'updated'


# Class to display item properties
class EditItemView:
    def __init__(self, ds, ds_type, ds_id='new'):
        self.ds = ds
        self.ds_type = ds_type
        self.columns = []
        self.item_columns()
        self.ds_pc = self.columns[0]
        self.current = []
        self.ds_id = ds_id
        if ds_id == 'new':
            self.change = 'New'
        else:
            self.item_contents()
            self.change = 'Edit'

    def item_columns(self):
        all_cols = cp_db_query(q_type='Table_columns', q_table=self.ds)
        cols = []
        for col in all_cols:
            cols.append(col[1])
        self.columns = cols

    def item_contents(self):
        self.current = cp_db_query_p(q_type='Show_cp_where', q_cp_id=[self.ds_id])[0]


# Class to commit changes to dataset
class CommitDsChange:
    def __init__(self, req):
        self.req = req
        self.ds = 'haha'
        self.ds_type = 'haha'

        # Edit cradle point
        if "Commit_Edit" in req.form:
            self.ds = req.form["Commit_Edit"]
            col_key = req.form["col_key"]
            if col_key == "rowid":
                self.ds_type = 'cradle point'
                self.cp_info_update()

        # Delete cp
        elif "del_cp" in req.form:
            self.del_item()

        elif "Add_Item" in req.form:
            self.ds = req.form["Add_Item"]
            self.ds_type = 'CP'
            self.new_cp()

    # Edit ds items
    def cp_info_update(self):
        q_cp_args = [self.req.form["in1"], self.req.form["in2"], self.req.form["in3"], self.req.form["id_key"]]
        cp_db_query_p(q_type='update_cp_info', q_cp_args=q_cp_args)
        return

    # Delete ds item
    def del_item(self):
        cp_db_query_p(q_type='Delete_cp_ID', q_cp_args=[self.req.form["del_cp_key"]])

    # add to cp set
    def new_cp(self):
        q_cp_args = [self.req.form["in0"], self.req.form["in1"], self.req.form["in2"], self.req.form["in3"]]
        cp_db_query_p(q_type='New_cp', q_cp_args=q_cp_args)
        return


# Class to organize CP info
# Not actually used... but could be
class CP:
    def __init__(self, cp):
        self.cp_id = cp[0]
        self.cp_id = cp[0]
        self.project = cp[2]
        self.programmer = cp[3]
        self.notes = cp[4]
        self.wbctrl_stat = cp[5]
        self.last_live = cp[6]
        self.hotspot = cp[7]
        self.rdp = cp[8]
        self.last_refreshed = cp[9]


