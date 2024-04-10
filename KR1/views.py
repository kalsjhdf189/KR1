from django.shortcuts import render, HttpResponse
import sqlite3

def index(request):
    c = sqlite3.connect('fit.db')
    cur = c.cursor()
    cur.execute("SELECT Название,Наполнение,Цена FROM Тариф")
    test = cur.fetchall()
    cur.execute("SELECT Преподаватель,Время,Название FROM Расписание")
    test2 = cur.fetchall()
    return render(request, 'index.html' , {'test': test, 'test2': test2})