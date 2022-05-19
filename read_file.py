f=open('test.txt','r')
text=f.read()
word_lst=text.split(' ')
for word in word_lst:
        print(word)
