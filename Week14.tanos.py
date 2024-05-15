word=input()
bomb=input()

while True:
  tmp=word.replace(bomb,"")
  if tmp==word:
    break
  word=tmp
print(tmp if len(tmp)>=1 else "FRULA")
