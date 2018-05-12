import requests
from lxml import html
import sys

def search_phone(number):
	r=requests.get("https://cellrevealer.com/Results/"+number+"/")
	tree=html.fromstring(r.content)
	name = tree.xpath("//div[@class='small-12 large-7 medium-7 columns']/table[@class='reverse-phone-results-table']/tbody/tr[3]/td[@class='value']/text()")
	location= tree.xpath("//div[@class='small-12 large-7 medium-7 columns']/table[@class='reverse-phone-results-table']/tbody/tr[5]/td[@class='value']/text()")
	#rint(name[0])
	#print(location[0])
	return name,location


if __name__ == '__main__':

	number=sys.argv[1]
	search_phone(number)
