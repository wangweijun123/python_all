str = "abc"
str = str.replace("a", "cccccc")
print(str)




names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.replace(" ", "_").lower()
    usernames.append(name)

print(usernames)




names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

# use enumerate out index
for index,value in enumerate(names):
    print('index = %s, value = %s' %(index, value))
    names[index] = value.replace(" ", "_").lower()

print(names)

# must modify item by index
for index in range(len(names)):
    names[index] = names[index].replace(" ", "_");

print(names)




tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    print(token)
    if (token[0] == '<') and (token[-1] == token[-1]):
        count = count + 1

print(count)



items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
middle = ""
# write your code here
for item in items:
    middle = middle + "<li>"+item+"</li>\n"

html_str = html_str + middle + "</ul>"

print(html_str)


#  resolve method


items = ['first string', 'second string']

html_str = "<ul>\n"
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)


card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  <= 17:
    hand.append(card_deck.pop())







