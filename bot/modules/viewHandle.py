import discord
from discord.ui import View
# 循環インポートを避けるためにこのインポートを遅延
# from .modal_template import SetForm
from .buttonHandle import SetButtonToView,SetFinishButton,SetButtonToModal,SetDeleteButton
import config


# 最初のボタン表示をさせるためのView
class SetButtonView(View):
    def __init__(self,user):
        super().__init__()

        self.user = user
        from .modalHandle import SetForm

        #個別のボタンを表示するボタン、modal表示しないように
        admissionbutton = SetButtonToView(label="入会届",style=config.admission_button_style,comment = "入会届を入力してください",user=user)
        changebutton = SetButtonToView(label="情報変更届",style=config.change_button_style,comment="登録情報を変更したい場合は下のボタンを押してください",user=user)
        obogbutton = SetButtonToView(label="OBOG届",style=config.obog_button_style,comment = "obog届を入力してください",user=user)
        deletebutton = SetButtonToView(label="退会届", style=config.delete_button_style,comment = "退会届を提出してよろしいですか？",user=user)
        self.add_item(admissionbutton)
        self.add_item(changebutton)
        self.add_item(obogbutton)
        self.add_item(deletebutton)
    
        

#モーダル表示のview
class SetModalView(View):
    def __init__(self,user,label,modal,style,form):
        super().__init__()
       
        button = SetButtonToModal(user=user,label=label,modal=modal,style=style,form=form)

        
        self.add_item(button)


class SetFinishView(View):
    def __init__(self,user,form,label,style):
        super().__init__()

        button = SetFinishButton(user=user,form=form,label=label,style=style)

        self.add_item(button)

class SetDeleteView(View):
    def __init__(self,user,form,label,style):
        super().__init__()

        #退会届の送信ボタン
        button = SetDeleteButton(user=user,form=form,label=label,style=style)

        self.add_item(button)
        
