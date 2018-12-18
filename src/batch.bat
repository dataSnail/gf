:: data cleaning output fileName mid_network_friends.txt
H:
cd H:\gf
::python ./src/data_cleaning.py --input_file_name ./data/network_friends_all.txt --output_file_name ./data/mid_network_friends.txt

::python ./src/getPerception.py --start_id 0 --end_id 1 worker_id 0

::windows
REM @echo off
REM set /a item=2000
REM set /a n=0
REM set /a e=item
REM set /a id=0
REM :loop
REM if %n% leq 18789 (
REM start python ./src/getPerception.py --start_id %n% --end_id %e% --worker_id %id%
REM set /a n+=item
REM set /a e+=item
REM set /a id+=1
REM GOTO :loop
REM )
REM pause