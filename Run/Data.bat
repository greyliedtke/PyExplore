
cd "C:/Users/greyl/ScaledData"

set py_exec="v_env/Scripts/Activate"
call %py_exec%

echo "running Data Server"
@echo off

streamlit run stream.py

pause


