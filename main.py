from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
class Calc(MDGridLayout):
     def __init__(self,**kwargs):
          super().__init__(**kwargs)
          self.rows = 2
          self.input_panel = MDTextFieldRect(multiline=False,font_size="32sp",size_hint=(1,0.5))
          self.bottom = MDGridLayout(cols=4,rows=4,spacing="2dp")
          nums = ["1","2","3","+",
                          "4","5","6","-",
                          "7","8","9","*",
                          "=","0","del","/"]
          for dig in nums:
              ops = ["+","-","*","/"]
              if dig in ops:
                   btn = MDRaisedButton(text=dig,on_release=lambda x,d=dig :self.process(d),size_hint=(0.01,0.049),font_size="32sp",md_bg_color=get_color_from_hex("#ffd700"))
                   #self.add_widget(btn)
              btn = MDRaisedButton(text=dig,on_release=lambda x,d=dig :self.process(d),size_hint=(0.01,0.049),font_size="32sp",md_bg_color=get_color_from_hex("#cd853f"),elevation=0)
              space = MDLabel()
              self.bottom.add_widget(btn)
          self.add_widget(self.input_panel)
          self.add_widget(self.bottom)
          
     def process(self,text,_=None):
           try:
                if text == '=' :
                     self.input_panel.text = str(eval(self.input_panel.text))
                elif text == 'del':
                      self.input_panel.text = self.input_panel.text[:-1]
                else:
                      self.input_panel.text += text
                      
           except:
                self.input_panel.text = "ERROR"
                return False
class CalcusApp(MDApp):
     def build(self):
          self.screenmanager = ScreenManager()
          screen = Screen(name="home")
          home = Calc()
          screen.add_widget(home)
          self.screenmanager.add_widget(screen)
          return self.screenmanager
                    
if __name__ == "__main__":
      app = CalcusApp()
      app.run()