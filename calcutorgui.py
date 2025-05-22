import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 


class Gridlayout(GridLayout):
    
    #initialise infinite keywords
    def __init__(self, **kwargs):
        
        #call grid layout constructor 
        
        super(GridLayout, self).__init__(**kwargs)
        
        
        #set columns
        self.cols =2.
        
        #Add widgets
        self.add_widget(Label(text ="First value "))
        
        # add input box
        
        self.first = TextInput(multiline = False)
        self.add_widget(self.first)



        #SECOND 
        
        self.add_widget(Label(text ="Operation: "))
        
        # add input box
        
        self.operation = TextInput(multiline = False)
        self.add_widget(self.operation)


    
        ## Second Value 
        self.add_widget(Label(text ="Second Value: "))
                
                # add input box
                
        self.second = TextInput(multiline = False)
        self.add_widget(self.second)




class MyCalc(App):
    def build(self):
        return GridLayout()
        
    
    
if __name__ == "__main__":
    MyCalc().run()
    
