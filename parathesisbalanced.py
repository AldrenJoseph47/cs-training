stack = []
open_brackets = "([{"
close_brackets = ")]}"
exp = input("Enter an expression with parentheses: ")
for char in exp:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets(top) != closing_brackets(char):
                
def check(myStr):
    stack=[]
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos=close_list.index(i)
            if ((len(stack)>0)and (open_list=[pos]=stack.pop())
            else:
                return "unbalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"
