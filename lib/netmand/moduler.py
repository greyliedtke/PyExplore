import modulefinder
import importer

mf = modulefinder.ModuleFinder()
rs = mf.run_script('netmand/importer.py')
print(rs)
