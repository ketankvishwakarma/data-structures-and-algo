


def isValid(s):
    print("input {}".format(s))
    paranthesis = {")":"(","}":"{","]":"["}
    stack = []
    if len(s)<2:
        return False
    for x in s:
        print("{}".format(x))
        if len(stack) ==0:
            stack.append(x)
        elif x in paranthesis.keys() and paranthesis[x] == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
        print("--> {}".format(stack))
    return len(stack)==0


if __name__ =="__main__":
    #print(isValid("([)]"))
    print(isValid("({})"))

