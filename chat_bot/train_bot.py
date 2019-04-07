# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:23:41 2017

@author: ratani
"""

from chatterbot import ChatBot
import logging




# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Castiel')

def training():
    # Train based on the english corpus
   chatbot.train("chatterbot.corpus.english")

    # Train based on the english corpus
   chatbot.train("chatterbot.corpus.hindi")

    # Train based on english greetings corpus
   chatbot.train("chatterbot.corpus.english.greetings")

    # Train based on the english conversations corpusts
   chatbot.train("chatterbot.corpus.english.conversations")

    # Start by training our bot with the Ubuntu corpus data
   chatbot.train("chatterbot.trainers.UbuntuCorpusTrainer")
    
