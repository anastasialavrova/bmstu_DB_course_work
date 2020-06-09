#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

# Подключаемся к базе данных
con = lite.connect('clinic.db')

with con:
    # cur = con.cursor()
    # # Создаем таблицу
    # cur.execute("CREATE TABLE doctors(id_doc INTEGER PRIMARY KEY, doc_name TEXT, doc_spec TEXT, doc_about TEXT)")
    # # Вносим данные
    # cur.execute("INSERT INTO doctors VALUES(1, 'Мелконян Армен Георгиевич ', 'терапевт', 'Доктор медицинских наук, подполковник медицинской службы запаса. Окончил Военно-медицинскую академию им. С.М. Кирова, Санкт-Петербург, факультет подготовки врачей для Военно-морского флота, военный врач (1980 г.) и факультет руководящего медицинского состава по специальности терапия (1986-1988 г.).')")
    # cur.execute("INSERT INTO doctors VALUES(2, 'Алексеева Людмила Анатольевна', 'терапевт', 'Терапевт факультетов ИУ, РТ')")
    # cur.execute("INSERT INTO doctors VALUES(3, 'Исаева Светлана Владимировна', 'оториноларинголог', 'Врач оториноларинголог Исаева Светлана Владимировна ведет амбулаторный прием пациентов, проводит консультацию и консервативное лечение при воспалении , травме , кровотечении, невоспалительным заболеваниям лор органов( отит, синусит, ларингит, фарингит , тонзиллит , евстахеит , аденоидит, снижение слуха, ангина, атерома мочки уха).')")
    # cur.execute("INSERT INTO doctors VALUES(4, 'Новикова Яна Биктимировна', 'эндокринолог', 'Врач эндокринолог, стаж 11 лет. Занимается ведением пациентов с эндокринными патологиями в стационарных и поликлинических условиях.')")
    # #cur.execute("DROP TABLE doctors")

    # cur = con.cursor()
    # # Создаем таблицу
    # cur.execute("CREATE TABLE schedule(id_sch INTEGER PRIMARY KEY, sch_name TEXT, sch_spec TEXT, sch_cab INTEGER, sch_floor INTEGER, "
    #             "sch_mon TEXT, sch_tue TEXT, sch_wed TEXT, sch_thu TEXT, sch_fri TEXT)")
    # # Вносим данные
    # cur.execute(
    #     "INSERT INTO schedule VALUES(1, 'Мелконян А.Г.', 'Зав. терап. отд.', '206', '2', '09:00-12:00', '09:00-12:00', '09:00-12:00', '09:00-12:00', '09:00-12:00')")
    # cur.execute(
    #     "INSERT INTO schedule VALUES(2, 'Алексеева Л. А.', 'Терапевт', '209', '2', '14:00-19:00', '08:30-14:00', '14:00-19:00', '08:30-14:00', '14:00-19:00')")
    # cur.execute(
    #     "INSERT INTO schedule VALUES(3, 'Исаева С. В.', 'ЛОР', '4', '1', '08:30-19:00', '08:30-19:00', '08:30-19:00', '08:30-19:00', '08:30-19:00')")
    # cur.execute(
    #     "INSERT INTO schedule VALUES(4, 'Новикова Я. Б.', 'Эндокринолог', '204', '2', '-', '-', '16:00-20:00', '-', '09:00-13:00')")
    # # cur.execute("DROP TABLE doctors")



    # cur = con.cursor()
    # # Создаем таблицу
    # cur.execute("CREATE TABLE record(id_rec INTEGER PRIMARY KEY, rec_login TEXT, rec_date DATETIME, rec_diag TEXT)")
    # # cur.execute("DROP TABLE record")

    # cur = con.cursor()
    # Создаем таблицу
    # cur.execute("CREATE TABLE news(id_news INTEGER PRIMARY KEY, news_date DATETIME, news_title TEXT, news_text TEXT)")
    # # cur.execute("DROP TABLE news")

    # cur = con.cursor()
    # #  # Создаем таблицу
    # cur.execute("CREATE TABLE monday(id_mon INTEGER PRIMARY KEY, mon_time TEXT, mon_busy1 INTEGER, mon_busy2 INTEGER, mon_busy3 INTEGER, mon_busy4 INTEGER)")
    # cur.execute("INSERT INTO monday VALUES(1, '8:00', '0',  '1', '0', '1')")
    # cur.execute("INSERT INTO monday VALUES(2, '8:30', '1',  '0', '1', '0')")
    # cur.execute("INSERT INTO monday VALUES(3, '9:00', '0',  '1', '0', '1')")
    # # cur.execute("DROP TABLE monday")

    # cur = con.cursor()
    #
    # cur.execute(
    #     "CREATE TABLE doc1(id_doc INTEGER PRIMARY KEY, doc_time TEXT, doc_mon INTEGER, doc_tue INTEGER, doc_wed INTEGER, doc_thu INTEGER, doc_fri INTEGER)")
    #
    # cur.execute("INSERT INTO doc1 VALUES(1, '8:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc1 VALUES(2, '8:30', '0',  '0', '1', '0', '1')")
    # cur.execute("INSERT INTO doc1 VALUES(3, '9:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc1 VALUES(4, '9:30', '1',  '1', '0', '1', '0')")
    # # cur.execute("DROP TABLE doc1")

    # cur = con.cursor()
    #
    # cur.execute(
    #     "CREATE TABLE doc2(id_doc INTEGER PRIMARY KEY, doc_time TEXT, doc_mon INTEGER, doc_tue INTEGER, doc_wed INTEGER, doc_thu INTEGER, doc_fri INTEGER)")
    #
    # cur.execute("INSERT INTO doc2 VALUES(1, '8:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc2 VALUES(2, '8:30', '0',  '0', '1', '0', '1')")
    # cur.execute("INSERT INTO doc2 VALUES(3, '9:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc2 VALUES(4, '9:30', '1',  '1', '0', '1', '0')")
    # # cur.execute("DROP TABLE doc2")

    # cur = con.cursor()
    #
    # cur.execute(
    #     "CREATE TABLE doc3(id_doc INTEGER PRIMARY KEY, doc_time TEXT, doc_mon INTEGER, doc_tue INTEGER, doc_wed INTEGER, doc_thu INTEGER, doc_fri INTEGER)")
    #
    # cur.execute("INSERT INTO doc3 VALUES(1, '8:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc3 VALUES(2, '8:30', '0',  '0', '1', '0', '1')")
    # cur.execute("INSERT INTO doc3 VALUES(3, '9:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc3 VALUES(4, '9:30', '1',  '1', '0', '1', '0')")
    # # cur.execute("DROP TABLE doc3")

    # cur = con.cursor()
    #
    # cur.execute(
    #     "CREATE TABLE doc4(id_doc INTEGER PRIMARY KEY, doc_time TEXT, doc_mon INTEGER, doc_tue INTEGER, doc_wed INTEGER, doc_thu INTEGER, doc_fri INTEGER)")
    #
    # cur.execute("INSERT INTO doc4 VALUES(1, '8:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc4 VALUES(2, '8:30', '0',  '0', '1', '0', '1')")
    # cur.execute("INSERT INTO doc4 VALUES(3, '9:00', '0',  '1', '0', '1', '0')")
    # cur.execute("INSERT INTO doc4 VALUES(4, '9:30', '1',  '1', '0', '1', '0')")
    # cur.execute("DROP TABLE doc4")

    cur = con.cursor()

    # cur.execute(
    #     "CREATE TABLE notes(id_notes INTEGER PRIMARY KEY,notes_day TEXT, notes_time TEXT, notes_user TEXT, notes_doctor TEXT)")

    #cur.execute("DROP TABLE notes")














