#By Prosta Umid
from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Hearts"}
	@loader.owner
	async def heartscmd(self, message):
		for _ in range(100):
			for heart in ['โค', '๏ธ๐งก', '๐', '๐', '๐', '๐']:
				await message.edit(heart)
				await sleep(0.6)