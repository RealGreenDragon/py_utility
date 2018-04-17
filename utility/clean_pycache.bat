@echo off

REM Remove all '__pycache__' folders in actual folder and all subfolders

for /d /r . %%d in (__pycache__) do (
if exist "%%d" echo "%%d" && rd /s/q "%%d"
)

echo Done

pause