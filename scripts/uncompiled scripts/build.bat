@echo off

set buildScriptPath=%cd%

cd ..
cd python

set pythonPath=%cd%

cd ..
cd diskmth

start /wait %pythonPath%\python.exe "%buildScriptPath%\build.py"