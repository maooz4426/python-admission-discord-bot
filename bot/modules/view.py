import discord
from discord.ui import View
# 循環インポートを避けるためにこのインポートを遅延
# from .modal_template import SetForm
from .button import SetButtonToView,SetFinishButton,SetButtonToModal


# ボタン表示をさせるためのView
class SetButtonView(View):
    def __init__(self):
        super().__init__()
        from .modal import SetForm
        admission_form = SetForm("入会届")
        admision_view = SetModalView("入会届",admission_form.SetModal1(admission_form),style=discord.ButtonStyle.primary)
        obog_view = SetModalView("OBOG届",SetForm("OBOG届"),style=discord.ButtonStyle.primary)
        admissionbutton = SetButtonToView(label="入会届",style=discord.ButtonStyle.primary,view=admision_view,comment = "入会届を入力してください")
        obogbutton = SetButtonToView(label="OBOG届",style=discord.ButtonStyle.gray,view=obog_view,comment = "obog届を入力してください")
        self.add_item(admissionbutton)
        self.add_item(obogbutton)

#モーダル表示のview
class SetModalView(View):
    def __init__(self,label,modal,style):
    # def __init__(self,label,modal,style):
        super().__init__()
        button = SetButtonToModal(label=label,modal=modal,style=style)
        # button = SetButtonToModal(label=label,modal=modal,style=style)
        
        self.add_item(button)

class SetupFinishView(View):
    def __init__(self,form,label,style):
        super().__init__()

        button = SetFinishButton(form=form,label=label,style=style)

        self.add_item(button)
        