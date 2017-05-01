import slate as slate
import re
with open('layout.pdf') as f:
	doc = slate.PDF(f)

# for data in doc:
# 	print data

page = doc[0]
index = page.index('Item Nbr Table Name Field Name Type Size Format Field Nbr')
length = len('Item Nbr Table Name Field Name Type Size Format Field Nbr')
data = page[index+length+1:]
print type(data)
data1 = re.sub("\s\s+"," # ",data)
print data1


