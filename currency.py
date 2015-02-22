# -*- coding: utf-8 -*-

# currency.py
# A currency converter plugin for hexchat.
# Copyright 2015 Max Thor
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


# Note! Only does one line!
import hexchat, urllib2, json

__module_name__ = "Currency"
__module_version__ = "1.0"
__module_description__ = "A currency converter plugin for hexchat"

def convert(amt, fro, to):
	p = str(fro+"_"+to)
	f = urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/convert?q='+p+'&compact=y')
	q = json.loads(f.read())
	if(p in q or p.upper() in q):
		a = q[p.upper()]['val']
		b = float(a)*float(amt)
		print(str(amt)+" "+fro+" is "+str(b)+" "+to)
		return hexchat.EAT_ALL
	else:
		print("Usage: /convert <amount> <from> <to>")
		return hexchat.EAT_ALL


def getParam(word, word_eol, userdata):
	del word[0]
	convert(word[0], word[1], word[2])

hexchat.hook_command('convert', getParam, help="Converts currencies")
