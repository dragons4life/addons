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

import hexchat, urllib, urllib2

__module_name__ = "urlshort"
__module_version__ = "1.0"
__module_description__ = "A URL Shortener for Hexchat"


def short(word, word_eol, userdata):
	if(len(word) > 1):
		url = word[1]
		f = urllib2.urlopen('http://po.st/api/shorten?longUrl='+url+'&apiKey=1A3CEEF6-33E0-45F3-8B0A-8236C77B98A1&format=txt')
		q = f.read()
		if(len(q) > 1):
			print(q)
			return hexchat.EAT_ALL
		else:
			return hexchat.EAT_ALL
	else:
		print("Usage: /short <url>")
		return hexchat.EAT_ALL
	
		


hexchat.hook_command('short', short, help="Shortens a url")