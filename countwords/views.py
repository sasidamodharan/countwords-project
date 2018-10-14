from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fullText = request.GET['fullText']
    fullTextSplit = fullText.split()
    wordDictionary = {}
    for word in fullTextSplit:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedList = sorted(wordDictionary.items(),key=operator.itemgetter(1), reverse = True)
    return render(request,'count.html', {'countOfWords':len(fullTextSplit),'sortedList':sortedList})

def about(request):
    return render(request, 'about.html')
