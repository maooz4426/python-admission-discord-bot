import discord

class RoleHandle():
    def __init__(self,interaction):
        self.circleMemberRole = discord.utils.get(interaction.guild.roles, name="サークル会員")
        self.obogMemberRole = discord.utils.get(interaction.guild.roles, name="OBOG")
        self.interaction = interaction

    
    #ロール付与のコード
    async def giveRole(self,title):
        

        if title == "入会届":
            remove_role = self.obogMemberRole
            give_role = self.circleMemberRole
        elif title == "OBOG届":
            remove_role = self.circleMemberRole
            give_role = self.obogMemberRole
        else :
            return
        
        print(give_role)
        member = self.interaction.user
        await member.remove_roles(remove_role)
        await member.add_roles(give_role)

    #ロールでどのシートを操作するか決定
    def setSheetNameByRole(self,roles):
        sheet = None
        for role in roles:
            print(role.name)
            if role.name == "サークル会員":
                print("ok")
                sheet = "admissionSheet"
                break
            elif role.name == "OBOG":
                sheet = "obogSheet"
                break
        
        return sheet

