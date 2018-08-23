#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime

from UtilsCell import emailutils
from UtilsCell.tools.redirect_log import RedirectLog

LOG_BUCKET = RedirectLog()

mail_user = '306862600@qq.com'
mail_pass = 'yjxvqgcgmneobibf****'
mail_server = 'smtp.qq.com'
mail_port = '465'


class EmailDemo:
    def __init__(self, debug=False, send_email=False, addrs=None):
        '''
        :param send_email: True,Send message to addrs. False, print message to stdout
        :param addrs: accept the email users email address
        '''
        self.debug = debug
        self.end_time = datetime.datetime.now()
        self.start_time = self.end_time - datetime.timedelta(days=1)
        self.send_email = send_email
        self.to_addrs = addrs
        self.title = 'email_demo'

        if not self.debug:
            sys.stdout = LOG_BUCKET

    def send_email_data(self):
        print("demo email body")

    def email_send(self):
        if self.send_email:
            send_status = emailutils.send(
                mail_user=mail_user,
                mail_pass=mail_pass,
                mail_server=mail_server,
                mail_port=mail_port,
                to_addr=self.to_addrs,
                title=self.title,
                mail_body=LOG_BUCKET.buff
            )
            if not self.debug:
                LOG_BUCKET.reset()
            return send_status

    def run(self):
        self.send_email_data()
        result = self.email_send()
        print(result)


if __name__ == '__main__':
    to_addrs = ["30686260@qq.com"]
    opt = EmailDemo(debug=False, send_email=True, addrs=to_addrs)
    opt.run()
    print('END')
