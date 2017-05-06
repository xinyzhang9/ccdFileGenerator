import re
from datetime import date

# test_str = 	'''CCD,1919191919,90,1,2,100,019,,12500.00,12500.00,123456,1000.00,13500.00,0.0725,050217,07.359,,050118,,,12,,,060117,01,12,,0,0.00,,,,2,,,,,,,,,,050217,,,01,01,,2,,,,,,,,,,,Joe Customer,015,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0207,,,,,,,,,,,,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,999999999,001,,:joe::customer:,50,,,,,,123 Fiserv Drive,Brookfield WI,53045,414444141,123 Fiserv Drive,Brookfield WI,53045,,,01251985,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,DL,,,,,,DL,US,,,,,,,,Joe Customer,,,,,Brookfield WI,53045,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''

# arr = test_str.split(',')
# print len(arr)

# for i in range(len(arr)):
# 	if arr[i] != '':
# 		print '{} -- {}'.format(i+1,arr[i])

import contextlib
import OpenSSL.crypto
import os
import requests
import ssl
import tempfile
import xml.etree.ElementTree as ET
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Daric.settings")
from home.models import TFSBLoanApp,TradeLine

data = {}

instance = TFSBLoanApp.objects.get(id=115)
for field,val in instance:
	if val != '':
		# print field,val
		data[field] = val

data2 = {}

data2['proceeds_amount'] = data['LoanAmount']
data2['check_amount'] = data['LoanAmount']
data2['original_interest'] = 0
data2['contract_amount'] = 0
data2['term'] = data['term']
data2['b1_name'] = data['FirstName']+' '+data['LastName']
data2['mail_street_address'] = data['Address1']
data2['mail_city_state'] = data['City']+' '+data['State']
data2['mail_zip'] = data['Zip']
data2['home_phone_number'] = data['PreferredPhone'].replace('(','').replace(')','').replace('-','')
data2['property_street_address'] = data['Address1']
data2['property_city_state'] = data['City']+' '+data['State']
data2['property_zip'] = data['Zip']
data2['b1_birthday'] = data['DateOfBirth'].replace('/','')
data2['b1_ID_type'] = 'SSN'
data2['b2_ID_type'] = 'SSN'
data2['b2_issue_contry'] = 'US'
data2['b2_street_address'] = data['CoApp_StreetAddress']
data2['b2_city_state'] = data['CoApp_City']+' '+data['CoApp_State']
data2['b2_zip'] = data['CoApp_Zip']
data2['purpose_code'] = '02' #Debt Consolidation
data2['b2_phone_number'] = data['CoApp_Phone'].replace('(','').replace(')','').replace('-','')
data2['marital_status'] = '0' # married
data2['personal_residence_flag'] = '0' #own
data2['qualifying_income'] = str(float(data['GrossAnnualIncome']) + float(data['CoApp_IncomeGross']))
data2['b2_homeownner_code'] = '0' # own
data2['b2_birthday'] = data['CoApp_DateOfBirth'].replace('/','')
data2['b1_credit_rating'] = '1' # data['fico_model_used']=732
data2['b1_employer_name'] = data['EmployerName']
data2['b2_employer_name'] = data['CoApp_EmployerName']




def parse_data(data,default,key):
	if key in data:
		return data[key]
	elif key in default:
		return default[key]
	else:
		return ''

def make_str(s,length):
	res = ''
	str_length = len(s)
	space_length = length-str_length
	res += s
	res += ' '*space_length
	return res

