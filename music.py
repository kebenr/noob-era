import discord
from discord.ext import commands
import youtube_dl
import ffmpeg
import asyncio

class music(commands.Cog):
	def __init__(self, client,num = 0):
		self.client = client
		self.queue = []
		self.num = num

	@commands.command()
	async def disconnect(self,ctx):
		await ctx.voice_client.disconnect()

	@commands.command()
	async def play(self,ctx,url):
		if ctx.author.voice is None:
			await ctx.send('ay foker no channel')
		voice_channel = ctx.author.voice.channel
		if ctx.voice_client is None:
			await voice_channel.connect()
			await ctx.send('ay fokr')
		else:
			await ctx.voice_client.move_to(voice_channel)
			await ctx.send('ay fokr')

		vc = ctx.voice_client
		await ctx.channel.purge(limit=1)

		FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
		YDL_OPTIONS = {'format':'best[height<=480]'}

		def repeat(vc, source):
			self.queue.pop(0)
			source = self.queue[0][0]
			vc.play(source, after=lambda e: repeat(vc, source))
			vc.is_playing()

		with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
			info = ydl.extract_info(url, download=False)
			title = info.get('title')
			url2 = info['formats'][0]['url']
			audio = await discord.FFmpegOpusAudio.from_probe(source = url2, **FFMPEG_OPTIONS)
			self.queue.append((audio,title))
			await ctx.send(f'added {title} to queue')
			
			if voice_channel and not vc.is_playing():
				source = self.queue[0][0]
				vc.play(source, after=lambda e: repeat(vc,source))
				vc.is_playing()
	

	@commands.command()
	async def skip(self,ctx,num = 0):
		await ctx.send('skipping')
		place = int(num) - 1
		vc = ctx.voice_client
		voice_channel = ctx.author.voice.channel
		FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
		YDL_OPTIONS = {'format':'best[height<=480]'}

		def repeat(vc,source):
			self.queue.pop(0)
			source = self.queue[0][0]
			vc.play(source, after=lambda e: repeat(vc, source))
			vc.is_playing()

		with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
			if voice_channel and not vc.is_playing():
				source = self.queue[0][0]
				vc.play(source, after=lambda e: repeat(vc,source))
				vc.is_playing()
				
			if place > 1:
				source = self.queue[place]
				self.queue.insert(1,source)
				self.queue.pop(place+1)
				vc.stop()
			
			else:
				vc.stop()




	@commands.command()
	async def pause(self,ctx):
		await ctx.send('paused')
		await ctx.voice_client.pause()


	@commands.command()
	async def resume(self,ctx):
		await ctx.send('resumed')
		await ctx.voice_client.resume()


	@commands.command()
	async def shutdown(self,ctx):
		await ctx.send('fok u nerd')
		await ctx.bot.close()

	@commands.command()
	async def queue(self,ctx):
		queue = ''
		place = 0
		for dog in self.queue:
			place += 1
			queue+=f'\n{place}. {dog[1]}'
		await ctx.send(queue)

	@commands.command()
	async def clear(self,ctx):
		self.queue = []
		await ctx.send('queue cleared')

	@commands.command()
	async def remove(self,ctx,num):
		await ctx.send(f'removed {self.queue[int(num)-1][1]}')
		self.queue.pop(int(num)-1)


def setup(client):
	client.add_cog(music(client))

