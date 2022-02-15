#by Prosta_Umid
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.fl(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`start loading...`")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   ▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`Done!`")
	#3 soat vaqtim ketdi qilgan ishim ctrl+c ctrl+v ni bosish boʻldi:-D






