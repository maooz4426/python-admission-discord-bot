from discord.ui import View
from .modal_template import SetButtonToModal

#モーダル表示のview
class SetupModalView(View):
    def __init__(self,label,modal,style):
    # def __init__(self,label,modal,style):
        super().__init__()
        button = SetButtonToModal(label=label,modal=modal,style=style)
        # button = SetButtonToModal(label=label,modal=modal,style=style)
        
        self.add_item(button)