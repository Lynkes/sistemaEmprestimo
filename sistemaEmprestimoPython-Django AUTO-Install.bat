@title Sistema Emprestimo
@echo off

set inst_dir=F:\
cd /d "%inst_dir%"

if not exist "sistemaEmprestimo\" (
    cmd /c git clone https://github.com/alexandrezamberlan/sistemaEmprestimo.git
)
cd /d "sistemaEmprestimo"

echo Sistema Emprestimo

git pull
echo.

call Python-DjangoUi.bat