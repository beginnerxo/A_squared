import kivy

import calculator

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.core.window import Window

from kivy.lang import Builder


#set window size 
Window.size = (500,700)


Builder.load_file('calc.kv')



class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"
        
    #button pressing function 
    def button_press(self, button):
        
        #default textbox variable 
        default = self.ids.calc_input.text
        
        #determine whether the default is 0
        if default == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{default}{button}'
    
    
    
    #backspace
    def backspace(self):
        default = self.ids.calc_input.text
        
        default_list = list(str(default))        
        new_value=""
        
        for i in range((len(default_list))-1):
            new_value =new_value+ default_list[i]
            
        self.ids.calc_input.text = f'{new_value}'
        
        
        
    
    def dot(self):
        default = self.ids.calc_input.text
        default = f"{default}."
        self.ids.calc_input.text = f'{default}'
    
        
               
    #operation sign functions 
    def math_sign(self,sign):
        #default textbox variable 
        default = self.ids.calc_input.text
        
        #adding the plus sign 
        self.ids.calc_input.text = f'{default}{sign}'
        
    
    
    
    
    
    
        
    def equals(self):
         default = self.ids.calc_input.text
         
         #for_addition 
         
         if "+" in default:
             num_list = default.split("+")
             
             answer = float(0)
             for i in num_list:
                answer = calculator.add(answer,float(i))
             
             #printing the answer in the text box
             self.ids.calc_input.text = f'{answer}'
            
        #for subtraxion  
         if "-" in default:
             num_list = default.split("-")
             
             answer = float(num_list[0])
             #print(answer)
             
             for i in range(len(num_list)):
                answer = calculator.sub(answer,float(i+1)) 
             self.ids.calc_input.text = f'{answer}'

         if "X" in default:
             num_list = default.split("-")
             
             answer = float(num_list[0])
             #print(answer)
             
             for i in range(len(num_list)):
                answer = calculator.mul(answer,float(i+1)) 
             self.ids.calc_input.text = f'{answer}'
             
         if "/" in default:
             num_list = default.split("-")
             
             answer = float(num_list[0])
             #print(answer)
             
             for i in range(len(num_list)):
                answer = calculator.div(answer,float(i+1)) 
             self.ids.calc_input.text = f'{answer}'
             
            
            
        
        




class MyCalc(App):
    def build(self):
        return MyLayout()
        
    
    
if __name__ == "__main__":
    MyCalc().run()
    
