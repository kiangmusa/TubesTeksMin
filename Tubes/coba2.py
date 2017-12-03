from xml.etree import cElementTree as ET
xmlstr = """
 <root>
 <page>
   <title>Chapter 1</title>
   <content>Welcome to Chapter 1</content>
 </page>
 <page>
  <title>Chapter 2</title>
  <content>Welcome to Chapter 2</content>
 </page>
 </root>
 """
root = ET.fromstring(xmlstr)
for page in list(root):
     title = page.find('title').text
     content = page.find('content').text
     print('title: %s; content: %s' % (title, content))

# ab = b.casefold()
    # tokens= nltk.word_tokenize(ab)
    # # print(tokens)
    # ps = PorterStemmer()
    # stemming = []
    # for w in tokens:
    #      stemming.append(ps.stem(w))
    # stop_words = set(stopwords.words('english'))
    # filtered_sentence = []
    # for w in stemming:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
    # # print(filtered_sentence)
    # punctuations = list(string.punctuation)
    # punc = [];
    # for w in filtered_sentence:
    #     if w not in punctuations:
    #         punc.append(w)
    # # print(punc[1])
    # c = {}
    # listTag = set()
    # for w in punc:
    #     try:
    #         listTag.add(w)
    #     except:
    #         pass
    # for item in listTag:
    #     c[item] = {}
    #     c[item][0] = 0
    #
    # jum = 0
    # for w in punc:
    #     jum+=1
    #     c[w][0]+=1
    #
    # for item in c:
    #     c[item][1]=c[item][0]/jum
    #
    # print(dict['0'])