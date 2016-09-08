#!/usr/bin/python
#coding:utf-8
import os,shutil,re,xlrd,sys,time
reload(sys)
sys.setdefaultencoding("utf8")
NameString = "lvl_"

readPath = ""
writePath = ""
index = 0
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
dirPath = cur_file_dir()
os.chdir(dirPath)
rootDir = os.getcwd()

if readPath == "":
	readPath = rootDir + "/Input/"

if writePath == "":
	writePath = rootDir + "/Output/"

if os.path.isdir(writePath):
	shutil.rmtree(writePath)
os.mkdir(writePath)
os.chdir(writePath)

def read(file):
	fileRead = open(file)
	try:
		txt = fileRead.read()
	finally:
		fileRead.close
	return txt
def write(writeFileName,str):
	fileWrite = open(writeFileName,"w")
	try:
		fileWrite.write(str)
	finally:
		# print "Finish write : " + writeFileName + "!!!"
		fileWrite.close()

filelist=os.listdir(readPath)  


for name in filelist:
	if name != ".DS_Store":
		readFileName = os.path.join(readPath,name)
		count = index + 5
		index += 1
		name = NameString + str(count) + ".png"
		writeFileName = os.path.join(writePath,name)
		write(writeFileName,read(readFileName))