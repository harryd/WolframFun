#!/usr/bin/env python
from wap import WolframAlphaEngine
from wap import WolframAlphaQueryResult
import sys

__author__ = 'me@tomdignan.com'
__version__ = '0.1-dev'

server = 'http://api.wolframalpha.com/v1/query.jsp'
appid = open('appid').readline()[0:-1]
print 'using app id: "%s"' % appid

if len(sys.argv) > 1:
	input = ' '.join(sys.argv[1:])
else:	
	input = 'who are you?'

wolfram = WolframAlphaEngine(appid, server)
query = wolfram.CreateQuery(input)
result = wolfram.PerformQuery(query)
waeqr = WolframAlphaQueryResult(result)
print waeqr.Answer()



