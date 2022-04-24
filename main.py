import voltage
from voltage.ext import commands
import asyncio
import random
from host import alive
import os
from animalpy import animals # Import main class

client = commands.CommandsClient(prefix="^")

# , help_command="Help_Command_Here" make sure its a class

async def status():
  for i in range(1, 10000):
    statuses = [
      "Playing with catnips!",
      "Meow!",
      "Thank you Cesiyi and Mclnoot!",
      "https://Meowie.mclaine1109.repl.co",
      "Check out Mechabot.tk!",
      "https://rvlt.gg/NpZnBaHE !"
    ]
    status = random.choice(statuses)
    await client.set_status(status, voltage.PresenceType.online)
    print(f"Set status to {status}")
    await asyncio.sleep(10)

# ez bug fix
# line 49-52 messed up the commands
# I say the culprit is '@client.listen' or 'async def on_message'

@client.listen("ready")
async def ready():
    print("komi!!! -",client.user)
    await status()

@client.command()
async def test(ctx):
    await ctx.send("> # SPREAD LUV! :ayame_heart: :girl_happy:")

# @client.listen("message")
# async def on_message(message):
#  if message.content.startswith("mew"):
#    await message.channel.send(" mew!")

@client.command()
async def cat(ctx):
    embed = voltage.SendableEmbed(
        description = "Mew!",
        media = animals.picture("cat")
    )
    await ctx.send(content="Hav kat pic!", embed=embed)

@client.command()
async def catfact(ctx):
    await ctx.send(animals.fact("cat"))

alive()
client.run(os.environ.get('SECRET'))
