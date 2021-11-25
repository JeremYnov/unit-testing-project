# L'objectif de ce script-test est de montrer chiffre à l'appuie, en passant par pytest-xdist (pour la parallélisation), le gain du temps réalisé ?

import pytest

# sans paral => 8.04s
# pytest -vs --disable-warnings --capture sys -rF -rP --html=../test_report.html --self-contained-html test_speed.py
# avec 2 workers => 5.50s
# pytest -vs --disable-warnings --capture sys -rF -rP --html=../test_report_2.html --self-contained-html -n 2 test_speed.py

# avec 4 workers => 4.18s
# pytest -n 4 -vs --disable-warnings --capture sys -rF -rP --html=../test_report4.html --self-contained-html test_speed.py


import time
# time_start = time.time()

def test_dog():
    print('ce test va durer 2s')
    time.sleep(2)
    assert 'dog'=='dog'

def test_cat():
    print('ce test va durer 2s')
    time.sleep(2)
    assert 'cat'=='cat'


def test_blue():
    print('ce test va durer 2s')
    time.sleep(2)
    assert 'blue'=='blue'


def test_green():
    print('ce test va durer 2s')
    time.sleep(2)
    assert 'green'=='green'