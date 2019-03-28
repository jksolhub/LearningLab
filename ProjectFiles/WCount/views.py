from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    #return render(request,'home.html',{'Hello':'How are you'})
    return render(request,'home.html')
def count(request):
    txt_fulltext=request.GET['fulltext']
    wordlist = txt_fulltext.split()
    word_dict={}
    for word in wordlist:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    sortedwords=sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html', {'txt_fulltext':txt_fulltext,'word_count':len(wordlist),'Word_Dictionary':sortedwords})
def about(request):
        return render(request,'about.html')