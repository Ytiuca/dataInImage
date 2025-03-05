@echo off
setlocal enabledelayedexpansion

for /f "tokens=1,2 delims==" %%A in (.env) do (
    set cle=%%A
    set valeur=%%B
    set !cle!=!valeur!
)

set flag_save=

if "%SAVE_BG%"=="true" (
    set flag_save=-s
)

python main.py -x %X_LENGTH% -y %Y_LENGTH% -d %TIME_BEFORE_BG_CHANGE% %flag_save%