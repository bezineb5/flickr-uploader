# content of test_sample.py

from uploadr.py import *

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
    
def test_isThisStringUnicode():
    s = isThisStringUnicode(u'Some unicode string')
    assert s == True
