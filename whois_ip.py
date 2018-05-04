#! /usr/bin python
# -*- coding: utf-8 -*-

import os
import urllib2
import time
import datetime
#
#
if __name__=='__main__':
    #
    list = open('list-ip.txt', 'r').read()
    query_list = list.split('\n')
    outputfile = 'whois-ip_result.txt'
    output = open(outputfile, 'w')

    #
    for query in query_list:
        #
        try:
            response = urllib2.urlopen('http://whois.nic.ad.jp/cgi-bin/whois_gw?key=%s' % query, None, 180)
        except urllib2.URLError, exc:
            print("error occurred.")
        else:
            d = datetime.datetime.today()
            html = response.read()
            print("%2s-%2s-%2s %2s:%2s:%2s query succeeded:%s" % (d.year, d.month, d.day, d.hour, d.minute, d.second, query))
            output.write("## %s" % query)
            output.write(str(html))
            # print(str(html))
            time.sleep(5)
            output.close()
