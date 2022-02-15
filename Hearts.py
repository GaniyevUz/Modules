#By Prosta Umid
from .. import loader
from asyncio import sleep
@loader.tds
class HeartMod(loader.Module):
	strings = {"name": "Hearts Unique"}
	@loader.owner
	async def heartcmd(self, message):
		for _ in range(50):
			for heart in ['💖', '💓', '💞', '💘', '💖', '❣']:
				await message.edit(heart)
				await sleep(0.6)