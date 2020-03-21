from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def GlobalCovid19():

	url = 'https://www.worldometers.info/coronavirus/'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')

	table = data.findAll('table',{'id':'main_table_countries_today'})

	country = table[0].findAll('tr')


	result = {'header':{'list':None}}

	for rw in country[:1]:
		hd = rw.findAll('th')
		#print(hd[0].text)
		result['header']['list'] = [hd[i].text for i in range(9)]


	for rw in country[1:]:
		cl = rw.findAll('td')
		result[cl[0].text.lower()] = {'list':None,
									  'country':None,
									  'total':None,
									  'new_cases':None,
									  'total_deaths':None,
									  'new_deaths':None,
									  'total_recoverd':None,
									  'active_cases':None,
									  'serious_critical':None,
									  'totalcase_per1million':None}


	for rw in country[1:]:
		cl = rw.findAll('td')
		#print(cl[0].text)
		index = cl[0].text.lower()
		#print(index)
		result[index]['list'] = [cl[i].text for i in range(9)]
		result[index]['country'] = cl[0].text
		result[index]['total'] = cl[1].text
		result[index]['new_cases'] = cl[2].text
		result[index]['total_deaths'] = cl[3].text
		result[index]['new_deaths'] = cl[4].text
		result[index]['total_recoverd'] = cl[5].text
		result[index]['active_cases'] = cl[6].text
		result[index]['serious_critical'] = cl[7].text
		result[index]['totalcase_per1million'] = cl[8].text

	result['total'] = result['total:']
	del result['total:']

	return result


def ThaiCovid19():
	url = 'https://ddc.moph.go.th/viralpneumonia/'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')

	alldata = []

	result = {}

	table = data.findAll('div',{'class':'popup_blog'})
	#print(table[0])
	for i,tb in enumerate(table):


		if i == 1:
			rw = tb.findAll('tr')
			for i in range(len(rw)):
				cl1 = [ r.text for r in rw[i].findAll('td')]
				alldata.append(cl1)


		if i == 0:
			rw = tb.findAll('tr')
			for i in range(len(rw)):
				cl1 = [ r.text for r in rw[i].findAll('td')]
				alldata.append(cl1)
			#print('-------')

	#print(alldata)
	# for i,d in enumerate(alldata):
	# 	print(i,d,'\n\n')

	result['อัพเดต'] = f'{alldata[0][0]} {alldata[12][0]}'
	result['ผู้ป่วยสะสม'] = alldata[3][0]
	result['ผู้ป่วยรายใหม่'] = alldata[3][1]
	result['ผู้ป่วยรุนแรง'] = alldata[5][0]
	result['ผู้ป่วยเสียชีวิต'] = alldata[5][1]
	result['ผู้ป่วยกลับบ้านแล้ว'] = alldata[5][2]
	result['ผู้ป่วยเฝ้าระวังสะสม'] = alldata[8][0]
	result['ผู้ป่วยเฝ้าระวังรายใหม่'] = alldata[8][1]

	result['รักษาพยาบาลอยู่รพ.'] = alldata[11][0]
	result['รักษาพยาบาลกลับบ้าน'] = alldata[11][1]
	result['รักษาพยาบาลสังเกตอาการ'] = alldata[11][2]

	for d in alldata[14:]:
		result['ผู้เดินทางที่คัดกรองสะสมจาก'+d[0]] = d[1] 

	result['อ้างอิง'] = url

	#print(result)
	return result

if __name__ == '__main__':
	data = GlobalCovid19()
	print(data['header']['list'])
	print(data['total']['list'])
	print(data['thailand'])
	thai = ThaiCovid19()
	print(thai)