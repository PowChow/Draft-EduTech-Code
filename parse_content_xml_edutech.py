import xml.etree.ElementTree as ET
import csv

tree = ET.parse("2015EdTech/class_content.xml")
root = tree.getroot()

content_list = ['e-log', 'children', 'history']
elog_list = ['anon', 'type', 'data', 'when', 'uid']
history_list = ['subject', 'anon', 'content']

# open a file for writing
with open('./classdiscussion_2015edtech.csv', 'w') as data: 
	csvwriter = csv.writer(data)
	data_head = []

	count = 0
	for thread in root.findall('content'):
		data = []
		#elog = thread.find('e-log').text
		print thread.find('e-log').text

		#student_list = []

		# if count == 0:
		# 	name = thread.find('Name').tag
		# 	data_head.append(name)
		# 	PhoneNumber = thread.find('PhoneNumber').tag
		# 	data_head.append(PhoneNumber)
		# 	EmailAddress = thread.find('EmailAddress').tag
		# 	data_head.append(EmailAddress)
		# 	Address = thread[3].tag
		# 	data_head.append(Address)
		# 	csvwriter.writerow(data_head)
		# 	count = count + 1

		# name = thread.find('Name').text
		# data.append(name)
		# PhoneNumber = thread.find('PhoneNumber').text
		# data.append(PhoneNumber)
		# EmailAddress = thread.find('EmailAddress').text
		# data.append(EmailAddress)
		# Address = thread[3][0].text
		# address_list.append(Address)
		# City = thread[3][1].text
		# address_list.append(City)
		# StateCode = thread[3][2].text
		# address_list.append(StateCode)
		# PostalCode = thread[3][3].text
		# address_list.append(PostalCode)
		# data.append(address_list)
		# csvwriter.writerow(data)
