import os
import subprocess, shlex, time
import numpy as np
import time, json
import sys, os, datetime
from six.moves import urllib
from six.moves import xrange
import numpy
import gzip
import os
import sys
import time

import shutil

def createDir(direc):
	command = "mkdir -p "+direc
	#print "create dir for ", direc
	if not (os.path.exists(direc) and os.path.isdir(direc)):
		os.system(command)


music_folder = '/Users/dipendra/Music/Audio'
albums = os.listdir(music_folder)
albums = [x for x in albums if os.path.isdir(os.path.join(music_folder, x))]
total_songs = 0
for album in albums:
	songs = [x for x in os.listdir(os.path.join(music_folder, album)) if
	         os.path.isfile(os.path.join(os.path.join(music_folder, album), x))]
	os.chdir(music_folder)
	os.rename(album, album.title())
	album = album.title()
	os.chdir(os.path.join(music_folder, album))
	album_name = album.replace('  ',' ')
	album_name = album_name.title()
	print '\n', album_name
	#if album != 'ATIF': continue
	#album_name = '\ '.join(album_name.split(' '))
	for song in songs:
		try:
			total_songs +=1
			extension = song.split('.')[-1]
			song_name = song.replace('(','_').replace(')','_')
			if '-' in song_name:    song_name = song_name.split('-')[
				                                    0]+'.'+extension
			if '[' in song_name:
				start = song_name.split('[')[0]
				end = song_name.split(']')[1]
				song_name = start + end
			if song != song_name:
				shutil.copyfile(song, song_name)
				os.remove(song)
			song_name = '\ '.join(song_name.split(' '))
			#os.system('mv '+song+' '+song_name)
			os.system('id3v2 -A "'+album_name+'" '+song_name)
			os.system('id3v2 -A "'+album_name+'" '+song_name)
			os.system('id3v2 -t "' + song + '" ' + song_name)
			print total_songs, song_name
		except:
			pass
