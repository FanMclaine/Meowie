import voltage  # Import voltage.
import random
from animalpy import animals
from voltage.ext import (
    commands,  # Importing the commands framework so we that we're able to create a Cog object.
)

cat = voltage.Client()  
codes = [ "100", "101", "102", "200", "201", "202", "203", "204", "206", "207", "300", "301", "302", "303", "304", "305", "307", "308", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "421", "422", "423", "424", "425", "426", "429", "431", "444", "450", "451", "497", "498", "499", "500", "502", "503", "504", "506", "507", "508", "509", "510", "511", "521", "523", "525", "599" ]

def setup(client) -> commands.Cog:

    test = commands.Cog(  # Create a new Cog object.
        "Test", "Some commands for testing."  # Give it a name.  # And an optional description.
    )

    animal = commands.Cog(
      "Animals", "Animal commandz!"
    )

    @test.command()
    async def pingcog(ctx):  # No self parameter.
        """Sends Pong!"""
        await ctx.reply("Pong from inside a Cog!")

    @animal.command()
    async def cat(ctx):
      """Kat pics!"""
      msg = await ctx.reply("Hav kat pic! (Embd loading... sry 4 waitin :c )", mention=False)
      catto = animals.picture("cat")
      await msg.edit(embed=voltage.SendableEmbed(media=catto), content="Hav kat pic!")

    @animal.command()
    async def catfact(ctx):
      """Kat fun facts!! (some may be dark)"""
      await ctx.send(animals.fact("cat"))

    @animal.command()
    async def dog(ctx):
      """Dog pics! >:( """
      msg = await ctx.reply("Hav dog pic! (Embd loading... sry 4 waitin :c )", mention=False)
      catto = animals.picture("dog")
      await msg.edit(embed=voltage.SendableEmbed(media=catto), content="Hav dog pic! >:(")

    @animal.command()
    async def httpcat(ctx):
      """httpcattos! """
      code = random.choice(codes)
      await ctx.send(embed = voltage.SendableEmbed(media=f"https://http.cat/{code}"), content="HttpCattos!")

    @animal.command()
    async def dogfact(ctx):
      """Dog fun facts!! >:( (some may be dark)"""
      await ctx.send(animals.fact("dog"))

    return animal
