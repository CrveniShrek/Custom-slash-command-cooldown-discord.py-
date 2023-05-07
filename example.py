import discord
from discord.ext import commands


def custom_cooldown(rate, per):
    def predicate(interaction: discord.Interaction):
        if interaction.user.id in (...): #put specified user ids here
            return None
        return discord.app_commands.Cooldown(rate, per)
    return discord.app_commands.checks.dynamic_cooldown(predicate, key= lambda i: i.user.id) #i.___.id can also be guild/channel/member



@bot.tree.command(name='test')
@custom_cooldown(1, 10) #these values effect every user except specified ones
async def test(interaction: discord.Interaction):
  ... #command code














