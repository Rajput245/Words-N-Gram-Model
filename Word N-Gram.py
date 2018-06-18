import random
import nltk
text="""A trade war is an economic conflict resulting from extreme protectionism in which states raise or create tariffs or other trade barriers against each other in response to trade barriers created by the other party.Increased protection causes both nations' output compositions to move towards their autarky position.

Some economists agree that certain economic protections are more costly than others, because they may be more likely to trigger a trade war. For example, if a country were to raise tariffs, then a second country in retaliation may similarly raise tariffs. An increase in subsidies, however, may be difficult to retaliate against by a foreign country. Many poor countries do not have the ability to raise subsidies. In addition, poor countries are more vulnerable than rich countries in trade wars; in raising protections against dumping of cheap products, a government risks making the product too expensive for its people to afford.[citation needed]

Trade wars and protectionism have been implicated by some scholars as the cause of some economic crises, in particular the Great Depression."""

n=3
ngrams={}
words=nltk.word_tokenize(text)
for i in range(len(words)-n):
    grams=' '.join(words[i:i+n])
    if grams not in ngrams.keys():
        ngrams[grams]=[]
    ngrams[grams].append(words[i+n])
    
CurrentGram=' '.join(words[0:n])
result=CurrentGram
for i in range(32):
    if CurrentGram not in ngrams.keys():
        break
    possibilities=ngrams[CurrentGram]
    nextItem=possibilities[random.randrange(len(possibilities))]
    result+=' '+nextItem
    rwords=nltk.word_tokenize(result)
    CurrentGram=' '.join(rwords[len(rwords)-n:len(rwords)])
print(result)