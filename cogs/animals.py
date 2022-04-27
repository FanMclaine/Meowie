import voltage  # Import voltage.
from animalpy import animals
from voltage.ext import (
    commands,  # Importing the commands framework so we that we're able to create a Cog object.
)

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
    async def dogfact(ctx):
      """Dog fun facts!! >:( (some may be dark)"""
      await ctx.send(animals.fact("dog"))

    return animal
