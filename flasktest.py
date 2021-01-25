#!/usr/bin/env python3

from flask import Flask, request, redirect
from random import choice,randint
from string import ascii_letters
from urllib.parse import urlparse
import sqlite3

def GetRandom():
  RandomInt = randint(1,7)
  return ''.join(choice(ascii_letters) for i in range(RandomInt))

def CheckExistsLurl(Lurl, conn):
  c = conn.cursor()
  c.execute("select count(*) from urls where lurl=?;", (Lurl,) )
  Res = c.fetchone()[0]
  return False if Res == 0 else True

def CheckExistsHash(Surl, conn):
  c = conn.cursor()
  c.execute("select count(*) from urls where surl=?;", (Surl,) )
  Res = c.fetchone()[0]
  return False if Res == 0 else True

def GetHash(Lurl, conn):
  c = conn.cursor()
  c.execute("select surl from urls where lurl=?;", (Lurl,) )
  return c.fetchone()[0]

def AddUrl():
  A = GetRandom()
  HostName = urlparse(request.base_url).hostname
  Lurl = request.get_json(force=True)['url']
#CREATE TABLE urls (surl text, lurl text, creationdate text, creationepoch int);
  conn = sqlite3.connect('flasktest.db')
  c = conn.cursor()
  if CheckExistsLurl(Lurl, conn):
    A = GetHash(Lurl, conn)
  else:
    while CheckExistsHash(A,conn):
      A = GetRandom()
    c.execute("INSERT INTO urls (surl, lurl, creationdate, creationepoch) VALUES ( ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP )", (A, Lurl) )
  conn.commit()
  conn.close()
  return "http://" + HostName + "/" + A + "\r\n"

def GetUrl():
  print("En GetUrl\r\n")
  Lurl = request.get_json(force=True)['url']
  HostName = urlparse(request.base_url).hostname
  conn = sqlite3.connect('flasktest.db')
  c = conn.cursor()
  A = GetHash(Lurl, conn)
  conn.close()
  return "http://" + HostName + "/" + A + "\r\n"

def GetLurl(surl,conn):
  c = conn.cursor()
  c.execute("select lurl from urls where surl=?;", (surl,) )
  return c.fetchone()[0]


app = Flask(__name__)
app.add_url_rule("/get", "GetUrl", GetUrl, methods=['POST'])
app.add_url_rule("/add", "AddUrl", AddUrl, methods=['POST'])

@app.route('/<surl>')
def Redirect(surl):
  conn = sqlite3.connect('flasktest.db')
  Lurl = GetLurl(surl,conn)
  print("Redirect de " + surl + " --> " + Lurl + "\r\n")
  return redirect(Lurl, code = 302)


if __name__ == '__main__':
   app.run("0.0.0.0","9090","true")
