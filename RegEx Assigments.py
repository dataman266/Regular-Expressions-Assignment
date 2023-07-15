#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
import re

string = "Abc123"
pattern = r'^[a-zA-Z0-9]+$'

if re.match(pattern, string):
    print("String contains only a-z, A-Z, and 0-9")
else:
    print("String does not contain only a-z, A-Z, and 0-9")


# In[2]:


#Question 2
string = "ab"

if re.match(r'ab*', string):
    print("Match found")
else:
    print("Match not found")


# In[36]:


#Question 3
string = "abbb"

if re.match(r'ab+', string):
    print("Match found")
else:
    print("Match not found")


# In[37]:


#Question 4
string = "ac"

if re.match(r'ab?', string):
    print("Match found")
else:
    print("Match not found")


# In[38]:


#Question 5
string = "abbb"

if re.search(r'ab{3}', string):
    print("Match found")
else:
    print("Match not found")


# In[39]:


#Question 6
text = "ImportanceOfRegularExpressionsInPython"
split_words = re.findall('[A-Z][^A-Z]*', text)
print(split_words)


# In[40]:


#Question 7
string = "abb"
if re.match(r'ab{2,3}', string):
    print("Match found")
else:
    print("Match not found")


# In[41]:


#Question 8
string = "this_is_a_sample_text_with_lowercase_letters"
lowercase_sequences = re.findall(r'[a-z]+', string)
print(lowercase_sequences)


# In[42]:


#Question 9
string = "alotofrandomtextb"
if re.match(r'a.*b$', string):
    print("Match found")
else:
    print("Match not found")


# In[43]:


#Question 10
string = "Hello World"
match = re.match(r'\b\w+', string)
if match:
    print("Match found:", match.group())
else:
    print("Match not found")


# In[44]:


#Question 11
string = "Abc123_"
if re.match(r'^[a-zA-Z0-9_]+$', string):
    print("Match found")
else:
    print("Match not found")


# In[45]:


#Question 12
string = "42 is the answer"
if re.match(r'^42', string):
    print("Match found")
else:
    print("Match not found")


# In[46]:


#Question 13
ip_address = "192.168.001.001"
new_ip_address = re.sub(r'\b0+(\d)', r'\1', ip_address)
print(new_ip_address)


# In[47]:


#Question 15
string = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

for word in searched_words:
    if re.search(word, string):
        print(f"Match found for '{word}'")
    else:
        print(f"No match found for '{word}'")


# In[48]:


#Question 16
string = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

match = re.search(searched_word, string)
if match:
    print(f"Match found for '{searched_word}' at index {match.start()}")
else:
    print(f"No match found for '{searched_word}'")


# In[49]:


#Question 17
string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

substrings = re.findall(pattern, string)
print(substrings)


# In[50]:


#Question 18
string = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

matches = re.finditer(pattern, string)
for match in matches:
    print(f"Found '{match.group()}' at index {match.start()}")


# In[52]:


#Question 19
date = '2022-05-15'
new_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', date)
print(new_date)


# In[53]:


#Question 20
string = 'An apple and an elephant entered the room.'
matches = re.findall(r'\b[aAeE]\w+', string)
print(matches)


# In[54]:


#Question 21
string = 'abc 123 def 456 xyz'
numbers = re.findall(r'\d+', string)

for number in numbers:
    position = string.index(number)
    print(f"Number: {number}, Position: {position}")


# In[55]:


#Question 22
string = 'abc 123 def 456 xyz 789'
numbers = re.findall(r'\d+', string)
max_value = max(map(int, numbers))

print(f"Maximum Numeric Value: {max_value}")


# In[56]:


#Question 23
string = 'HelloWorldHowAreYou'
new_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)

print(new_string)


# In[57]:


#Question 24
string = 'AbcDeFGhIjKlM'
sequences = re.findall(r'[A-Z][a-z]+', string)

print(sequences)


# In[58]:


#Question 25
sentence = 'This is is a test test sentence'
new_sentence = re.sub(r'\b(\w+)\b(?:\s+\1\b)+', r'\1', sentence)

print(new_sentence)


# In[59]:


#Question 26
string = input("Enter a string: ")

if re.search(r'\w$', string):
    print("String ends with an alphanumeric character")
else:
    print("String does not end with an alphanumeric character")


# In[60]:


#Question 27
string = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = re.findall(r'#[A-Za-z0-9_]+', string)
print(hashtags)


# In[61]:


#Question 28
text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

new_text = re.sub(r'<U\+\w+>', '', text)
print(new_text)


# In[62]:


#Question 29
with open('RegExtext.txt', 'r') as file:
    text = file.read()

dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
print(dates)


# In[63]:


#Question 30
text = 'Python Exercises, PHP exercises.'

new_text = re.sub(r'[ ,.]', ':', text)
print(new_text)


# In[ ]:




