import flet 
from flet import IconButton, Page, Row, icons 
from flet.textfield import TextField

def main(page: Page):
    page.tittle = "Flet Contador"
    page.vertical_alignment = "center"
   
    
    txt_number = TextField (value= "0", text_align="right", width=100)
    
    def minus_click(event):
        txt_number.value = int(txt_number.value) -1
        page.update()
        
    def plus_click(event):
        print("plus_click")
        txt_number.value = int(txt_number.value) +1  
        page.update()
    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, 
                           on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, 
                           on_click=plus_click),
                
             
             ],
            alignment='center'
            
        )
    )  
    
# modo desktop
# flet.app(target=main)


#modo web
flet.app(target=main, view=flet.WEB_BROWSER)