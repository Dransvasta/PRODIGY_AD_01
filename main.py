from flet import *

def main(page: Page):
    bgc='#CCD5AE'
    butc='#E0E5B6'
    screenc='#FAEDCE' # or #FEFAE0
    butts=10
    page.window.width = 400
    page.window.height = 715
    page.bgcolor='#ffffff'
    def eval_expression(expression):
        try:
            # Tokenize the expression
            tokens=[]
            s=""
            for i in expression:
                if i in "+-*/%^":
                    tokens.append(s)
                    tokens.append(i)
                    s=""
                else:
                    s+=i
            tokens.append(s)
            
            if len(tokens) == 0:
                return "0"  # Return 0 if expression is empty
            
            # Initialize the result with the first number
            result = float(tokens[0])
            i = 1
            
            while i < len(tokens):
                operator = tokens[i]
                next_number = float(tokens[i + 1])
                
                if operator == '+':
                    result += next_number
                elif operator == '-':
                    result -= next_number
                elif operator == '*':
                    result *= next_number
                elif operator == '/':
                    if next_number == 0:
                        return "Error"  # Avoid division by zero
                    result /= next_number
                elif operator == '^':
                    result **= next_number
                elif operator == '%':
                    result %= next_number
                
                i += 2  # Move to the next operator
            
            return str(result)  # Return the result as a string
        except Exception as e:
            return str(e)  # Return "Error" if evaluation fails
    screentext = Text(value="", color=colors.WHITE, size=30)
    def buttonclick(a):
        screentext.value+=a+""
        page.update()

    def equalbutton():
        result = eval_expression(screentext.value.strip())  # Evaluate the expression
        screentext.value = result  # Update the screen with the result
        page.update()
    def cleartext():
        screentext.value=''
        page.update()
    def clearonetext():
        screentext.value=screentext.value[:-1]
        page.update()
    page.padding=padding.only(left=10,right=10,top=10,bottom=10)
    container = Container(
        width=380,
        height=660,
        bgcolor=bgc,
        border=border.all(color='#FAEDCE',width=3),
        border_radius=border_radius.all(value=26.5),
        padding=padding.only(left=10,right=10,top=10,bottom=10),
        content=Column(controls=[
            Container(
                width=340,
                height=200,
                padding=padding.all(15),
                bgcolor=screenc,
                margin=margin.only(top=5),
                border_radius=border_radius.all(30),
                content=Column(
            controls=[
                screentext
            ],
            alignment=MainAxisAlignment.END,  # Align items to the bottom
            horizontal_alignment=CrossAxisAlignment.START  # Align items to the left
        )
            ),
            Container(
                width=340,
                height=415,
                margin=margin.only(top=15),
                content=Column(
                    controls=[
                        Row(controls=[
                            ElevatedButton(content=Container(
                                content=Text(value='+',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('+')),
                            ElevatedButton(content=Container(
                                content=Text(value='-',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('-')),
                            ElevatedButton(content=Container(
                                content=Text(value='*',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('*')),
                            ElevatedButton(content=Container(
                                content=Text(value='/',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('/'))
                        ]),
                        Row(controls=[
                            Container(
                                width=255,
                                height=240,
                                
                                content=Column(controls=[
                                    Row(controls=[ElevatedButton(content=Container(
                                content=Text(value='1',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('1')),ElevatedButton(content=Container(
                                content=Text(value='2',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('2')),ElevatedButton(content=Container(
                                content=Text(value='3',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('3'))],
                                ),Row(controls=[ElevatedButton(content=Container(
                                content=Text(value='4',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('4')),ElevatedButton(content=Container(
                                content=Text(value='5',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('5')),ElevatedButton(content=Container(
                                content=Text(value='6',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('6'))],
                                ),Row(controls=[ElevatedButton(content=Container(
                                content=Text(value='7',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('7')),ElevatedButton(content=Container(
                                content=Text(value='8',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('8')),ElevatedButton(content=Container(
                                content=Text(value='9',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('9'))],
                                )
                                ],spacing=40)
                            )
                            
                        ,Container(
                            width=80,
                            height=240,
                            
                            
                            content=Column(controls=[
                                ElevatedButton(content=Container(
                                content=Text(value='AC',size=21),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=110,width=76,on_click=lambda _:cleartext()),
                                ElevatedButton(content=Container(
                                content=Text(value='C',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=110,width=76,on_click=lambda _:clearonetext())
                            ])
                        )]),
                        Container(
                            offset=transform.Offset(x=0,y=-0.4),
                            content=Row(controls=[
                            ElevatedButton(content=Container(
                                content=Text(value='^',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('^')),ElevatedButton(content=Container(
                                content=Text(value='0',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('0')),ElevatedButton(content=Container(
                                content=Text(value='%',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:buttonclick('%')),
                                Container(
                                margin=margin.only(left=8),
                                content=ElevatedButton(content=Container(
                                content=Text(value='=',size=30),
                                alignment=alignment.center,
                                offset=transform.Offset(y=-0.08,x=0)
                                 
                                ),bgcolor=butc,color=colors.WHITE,height=50,width=76,on_click=lambda _:equalbutton()))
                                
                                
                        ]))
                    ],spacing=40
                )
            )
        ])
    )
    page.add(container)
app(target=main)