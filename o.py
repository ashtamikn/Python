>>> import re
>>> pattern='phone'
>>> re.search(pattern,text)
<_sre.SRE_Match object; span=(10, 15), match='phone'>
>>> match=re.search(pattern,text)
>>> match
<_sre.SRE_Match object; span=(10, 15), match='phone'>
>>> match.span()
(10, 15)
>>> match.start()
10
>>> match.end()
15
>>> match
<_sre.SRE_Match object; span=(10, 15), match='phone'>
>>> text
'the agent phone no is 408-555-1234.call soon'
>>> matches=re.findall('phone',text)
>>> matches
['phone']
text='my phone no is 408-555-1234'
 phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)#r  is used to tell python that its not \t or \n
>>> phone
<_sre.SRE_Match object; span=(15, 27), match='408-555-1234
 phone=re.search(r'\d{3}-\d{3}-\d{4}',text)
>>> phone
<_sre.SRE_Match object; span=(15, 27), match='408-555-1234'>
>>> 
phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
>>> results=re.search(phone_pattern,text)
>>> results.group(1)
'408'>>> re.search(r'cat','the cat is here')
<_sre.SRE_Match object; span=(4, 7), match='cat'>
>>> re.findall(r'at','the cat in the hat sat there')
['at', 'at', 'at']
>>> re.findall(r'.at','the cat in the hat sat there')
['cat', 'hat', 'sat']
>>> re.findall(r'^\d','1 is a number')
['1']
>>> phrase='there are 3 numbers 34 inside 5 this sentence'
>>> pattern=r'[^\d]
  File "<stdin>", line 1
    pattern=r'[^\d]
                  ^
SyntaxError: EOL while scanning string literal
>>> text='this is a string ! but it has punctuation.how can we remove it?'
>>> re.findall(r'[^!.?]+',text)
['this is a string ', ' but it has punctuation', 'how can we remove it']
>>> re.findall(r'[^!.? ]+',text)
['this', 'is', 'a', 'string', 'but', 'it', 'has', 'punctuation', 'how', 'can', 'we', 'remove', 'it']
>>> re.findall(r'[^!.? ]',text)
['t', 'h', 'i', 's', 'i', 's', 'a', 's', 't', 'r', 'i', 'n', 'g', 'b', 'u', 't', 'i', 't', 'h', 'a', 's', 'p', 'u', 'n', 'c', 't', 'u', 'a', 't', 'i', 'o', 'n', 'h', 'o', 'w', 'c', 'a', 'n', 'w', 'e', 'r', 'e', 'm', 'o', 'v', 'e', 'i', 't']
>>> re.findall(r'[^!.? ]+',text)
['this', 'is', 'a', 'string', 'but', 'it', 'has', 'punctuation', 'how', 'can', 'we', 'remove', 'it']
>>> clean=re.findall(r'[^!.? ]+',text)
>>> ' '.join(clean)
'this is a string but it has punctuation how can we remove it'
>>> text='hypen-words long-ishh'
>>> pattern=r'[\w]+
  File "<stdin>", line 1
    pattern=r'[\w]+
                  ^
SyntaxError: EOL while scanning string literal
>>> pattern=r'[\w]+'
>>> re.findall(pattern,text)
['hypen', 'words', 'long', 'ishh']
>>> pattern=r'[\w]+-[\w]+'
>>> re.findall(pattern,text)
['hypen-words', 'long-ishh']
>>> 


