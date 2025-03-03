@echo off
setlocal enabledelayedexpansion

for /f "tokens=1,2 delims==" %%A in (.env) do (
    set cle=%%A
    set valeur=%%B
    set !cle!=!valeur!
)

python main.py < nul (
    echo %X_LENGTH%
    echo %Y_LENGTH%
    echo %TIME_BEFORE_BG_CHANGE%
)