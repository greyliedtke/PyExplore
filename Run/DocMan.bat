
cd "C:/Users/greyl/PyExplore"

set py_exec="virtual_env/Scripts/Activate"
call %py_exec%
cd DocMan

echo "running DocMan Server"
@echo off

mkdocs serve
pause