def makeccd(data):
	# for key,val in data.items():
	# 	print key,val
	default = {}
	default['loan_number'] = '1919191919'
	default['interest_type'] = '1'
	default['payment_type'] = '2'
	default['call_code'] = '100'
	default['originating_branch'] = '019'
	default['proceeds_amount'] = '12500.00'
	default['check_amount'] = '12500.00'
	default['check_number'] = '123456'

	default['original_interest'] = '1000.00'
	default['contract_amount'] = '13500.00'
	default['interest_rate'] = '0.0725'
	default['apr'] = '07.359'
	default['maturity_date'] = '050118'
	default['term'] = '36'
	default['first_pmt_due_date'] = '060117'
	default['pmt_due_day'] = '01'
	default['no_of_pmt'] = '12'
	default['pmt_frequency'] = '0'
	default['escrow_pmt_amount'] = '0.00'
	default['repayment_plan'] = '2'
	default['interest_pmt_type'] = '2'
	default['b1_name'] = 'Beth Testcase'
	default['officer_number'] = '015'
	default['b1_tin'] = '999999999'
	default['b1_relationship'] = '001'
	default['mail_street_address'] = '123 Fiserv Drive'
	default['mail_city_state'] = 'Brookfield WI'
	default['mail_zip'] = '53045'
	default['home_phone_number'] = '414444141'
	default['property_street_address'] = '123 Fiserv Drive'
	default['property_city_state'] = 'Brookfield WI'
	default['property_zip'] = '53045'
	default['b1_birthday'] = '01251985'
	default['b1_ID_type'] = 'DL'
	default['b2_ID_type'] = 'DL'
	default['b2_issue_contry'] = 'US'
	default['b2_city_state'] = 'Brookfield WI'
	default['b2_zip'] = '53045'
	default['country_code'] = '001' #US

	loan_number = parse_data(data,default,'loan_number')
	interest_type = parse_data(data,default,'interest_type')
	payment_type = parse_data(data,default,'payment_type')
	call_code = parse_data(data,default,'call_code')
	originating_branch = parse_data(data,default,'originating_branch')
	proceeds_amount = parse_data(data,default,'proceeds_amount')
	check_amount = parse_data(data,default,'check_amount')
	check_number = parse_data(data,default,'check_number')
	original_interest = parse_data(data,default,'original_interest')
	contract_amount = parse_data(data,default,'contract_amount')
	interest_rate = parse_data(data,default,'interest_rate')
	apr = parse_data(data,default,'apr')
	maturity_date = parse_data(data,default,'maturity_date')
	term = parse_data(data,default,'term')
	first_pmt_due_date = parse_data(data,default,'first_pmt_due_date')
	pmt_due_day = parse_data(data,default,'pmt_due_day')
	no_of_pmt = parse_data(data,default,'no_of_pmt')
	escrow_pmt_amount = parse_data(data,default,'escrow_pmt_amount')
	pmt_frequency = parse_data(data,default,'pmt_frequency')
	repayment_plan = parse_data(data,default,'repayment_plan')
	interest_pmt_type = parse_data(data,default,'interest_pmt_type')
	b1_name = parse_data(data,default,'b1_name')
	officer_number = parse_data(data,default,'officer_number')
	b1_tin = parse_data(data,default,'b1_tin')
	b1_relationship = parse_data(data,default,'b1_relationship')
	mail_street_address = parse_data(data,default,'mail_street_address')
	mail_city_state = parse_data(data,default,'mail_city_state')
	mail_zip = parse_data(data,default,'mail_zip')
	home_phone_number = parse_data(data,default,'home_phone_number')
	property_street_address = parse_data(data,default,'property_street_address')
	property_city_state = parse_data(data,default,'property_city_state')
	property_zip = parse_data(data,default,'property_zip')
	b1_birthday = parse_data(data,default,'b1_birthday')
	b1_ID_type = parse_data(data,default,'b1_ID_type')
	b2_ID_type = parse_data(data,default,'b2_ID_type')
	b2_issue_contry = parse_data(data,default,'b2_issue_contry')
	b2_city_state = parse_data(data,default,'b2_city_state')
	b2_zip = parse_data(data,default,'b2_zip')
	purpose_code = parse_data(data,default,'purpose_code')
	b2_birthday = parse_data(data,default,'b2_birthday')
	b2_homeownner_code = parse_data(data,default,'b2_homeownner_code')
	b1_credit_rating = parse_data(data,default,'b1_credit_rating')
	b2_phone_number = parse_data(data,default,'b2_phone_number')
	marital_status = parse_data(data,default,'marital_status')
	personal_residence_flag = parse_data(data,default,'personal_residence_flag')
	b1_employer_name = parse_data(data,default,'b1_employer_name')
	b2_employer_name = parse_data(data,default,'b2_employer_name')
	country_code = parse_data(data,default,'country_code')
	b2_street_address = parse_data(data,default,'b2_street_address')

	lst = ['']*1515

	lst[0] = 'CCD'
	lst[1] = loan_number[0:10]
	lst[2] = '90'
	lst[3] = interest_type[0]
	lst[4] = payment_type[0]
	lst[5] = call_code[0:3]
	lst[6] = originating_branch[0:3]
	lst[8] = str('%.2f' % float(proceeds_amount))
	lst[9] = str('%.2f' % float(check_amount))
	lst[10] = check_number[0:12]
	lst[11] = str('%.2f' % float(original_interest))
	lst[12] = str('%.2f' % float(contract_amount))
	lst[13] = str('%.4f' % float(interest_rate))
	lst[14] = date.today().strftime('%Y%m%d')
	lst[15] = str('%.3f' % float(apr))
	lst[17] = maturity_date
	lst[20] = term[0:3]
	lst[23] = first_pmt_due_date
	lst[24] = pmt_due_day[0:2]
	lst[25] = no_of_pmt[0:3]
	lst[27] = pmt_frequency[0]
	lst[28] = str('%.2f' % float(escrow_pmt_amount))
	lst[32] = repayment_plan[0]
	lst[48] = interest_pmt_type[0]
	lst[59] = make_str(b1_name,15)
	lst[60] = officer_number[0:3]
	lst[62] = make_str(b1_employer_name,15)
	lst[79] = purpose_code[0:1]
	lst[81] = country_code[0:3]
	lst[217] = personal_residence_flag[0]
	lst[228] = date.today().strftime('%Y%m%d') #application date
	lst[332] = b1_tin[0:14]
	lst[323] = b1_relationship[0:3]
	lst[325] = make_str(b1_name,35)
	lst[332] = make_str(mail_street_address,35)
	lst[333] = make_str(mail_city_state,35)
	lst[334] = mail_zip[0:9]
	lst[335] = home_phone_number[0:10]
	lst[336] = make_str(property_street_address,35)
	lst[337] = make_str(property_city_state,35)
	lst[338] = property_zip[0:9]
	lst[341] = b1_birthday
	lst[350] = b1_credit_rating[0]
	lst[625] = b1_ID_type[0:2]
	lst[631] = b2_ID_type[0:2]
	lst[632] = b2_issue_contry[0:2]
	lst[640] = make_str(b1_name,40)
	lst[642] = make_str(mail_street_address,40)
	lst[643] = make_str(b2_street_address,40)
	lst[645] = make_str(b2_city_state,27)
	lst[646] = b2_zip[0:9]
	lst[647] = b2_phone_number[0:10]
	lst[650] = b2_birthday
	lst[667] = make_str(b2_employer_name,40)
	lst[671] = b2_homeownner_code[0]

	return ','.join(lst)


res = makeccd(data2)
print res