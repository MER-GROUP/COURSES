def podpoisk(expression):
    if '(' in expression:
        st = expression.rfind('(')
        en = expression.find(')', st)+1
        skob = expression[st:en]
        i = 1
        while expression[st-i].isdigit():
            i += 1
        tmp_nums = int(expression[st-i+1:st]) if i > 1 else 1
        return podpoisk(expression.replace(str(tmp_nums)+skob, skob[1:-1]*tmp_nums))
    else:
        return expression

def main():
    print(podpoisk(input()))

if __name__ == '__main__':
    main()