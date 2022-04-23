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

@client.listen("ready")
async def ready():
    print("komi!!! - {client.user}")
    await status()

@client.listen("message")
async def on_ping(message):
    if message.author.bot is False:
        await client.handle_commands(message)
    elif message.content == "01FWZKVAJZEGH8JV4RRRSYRVAF":
        await message.reply(f"Mah prefix iz `^`!!")
        await client.handle_commands(message)
        return

@client.command()
async def test(ctx):
    await ctx.send("# SPREAD LUV! :cat_blob: :girl_happy:")

@client.listen("message")
async def on_message(message):
  if message.content.startswith("mew"):
    await message.channel.send(" mew!")

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