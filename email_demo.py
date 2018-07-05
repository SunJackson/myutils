#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime

from utils import emailutils
from tools.redirect_log import RedirectLog

LOG_BUCKET = RedirectLog()


class EmailDemo:
    def __init__(self, send_email=False, addrs=None):
        '''
        :param send_email: True,Send message to addrs. False, print message to stdout
        :param addrs: accept the email users email address
        '''
        self.end_time = datetime.datetime.now()
        self.start_time = self.end_time - datetime.timedelta(days=1)
        self.send_email = send_email
        self.to_addrs = addrs
        self.title = 'email_demo'

        if send_email:
            sys.stdout = LOG_BUCKET

    def send_email_data(self):
        print("email body")

    def email_send(self):
        if self.send_email:
            emailutils.send(
                to_addr=self.to_addrs,
                title=self.title,
                mail_body=LOG_BUCKET.buff
            )
            LOG_BUCKET.reset()

    def run(self):
        self.send_email_data()
        self.email_send()


if __name__ == '__main__':
    to_addrs = ["xxxxxxxx@dd.com", "yyyyyyyyy@dd.com"],
    opt = EmailDemo(send_email=True, addrs=to_addrs)
    opt.run()