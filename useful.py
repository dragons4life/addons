# -*- coding: utf-8 -*-

# useful.py
# A plugin of useful stuff for hexchat.
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

import hexchat, base64

__module_name__ = "Useful-Plugin"
__module_version__ = "1.0"
__module_description__ = "A plugin of useful stuff for hexchat."


def reverse(word, word_eol, userdata):
	if(len(word) > 1):
		del word[0]
		st = " ".join(word)
		print st[::-1]
		return hexchat.EAT_ALL
	else:
		print("Usage: /reverse <string>")
		return hexchat.EAT_ALL
		


def b64En(word, word_eol, userdata):
	if(len(word) > 1):
		del word[0]
		st = " ".join(word)
		print(base64.b64encode(st))
		return hexchat.EAT_ALL
	else:
		print("Usage: /b64enc <string>")
		return hexchat.EAT_ALL

def b64De(word, word_eol, userdata):
	if(len(word) > 1):
		del word[0]
		st = " ".join(word)
		print(base64.b64decode(st))
		return hexchat.EAT_ALL
	else:
		print("Usage: /b64dec <string>")
		return hexchat.EAT_ALL


def caesar(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
				for i in s.upper()
				if ord(i) >= 65 and ord(i) <= 90 ])

def getShitToCaesar(word, word_eol, userdata):
	if(len(word) > 1):
		del word[0]
		leng = len(word)
		k = word[leng]
		del word[leng]
		st = " ".join(word)
		print(caesar(st, k))
		return hexchat.EAT_ALL
	else:
		print("Usage: /caesar <string> <key>")
		return hexchat.EAT_ALL



hexchat.hook_command('reverse', reverse, help="Reverses a string")
hexchat.hook_command('b64enc', b64En, help="Base64 encodes a string")
hexchat.hook_command('b64dec', b64De, help="Base64 decodes a string")
hexchat.hook_command('caesar', getShitToCaesar, help="Caesar a string")
