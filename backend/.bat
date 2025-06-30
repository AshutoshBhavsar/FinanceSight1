@echo off
cd /d E:\FinanceSight1
call venv\Scripts\activate
set PYTHONPATH=.
uvicorn backend.main:app --reload
