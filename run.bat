@ECHO OFF

SETLOCAL EnableDelayedExpansion

FOR /f "delims=" %%F IN ('dir /b /s "src\%1.py" 2^>NUL') DO SET filepath=%%F

SET INPUT=io\in.txt
SET OUTPUT=io\out.txt
SET ERROR=io\err.txt

IF DEFINED filepath (
    py "%filepath%" < %INPUT% > %OUTPUT% 2> %ERROR%  ^
        && SET success=true ^
        || SET success=
    ECHO.
    TYPE "%OUTPUT%"
    ECHO.
    IF DEFINED success (
        ECHO === Execution successful.
    ) ELSE (
        ECHO === The program crashed.
        ECHO.
        TYPE "%ERROR%"
        ECHO.
    )
) ELSE (
    ECHO === ERROR: File not found!
)

ENDLOCAL
