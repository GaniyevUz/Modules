#by @JahongirGaniyev
from .. import loader
from asyncio import sleep
@loader.tds
class SmileMod(loader.Module):
	strings = {"name": "Smile"}
	@loader.owner
	async def smilecmd(self, message):
		for _ in range(100):
			for smile in ["ð", "ð", "ð", "ð", "ð", "ð", "ð", "ðĪĢ", "ð", "ð", "ð", "ð", "ð", "ð", "ð", "ðĨ°", "ð", "ð","ð", "ð", "âđïļ", "ð", "ð", "ð", "ð", "ðĪŠ", "ðĻ", "ð§", "ðĪ", "ð", "ðĪĐ","ðĨģ","ðĪ","ðĪŊ","ðĪ ","ðĪ","ðĪ","ðĪ","ðĪ","ð","ðĄ","ðĪŽ","ðĨš","ðĪ","ðŽ" ]:
				await message.edit(smile)
				await sleep(0.5)
