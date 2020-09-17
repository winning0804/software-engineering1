import sys
import jieba

from sys import argv


def stopwordslist():
    stopwords = [line.strip() for line in open('D:\study\sim_0.8\stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords

def jieba_list(text):
    items = ""
    s = ""
    stopwords = stopwordslist()
    for i in range(0, len(text)):
        if '\u4e00' <= text[i] <= '\u9fff':
            if text[i] not in stopwords:
                s += text[i]
        elif text[i] == '。':
            if s != "":
                items += s
                s = ""
    if s != "":
        items += s
        s = ""
    # print(items)
    test_items = jieba.lcut(items, cut_all=True)
    return test_items

def jaccard(text1,text2):
    # 将分词去重
    delete_text1 = set(text1)
    delete_text2 = set(text2)
    # print(delete_text1)
    # print(delete_text2)

    # 记录相交分词的个数
    temp = 0
    for i in delete_text1:
        if i in delete_text2:
            temp += 1
    fenmu = len(delete_text2) + len(delete_text1) - temp  # 并集
    jaccard_coefficient = float(temp / fenmu)  # 交集
    return jaccard_coefficient

if __name__ == '__main__':
    f1 = open(argv[1],'r',encoding='UTF-8')
    f2 = open(argv[2],'r',encoding='UTF-8')
    f3 = open(argv[3],'w',encoding='UTF-8')

    text1=f1.read()
    text2=f2.read()

    list1 = jieba_list(text1)
    list2 = jieba_list(text2)
    count = jaccard(list1, list2)


    f3.write(str(count))

    #print (f1.read())
    f1.close()
    f2.close()
    f3.close()
