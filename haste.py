# -*- coding: utf-8 -*-

# Short.py
# A url shortener plugin for hexchat.
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

__module_name__ = "hexchat"
__module_version__ = "1.0"
__module_description__ = "A HasteBin client for hexchat"


def haste(word, word_eol, userdata):
	if(len(word) > 1):
		del word[0]
		data = " ".join(word)
		print(data);
		f = urllib2.urlopen('http://hastebin.com/documents', data)
		q = f.read()
		if(len(q) > 1):
			print("http://hastebin.com/"+q)
			return hexchat.EAT_ALL
		else:
			return hexchat.EAT_ALL
	else:
		print("Usage: /haste <data>")
		return hexchat.EAT_ALL
	
		


hexchat.hook_command('haste', haste, help="Hastebins data.")