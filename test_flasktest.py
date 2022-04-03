
from flask import Flask, request, redirect
from random import choice,randint
from string import ascii_letters
from urllib.parse import urlparse
import sqlite3
from os.path import exists


def test_GetRandom():
  import flasktest

  assert flasktest.GetRandom()

  assert len(flasktest.GetRandom()) > 0
  assert len(flasktest.GetRandom()) < 8

def check_db():
  assert exists('flasktest.db')