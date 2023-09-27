"""
file to handle logging files
"""

# ------------------------------------------------------
# imports
from datetime import datetime
from csv_logger import CsvLogger

log_folder = "ControlSystem/Logs/"

def create_csv_log(fname):
    today = datetime.now().strftime("%y%m%d")
    filename = f'{log_folder}/{fname}/{today}.csv'
    delimiter = ','
    fmt = f'%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s'
    datefmt = '%Y/%m/%d %H:%M:%S'
    header = ['date', 'level', 'value_1', 'value_2']

    # Creat logger with csv rotating handler
    csv_log = CsvLogger(filename=filename,
                        add_level_nums=None,
                        fmt=fmt,
                        datefmt=datefmt,
                        header=header)
    
    return csv_log

log_gui = create_csv_log("GUI")
log_logic = create_csv_log("Logic")


# example logs
# csvlogger.info(["that's that", "ok"])
# csvlogger.warning(["that's that", "ok"])
# csvlogger.error(["that's that", "ok"])
# csvlogger.cmd(["that's that", "nice"])

# ------------------------------------------------------
