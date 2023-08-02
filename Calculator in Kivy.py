import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('calulator.kv')

class kivyBuilderFunction(Widget):
    def Clear_Function(self):
        self.ids.calculator_input.text=""

    def button_click(self,buttonInstance):
        prior=self.ids.calculator_input.text
        if "Math Error" in prior:
            priorp=""
        if (prior=="0"):
            self.ids.calculator_input.text=f"{buttonInstance}"
        else:
            self.ids.calculator_input.text=f"{prior}{buttonInstance}"

    def Operation_Function(self,operatinInstance):
        prior=self.ids.calculator_input.text  
        if (prior!="0"):
            self.ids.calculator_input.text=f"{prior}{operatinInstance}"

    def Equals_Function(self):
        prior=self.ids.calculator_input.text 
        try:
            answer=eval(prior)
            self.ids.calculator_input.text =str(answer)
        except:
            self.ids.calculator_input.text ="Math Error"
        """if "+" in prior:
            num_list=prior.split("+")
            answer=0.0
            for number in num_list:
                answer+=float(number)
            self.ids.calculator_input.text=str(answer)"""

    def dot_Function(self):
        prior=self.ids.calculator_input.text 
        num_list=prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior=f"{prior}."
            self.ids.calculator_input.text=prior
        elif "." in prior:
            pass
        else:
            prior=f"{prior}."
            self.ids.calculator_input.text=prior
            
            
           


    def remove_Last(self):
        prior=self.ids.calculator_input.text
        prior=prior[0:-1]               # important to understand 
        self.ids.calculator_input.text=prior

    def pos_neg_Function(self):
        prior=self.ids.calculator_input.text
        if "-" in prior:
            self.ids.calculator_input.text=f'{prior.replace("-","")}'
        else:
            self.ids.calculator_input.text=f"-{prior}"
        

class calculator_APP(App):
    def build(self):
        Window.size=(500,700)
        Window.clearcolor=(0,0,0,1)
        return kivyBuilderFunction()

calculator_APP().run()
