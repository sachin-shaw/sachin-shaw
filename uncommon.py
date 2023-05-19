def uncommon_words(str1,str2):
    words1=str1.split()
    words2=str2.split()

    set1=set(words1)
    set2=set(words2)
    uncommon_words=set1.symmetric_difference(set2)
    return uncommon_words

str1='the quick brown fox'
str2='jumped over the lazy dog'
result=uncommon_words(str1,str2)
print(result)