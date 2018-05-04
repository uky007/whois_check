#!/usr/bin python
# -*- coding: utf-8 -*-

import os
import urllib
import urllib2
import time
import datetime
#
#
if __name__=='__main__':
    #
    list = open('list-company.txt', 'r').read()
    query_list=list.split('\n')
    outputfile = open(outputfile, 'w')

    #
    for query in query_list:
        #
        try:
            query_uni = query.decode('utf-8')
            query_s = query_uni.encode('sjis')
            query_urlenc = urllib2.quote(query_s)
            # print(query_urlenc)
            # print(query_urlenc)
            url = 'http://whois.nic.ad.jp/cgi-bin/whois_gw?codecheck-sjis=%82%C9%82%D9%82%F1%82%CB%82%C1%82%C6%82%ED%81%5B%82%AD%82%A2%82%F1%82%D3%82%A7%82%DF%81%5B%82%B5%82%E5%82%F1%82%B9%82%F1%82%BD%81%5B&key=%27'+ query_urlenc + '&submit=%8C%9F%8D%%F5&type=NET-HOLDER&rule='
            # print(url)
            response = urllib2.urlopen(url, None, 180)
        except urllib2.URLError, exc:
            print("error occurred.")
        else:
            d = datetime.datetime.today()
            html = response.read()
            print("%2s-%2s-%2s %2s:%2s:%2s query succeeded:%s" % (d.yaer, d.month, d.day, d.hour, d.minute, d.second, query))
            output.write("## %s" % query)
            output.write(str(html))
            # print(str(html))
            time.sleep(5)
            output.close()
            
