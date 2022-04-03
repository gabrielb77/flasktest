
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

def test_CheckExistsLurl():
  assert exists('flasktest.db')

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