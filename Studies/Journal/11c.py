import re

poem = """In winter I get up at night 
And dress by yellow candle-light. 
In summer, quite the other way, 
I have to go to bed by day. 

I have to go to bed and see 
The birds still hopping on the tree, 
Or hear the grown-up people's feet 
Still going past me in the street."""

ght = re.findall("\w+ght", poem)
ay = re.findall("\w+ay", poem)

my_dict = {"ght": ght, "ay": ay}

print(f"Following are the rhyming words : \n{my_dict}")
