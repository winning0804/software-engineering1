import sys
import jieba

def jieba_list(text):
    items=""
    s=""
    for i in range(0,len(text)):
        if '\u4e00' <= text[i] <= '\u9fff':
            s += text[i]
        elif text[i] == '。':
            if s != "":
                items += s
                s = ""
    if s != "":
        items += s
        s = ""
    #print(items)
    test_items = jieba.lcut(items, cut_all=True)
    return test_items

def jaccard(text1,text2):
    delete_text1 = set(text1)
    delete_text2 = set(text2)
    temp = 0
    for i in delete_text1:
        if i in delete_text2:
            temp += 1
    fenmu = len(delete_text2) + len(delete_text1) - temp  # 并集
    jaccard_coefficient = float(temp / fenmu)  # 交集
    return jaccard_coefficient

if __name__ == '__main__':
    f1 = open(sys.argv[1], 'r',encoding='UTF-8')
    f2 = open(sys.argv[2], 'r', encoding='UTF-8')
    text1=f1.read()
    text2=f2.read()
    list1 = jieba_list(text1)
    list2 = jieba_list(text2)
    count=jaccard(list1,list2)
    print(count)
    #print("【返回列表】：{0}".format(list1))
    #print("【返回列表】：{0}".format(list2))
    f1.close()
    f2.close()
    
