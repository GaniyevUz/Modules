#by #Prosta_Umid
from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Police"}
	@loader.owner
	async def policecmd(self, message):
		for _ in range(12):
			for police in ['š“š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµšµ\nš“š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµšµ\nš“š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµšµ','šµšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“š“\nšµšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“š“\nšµšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“š“']:
				await message.edit(police)
				await sleep(0.3)
