import discord

async def giveRole(interaction,title):

    if title == "入会届":
        remove_role = discord.utils.get(interaction.guild.roles,name="OBOG")
        give_role = discord.utils.get(interaction.guild.roles, name="サークル会員")
    elif title == "OBOG届":
        remove_role = discord.utils.get(interaction.guild.roles,name="サークル会員")
        give_role = discord.utils.get(interaction.guild.roles, name="OBOG")
    else :
        return
    print(give_role)
    member = interaction.user
    await member.remove_roles(remove_role)
    await member.add_roles(give_role)