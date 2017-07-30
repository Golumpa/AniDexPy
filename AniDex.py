#!/usr/bin/python

#-----------------------------------------------------------------------------
# Copyright (c) 2017, Golumpa.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

import sys, getopt
import requests
from pprint import pprint

def main(argv):
	# Config NEEDED or have to be called by python
	apiurl = "https://anidex.info/api/" # URL to API, this shouldn't need to change, but if you want to anyway you can change it here or use the -u arg in command line.
	apikey = "myapitoken" # Use the same API every time? enter it here so you dont have to enter it every time with the -a arg.
	torrentfile = "" # File to upload, just setting the variable. Use the -f arg to set this in command line.
	subcatid = "3" # 3 = Anime Dub, See https://i.golu.mp/OO9zv for API catagory IDs. Use the -c arg to set this in command line.
	language = "1" # 1 = English, See https://i.golu.mp/CJ7tr for language IDs. Use the -l arg to set this in command line.
	send = "true" # Apparently its needed in the API. I belive true is needed for it to be posted on AniDex, use --nosend to turn this to false.

	# Optional Config
	torrentname = "" # Defualt name for the torrent. Use the -n arg to set this in the command line.
	description = "Uploaded with AniDex remote by Golumpa" # default description for the torrent use the -d arg to set this in command line.
	group = "0" # 0 = NO group, set this ID or use the -g arg if you want to release to a group.
	batch = "0" # 0 = NOT a batch, set to "1" or use --batch in command line if it is a batch.
	hentai = "0" # 0 = NOT hentai, set to "1" or use --hentai in command line if it is hentai.
	reencode = "0" # 0 = NOT a re-encode,  set to "1" or use --reencode in command line if it is a re-encode.
	private = "0" # 0 = NOT private, set to "1" or use --private in commandline if you DO NOT want to publish this torrent publicly.

	helptext = """#=#=#=#=#=#=#=#=#=#\nAniDex API Uploader\n#=#=#=#=#=#=#=#=#=#

  USAGE: AniDex.py -a <apikey> -f <torrentfile> -c <category> -l <language> -n <torrentname> -d <description> -g <group_id> -u <apiurl> --batch --hentai --reencode --private --nosend

  -a <apikey>\n  REQUIRED: The API Key you get from your AniDex Account Settings under the "Upload API" section. https://anidex.info/?page=settings\n
  -f <torrentfile>\n  REQUIRED: The path to the .torrent file you wish to upload. "always best to do absolute paths personally" eg. "/home/golumpa/Boku no Pico.torrent"\n
  -c <category>\n  REQUIRED: The catagory of the torrent you are uploading, for a list of cacagories check this link: https://i.golu.mp/OO9zv\n
  -l <language>\n  REQUIRED: The language of the torrent you are uploading. NOT YOUR LANGUAGE, the language of the media such as Spanish for Spanish subs. See this link for a list of available languages: https://i.golu.mp/CJ7tr\n
  -n <torrentname>\n  OPTIONAL: The name of torrent that will be show on AniDex, such as a more user freindly and readable title.\n
  -d <description>\n  OPTIONAL: The description of the torrent, try to keep it informal as everyone hates blank descriptions that say or show nothing about the release.\n
  -g <group_id>\n  OPTIONAL: The Group ID that you wish to post this torrent under.\n
  -u <apiurl>\n  OPTIONAL: The URL of the AniDex API, you shouldnt need to change this value but on the offchance you can.\n
  --batch\n  OPTIONAL: Option to set this torrent as a batch with multiple episodes.\n
  --hentai\n  OPTIONAL: Option to set this torrent to a hentai release so its hidden to the people that dont want to see nsfw content.\n
  --reencode\n  OPTIONAL: Option to set this release to a re-encode release, basically where you run the original through something like handbrake to get a different quality.\n
  --private\n  OPTIONAL: Option to set the torrent to private so only you AND your group members can view it.\n
  --nosend\n  OPTIONAL: Not sure if this works but I assume this will make it so it doenst actually submit the torrent to AniDex. Not sure why you would want it though...\n"""

	try:
		opts, args = getopt.getopt(argv,"ha:f:n:c:l:d:g:u:",["file=","apiurl=","apikey=","cat=","name=","group=","lang=","desc=","batch","hentai","nosend","reencode","private"])
	except getopt.GetoptError:
		print(helptext)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(helptext)
			sys.exit()
		elif opt in ("-f", "--file"):
			torrentfile = arg
		elif opt in ("-u", "--apiurl"):
			url = arg
		elif opt in ("-a", "--apikey"):
			apiToken = arg
		elif opt in ("-c", "--cat"):
			subcatid = arg
		elif opt in ("-n", "--name"):
			torrentname = arg
		elif opt in ("-g", "--group"):
			group = arg
		elif opt in ("-l", "--lang"):
			language = arg
		elif opt in ("-d", "--desc"):
			description = arg
		elif opt in ("--batch"):
			batch = "1"
		elif opt in ("--hentai"):
			hentai = "1"
		elif opt in ("--nosend"):
			send = "false"
		elif opt in ("--reencode"):
			reencode = "1"
		elif opt in ("--private"):
			private = "1"
	data = {
		'subcat_id':subcatid,
		'file':torrentfile,
		'torrent_name':torrentname,
		'group_id':group,
		'lang_id':language,
		'description':description,
		'batch':batch,
		'hentai':hentai,
		'reencode':reencode,
		'private':private,
		'api_key':apikey,
		'send':send
	}
	if torrentfile != "":
		response = requests.post(apiurl,
			data=data,
			files={'file': open(torrentfile, 'rb')})
	else:
		response = requests.post(apiurl,
			data=data)
	pprint(response.text)

if __name__ == "__main__":
   main(sys.argv[1:])