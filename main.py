import telebot
import random
from telebot import types
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open ('data/libraries.txt', 'r', encoding='UTF-8')
libraries = f.read().split('\n')
f.close()
f = open ('data/frameworks.txt', 'r', encoding='UTF-8')
frameworks = f.read().split('\n')
f.close()
f = open ('data/projects.txt', 'r', encoding='UTF-8')
projects = f.read().split('\n')
f.close()