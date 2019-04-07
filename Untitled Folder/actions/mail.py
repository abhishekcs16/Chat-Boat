# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 13:38:46 2017

@author: ratani
"""

import smtplib

gmail_user = 'project.castiel.ai@gmail.com'  
gmail_password = 'heart1996'

sender = gmail_user  
to = ['me@gmail.com', 'bill@gmail.com']  
subject = 'OMG Super Important Message'  
body = "Hey, what's up?\n\n- You"

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sender, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sender, to, email_text)
    server.close()

    print 'Email sent!'
except:  
    print 'Something went wrong...'
