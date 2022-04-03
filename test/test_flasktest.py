
from flask import Flask, request, redirect
from random import choice,randint
from string import ascii_letters
from urllib.parse import urlparse
import sqlite3
from os.path import exists


def test_GetRandom():
  from .. import flasktest

  assert flasktest.GetRandom()

  assert len(flasktest.GetRandom()) >= 1
  assert len(flasktest.GetRandom()) <= 7

def test_CheckExistsLurl():
  from .. import flasktest

  assert exists('flasktest.db')

  assert flasktest.CheckExistsLurl('http://noexisteurl.com',sqlite3.connect('test_flasktest.db'))

def test_CheckExistsHash():
  assert exists('flasktest.db')

def test_GetHash():
  assert exists('flasktest.db')

def test_AddUrl():
  assert exists('flasktest.db')

def test_GetUrl():
  assert exists('flasktest.db')

def test_GetLurl():
  assert exists('flasktest.db')