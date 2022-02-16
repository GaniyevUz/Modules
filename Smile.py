#by @JahongirGaniyev
from .. import loader
from asyncio import sleep
@loader.tds
class SmileMod(loader.Module):
	strings = {"name": "Smile"}
	@loader.owner
	async def smilecmd(self, message):
		for _ in range(100):
			for smile in ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😟","😕", "🙁", "☹️", "😋", "😛", "😝", "😜", "🤪", "😨", "🧐", "🤓", "😎", "🤩","🥳","🤓","🤯","😵‍💫","🤒","🤕","🤐","😮‍💨","🙄","😡","🤬","🥺","🤔","😬" ]:
				await message.edit(smile)
				await sleep(0.5)
