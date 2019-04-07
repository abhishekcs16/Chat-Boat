# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:10:16 2017

@author: Abhishek
"""

from pygame import mixer # Load the required library

mixer.init()
mixer.music.load('/home/ratani/Videos/videos/2 Many Girls - Fazilpuria.mp4')
mixer.music.play()
