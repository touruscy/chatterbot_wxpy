# -*- coding:utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import preprocessors
from wxpy import *
import configparser


def load_path():
	# 读取配置文件
	config = configparser.ConfigParser()
	config.read("config.cfg")
	my_friend = config.get("friends", "my_friends")
	my_mp = config.get("mp", "mps")
	my_group = config.get("groups", "my_groups")
	return my_friend, my_mp, my_group

def witchat(people):
	print(people)
	# 初始化机器人
	chatbot = ChatBot(
    "My ChatterBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter")
	chatbot.set_trainer(ChatterBotCorpusTrainer)
	print("**************开启机器人**************")
	chatbot.train("./conversations.yml")
	# chatbot.train("chatterbot.corpus.chinese")
	print("**************调用中文词库**************")
	
	bot = Bot()
	print("**************启动微信****************")
	@bot.register()  
	def print_msg(msg):
		print(msg)
	
	my_friend = ""	
	print(people[0])
	if people[0]=="" or people[0] is None:
			pass
	else:			
		my_friend = bot.friends().search(people[0])[0]
	print("该朋友是", my_friend)	
	# 使用机器人进行自动回复				
	@bot.register(my_friend)
	def reply_my_friends(msg):
		return chatbot.get_response(msg.text).text
	
	my_mp = ""
	if people[1]=="" or people[1] is None:
			pass	
	else:
		my_mp = bot.mps().search(people[1])[0]		
	print("该公众号是", my_mp)
	my_mp.send("hello, 小冰冰，我又来了")
	# 使用机器人进行自动回复	
	@bot.register(my_mp)
	def reply_my_mps(msg):
		return chatbot.get_response(msg.text).text
	
	my_group = ""	
	if people[2]=="" or people[2] is None:
			pass	
	else:
		my_group = bot.groups().search(people[2])[0]
	print("该群聊是", my_group)
	# my_group.send("hello,guys")
	# 使用机器人进行自动回复
	@bot.register(my_group)
	def reply_my_groups(msg):			
		return chatbot.get_response(msg.text).text	
		
	embed()
	
if __name__ == '__main__':
	path = load_path()
	witchat(path)

