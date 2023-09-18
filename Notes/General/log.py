"""
setting up logging for control system
"""


from csv_logger import CsvLogger


filename = 'logs/log.csv'
delimiter = ','
custom_additional_levels = ['cmd', 'logic']
fmt = f'%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s'
datefmt = '%Y/%m/%d %H:%M:%S'
max_size = 1024  # 1 kilobyte
max_files = 4  # 4 rotating files
header = ['date', 'level', 'value_1', 'value_2']

# Creat logger with csv rotating handler
csvlogger = CsvLogger(filename=filename,
                      add_level_names=custom_additional_levels,
                      add_level_nums=None,
                      fmt=fmt,
                      datefmt=datefmt,
                      max_size=max_size,
                      max_files=max_files,
                      header=header)


# example logs
# csvlogger.info(["that's that", "ok"])
# csvlogger.warning(["that's that", "ok"])
# csvlogger.error(["that's that", "ok"])
# csvlogger.cmd(["that's that", "nice"])