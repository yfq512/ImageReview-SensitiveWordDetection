def clean_str(text):
    pass_sign = [' ','`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|',':',';','"','?','/','<','>',',','.','：','；','“','‘','《','》','，','。','？']
    x = ''
    for n in text:
        if not n in pass_sign:
            x = x + n
    if len(x) == 0:
        return None
    return x

def nsword_fit(text):
    text = clean_str(text)
    keywords_path = './keywords.txt'
    keywords_list = []
    for n in open(keywords_path):
        if not (n == '' or n == '\n'): # 删除敏感词汇列表非法字符
            keywords_list.append(n[:-1])
    keywords_list.append('你') # 添加敏感字符，测试用
    keywords_list.append('我') # 添加敏感字符，测试用
    cnt = 0
    wf_words = []
    for n in keywords_list:
        cnt = 0
        if n in text:
            cnt2 = text.count(n)
            wf_words.append({n:cnt2})
    return wf_words

if __name__ == "__main__":
    print('>>>',nsword_fit('中国'))
