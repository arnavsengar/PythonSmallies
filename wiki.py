import wikipedia
s=input()
result=wikipedia.summary(s,sentences=2)
print(result)