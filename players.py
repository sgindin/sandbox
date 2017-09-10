# coding=utf-8
import json

russian = u"привет мир".encode('utf-8')
print russian

players = [u"иван".encode('utf-8'), u"сергей".encode('utf-8'), u"михаил".encode('utf-8'), u"владимир".encode('utf-8')]

for p in players:
    print p

#print players[0:3]

players = ['иван', 'Сергей', 'michail', 'vladimir']
for p in players[0:2]:
    print p
