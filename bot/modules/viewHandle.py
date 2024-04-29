import discord
from discord.ui import View
# 循環インポートを避けるためにこのインポートを遅延
# from .modal_template import SetForm
from .buttonHandle import SetButtonToView,SetFinishButton,SetButtonToModal
import config


# 最初のボタン表示をさせるためのView
class SetButtonView(View):
    def __init__(self,user):
        super().__init__()

        self.user = user
        from .modalHandle import SetForm


        #フォームを動的に作りたいのでコメントアウト
        # # フォーム準備（データの準備） 
        # admission_form = SetForm(user,"入会届")
        # change_form = SetForm(user,"情報変更届")
        # obog_form = SetForm(user,"OBOG届")

        #モーダルをあらかじめ準備するとInputTextのvalueへの入力がここで起こってしまう
        # モーダル準備
        # admision_view = SetModalView(user,"入会届(1/1)",admission_form.SetModal1(admission_form),style=discord.ButtonStyle.primary,form = admission_form)
        # change_view = SetModalView(user,"情報変更届(1/1)",change_form.SetModal1(change_form),style=discord.ButtonStyle.success,form=change_form)
        # obog_view = SetModalView(user,"OBOG届(1/1)",obog_form.SetModal1(obog_form),style=discord.ButtonStyle.gray,form = obog_form)

        #個別のボタンを表示するボタン、modal表示しないように
        admissionbutton = SetButtonToView(label="入会届",style=config.admission_button_style,comment = "入会届を入力してください",user=user)
        changebutton = SetButtonToView(label="情報変更届",style=config.change_button_style,comment="登録情報を変更したい場合は下のボタンを押してください",user=user)
        obogbutton = SetButtonToView(label="OBOG届",style=config.obog_button_style,comment = "obog届を入力してください",user=user)
        deletebutton = SetButtonToView(label="退会届", style=config.delete_button_style,comment = "退会届を入力してください",user=user)
        self.add_item(admissionbutton)
        self.add_item(changebutton)
        self.add_item(obogbutton)
        self.add_item(deletebutton)
    
        # 個別のボタンを表示、ただmodalを表示したくないのでコメントアウト
        # admissionbutton = SetButtonToView(label="入会届",style=discord.ButtonStyle.primary,view=admision_view,comment = "入会届を入力してください",user=user,form = admission_form)
        # changebutton = SetButtonToView(label="情報変更届", view=change_view,style=discord.ButtonStyle.success,comment="登録情報を変更したい場合は下のボタンを押してください",user=user,form = change_form)
        # obogbutton = SetButtonToView(label="OBOG届",style=discord.ButtonStyle.gray,view=obog_view,comment = "obog届を入力してください",user=user,form = obog_form)
        # self.add_item(admissionbutton)
        # self.add_item(changebutton)
        # self.add_item(obogbutton)

        

#モーダル表示のview
class SetModalView(View):
    def __init__(self,user,label,modal,style,form):
    # def __init__(self,label,modal,style):
        super().__init__()
       
        button = SetButtonToModal(user=user,label=label,modal=modal,style=style,form=form)
        # button = SetButtonToModal(label=label,modal=modal,style=style)
        
        self.add_item(button)


class SetFinishView(View):
    def __init__(self,user,form,label,style):
        super().__init__()

        button = SetFinishButton(user=user,form=form,label=label,style=style)

        self.add_item(button)
        