import tkinter as tk

disValue = 0  # 초기 값 지정
operator = {'+': 1, '-': 2, '/': 3, '*': 4, 'C': 5, '=': 6}
stoValue = 0
opPre = 0


def number_click(value):
    global disValue
    disValue = (disValue*10) + value  # *10을 지워보세요 그러면 알게됩니다.
    str_value.set(disValue)  # disValue의 값으로 수정


def clear():
    global disValue, stoValue, opPre
    disValue = 0
    stoValue = 0
    opPre = 0
    str_value.set(disValue)


def operator_click(value):
    # print("명령", value)
    global disValue, operator, stoValue, opPre
    op = operator[value]  # 연산자라는 것을 알려주는 변수 설정
    if op == 5:
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(disValue)
    elif op == 6:
        if opPre == 1:
            disValue = stoValue + disValue
        if opPre == 2:
            disValue = stoValue - disValue
        if opPre == 3:
            disValue = stoValue / disValue
        if opPre == 4:
            disValue = stoValue * disValue

        str_value.set(disValue)

        str_value.set(str(disValue)) # 필요한 이유 : Transition Handling 오류방지
        disValue = 0
        stoValue = 0
        opPre = 0
    else:
        clear()


def button_click(value):
    print(value)
    try:
        value = int(value)  # why? 정수로 들어가야 하는거죠? 계산때문에?
        number_click(value)
    except:
        operator_click(value)


win = tk.Tk()  # 최상위 창을 만듬
win.title('계산기')  # 프로그램 title을 정함


str_value = tk.StringVar()  # 버튼이 눌렸을때 해당 버튼의 값을 문자로 바꾸는 메소드
str_value.set(str(disValue))  # 바뀐 문자를 edit창에 str(disValue)의 값을 나타게 함
dis = tk.Entry(win, textvariable=str_value, justify='right')  # 계산기 edit 창을 만듬
dis.grid(column=0, row=0, columnspan=4, ipadx=150, ipady=30)  # edit 창 커스텀

calItem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):
        # enumerate()
        # 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
        # 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'

        bt = tk.Button(
            win,
            text=item,
            width=10,
            height=5,
            bg=color,
            fg='#fff',
            command=lambda cmd=item: button_click(cmd),
            # anchor='s' # 버튼안의 문자 위치
        )
        bt.grid(column=k, row=(i+1))


win.mainloop()
# 생성한 윈도우 내부에서 수행되는 마우스 클릭 같은 이벤트들이 발생하게끔 유지해주는 함수이다.