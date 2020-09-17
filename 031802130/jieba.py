import jieba

def jieba_list(text):
    items=[]
    s=""
    for i in range(0,len(text)):
        if '\u4e00' <= text[i] <= '\u9fff':
            s += text[i]
        elif text[i] == '。':
            if s != "":
                items.append(s)
                s = ""
    if s != "":
        items.append(s)
        s = ""
    test_items = [[i for i in jieba.lcut(item)] for item in items]
    return test_items


if __name__ == '__main__':
    f = open(sys.argv[1], 'r',encoding='UTF-8')
    text=f.read()
    list = jieba_list(text)
    print(list)
    f.close()
