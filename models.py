from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from borrower.models import CreditProfile
from lender.models import Lender
from smallbusiness.models import SBCreditProfile



class TFSBLoanApp(models.Model):
	IncomeSource1_GMI = models.CharField(default='0',max_length=500)
	IncomeSource1_Job = models.CharField(default='',max_length=500)
	IncomeSource1_Employer = models.CharField(default='',max_length=500)
	IncomeSource2_GMI = models.CharField(default='0',max_length=500)
	IncomeSource2_Job = models.CharField(default='',max_length=500)
	IncomeSource2_Employer = models.CharField(default='',max_length=500)
	IncomeSource3_GMI = models.CharField(default='0',max_length=500)
	IncomeSource3_Job = models.CharField(default='',max_length=500)
	IncomeSource3_Employer = models.CharField(default='',max_length=500)
	IncomeSource4_GMI = models.CharField(default='0',max_length=500)
	IncomeSource4_Job = models.CharField(default='',max_length=500)
	IncomeSource4_Employer = models.CharField(default='',max_length=500)
	IncomeSource5_GMI = models.CharField(default='0',max_length=500)
	IncomeSource5_Job = models.CharField(default='',max_length=500)
	IncomeSource5_Employer = models.CharField(default='',max_length=500)
	fico_model_used = models.CharField(default='742',max_length=100)
	debt_to_income = models.CharField(default='0.33',max_length=100)
	income_verified = models.CharField(default='',max_length=100)
	default_risk_scorecard = models.CharField(default='',max_length=100)
	bankruptcies = models.CharField(default='No',max_length=100)
	latePayment = models.CharField(default='No',max_length=100)
	delinquent_risk_scorecard_101 = models.CharField(default='',max_length=100)
	delinquent_risk_scorecard_102 = models.CharField(default='',max_length=100)
	PreferredPhone = models.CharField(default='',max_length=500)
	DateOfBirth = models.CharField(default='',max_length=500)
	Email = models.CharField(default='',max_length=500)
	FirstName = models.CharField(default='',max_length=500)
	LastName = models.CharField(default='',max_length=500)
	LoanPurpose = models.CharField(default='',max_length=500)
	LoanAmount  = models.CharField(default='',max_length=500)
	OwnOrRent = models.CharField(default='',max_length=500)
	RentAmount = models.CharField(default='',max_length=500)
	temporaryPassword = models.CharField(default='',max_length=100)
	MortgagePayment = models.CharField(default='',max_length=500)
	Address1 = models.CharField(default='',max_length=500)
	City = models.CharField(default='',max_length=500)
	State = models.CharField(default='',max_length=500)
	Zip = models.CharField(default='',max_length=500)
	CurrentAddressTwoYears = models.CharField(default='',max_length=500)
	PreviousAddress1 = models.CharField(default='',max_length=500)
	PreviousCity = models.CharField(default='',max_length=500)
	PreviousState = models.CharField(default='',max_length=500)
	PreviousZip = models.CharField(default='',max_length=500)
	ActiveDutyOrVeteran = models.CharField(default='',max_length=500)
	TerminalServiceDate = models.CharField(default='',max_length=500)
	MilitaryRank = models.CharField(default='',max_length=500)
	MilitaryAllotment = models.BooleanField(default=False)
	DirectDeposit = models.BooleanField(default=False)
	checkingapplicationcomments = models.CharField(default='',max_length=5000)
	incomeverificationcomments = models.CharField(default='',max_length=5000)
	voidedcheckcomments = models.CharField(default='',max_length=5000)
	identificationcomments = models.CharField(default='',max_length=5000)
	creditcardstatementscomments = models.CharField(default='',max_length=5000)
	checkingapplicationSubmitted = models.BooleanField(default=False)
	incomeverificationSubmitted = models.BooleanField(default=False)
	voidedcheckSubmitted = models.BooleanField(default=False)
	identificationSubmitted = models.BooleanField(default=False)
	creditcardstatementsSubmitted = models.BooleanField(default=False)
	checkingapplicationAccepted = models.BooleanField(default=False)
	incomeverificationAccepted = models.BooleanField(default=False)
	voidedcheckAccepted = models.BooleanField(default=False)
	identificationAccepted = models.BooleanField(default=False)
	creditcardstatementsAccepted = models.BooleanField(default=False)
	MilitaryServiceYears = models.CharField(default='', max_length=5000)
	EmployerName = models.CharField(default='',max_length=500)
	JobTitle = models.CharField(default='',max_length=500)
	IncomeOther = models.CharField(default='0',max_length=500)
	IncomeOther2 = models.CharField(default='0',max_length=500)
	CoApp_IncomeOther = models.CharField(default='0',max_length=500)
	IncomeOther3 = models.CharField(default='0',max_length=500)
	IncomeTotal = models.CharField(default='',max_length=500)
	IncomeSource = models.CharField(default='',max_length=500)
	SSN = models.CharField(default='',max_length=500)
	PaymentsObligated = models.CharField(default='',max_length=500)
	PaymentsObligatedAmount = models.CharField(default='',max_length=500)
	CoApplicant = models.CharField(default='',max_length=500)
	CoApp_DateOfBirth = models.CharField(default='',max_length=500)
	CoApp_FirstName = models.CharField(default='',max_length=500)
	CoApp_LastName = models.CharField(default='',max_length=500)
	CoApp_OwnOrRent = models.CharField(default='',max_length=500)
	CoApp_RentAmount = models.CharField(default='',max_length=500)
	CoApp_MortgagePayment = models.CharField(default='',max_length=500)
	CoApp_StreetAddress = models.CharField(default='',max_length=500)
	CoApp_City = models.CharField(default='',max_length=500)
	CoApp_State = models.CharField(default='',max_length=500)
	CoApp_Zip = models.CharField(default='',max_length=500)
	CoApp_Phone = models.CharField(default='',max_length=500)
	CoApp_Email = models.CharField(default='',max_length=500)
	CoApp_SSN = models.CharField(default='',max_length=500)
	CoApp_EmployerName = models.CharField(default='',max_length=500)
	CoApp_IncomeGross = models.CharField(default='',max_length=500)
	CoApp_IncomeSource = models.CharField(default='',max_length=500)
	CoApp_IncomeTotal = models.CharField(default='',max_length=500)
	ReferFriend = models.CharField(default='',max_length=500)
	Consent_Value = models.CharField(default='',max_length=500)
	CoApp_Consent_Value = models.CharField(default='',max_length=500)
	CoApp_CP_Authorization = models.CharField(default='',max_length=500)
	CoApp_TCPA_Release = models.CharField(default='',max_length=500)
	CP_Authorization = models.CharField(default='',max_length=500)
	TCPA_Release = models.CharField(default='',max_length=500)
	CoApp_RelationToApplicant = models.CharField(default='',max_length=500)
	GrossAnnualIncome = models.CharField(default='0',max_length=500)
	decision = models.CharField(default='',max_length=500)
	originationFee = models.CharField(default='',max_length=500)
	apr = models.CharField(default='',max_length=500)
	interestRate = models.CharField(default='',max_length=500)
	interestRatePercent = models.CharField(default='',max_length=500)
	monthlyPayment = models.CharField(default='',max_length=500)
	term = models.CharField(default='36',max_length=500)
	timeStamp = models.DateTimeField(default=datetime.now())

	def __iter__(self):
		for field_name in self._meta.get_all_field_names():
			value = getattr(self, field_name, None)
			yield (field_name, value)

	def tradesActive(self):
		listnow = []
		for trade in self.tradeline_set.all():
			try:
				if float(trade.balance) > 0:
					listnow.append(trade)
			except:
				pass
		return listnow

	def totalbal(self):
		balance = 0.0
		for trade in self.tradeline_set.all():
			try:
				balance += float(trade.balance)
			except:
				pass
		return balance

	def totalmin(self):
		balance = 0.0
		for trade in self.tradeline_set.all():
			try:
				balance += float(trade.minPayment)
			except:
				pass
		return balance



	def revolvingTrades(self):
		finals = self.tradeline_set.all().filter(tradeType='Revolving')
		listnow =[]
		for trade in finals:
			try:
				if float(trade.balance) > 0:
					listnow.append(trade)
			except:
				pass
		return listnow


	def revolvingminPayment(self):
		minPayment = 0;
		for indique in self.revolvingTrades():
			minPayment = minPayment + float(indique.minPayment)
		return minPayment

	def revolvingBalance(self):
		mybalance = 0;
		for indique in self.revolvingTrades():
		 try:
			mybalance = mybalance + float(indique.balance)
		 except:
			pass
		return mybalance

	
	def nonConsLoanAmount(self):
		return float(self.LoanAmount) - float(self.revolvingBalance())

	def coGrossMonthly(self):
	 try:
		return str(float(self.CoApp_IncomeGross) / 1.0)
	 except:
		return 0

	def grossMonthly(self):
		return str(float(self.GrossAnnualIncome) / 12.0)

	def totalMonthly(self):
		now = 0.0
		try:
			now = str(float(self.IncomeTotal) / 12.0)
		except:
			pass
		return now
		return str(float(self.IncomeTotal) / 12.0)
	def seedScore(self):
		fico_model_used = '742'
		debt_to_income = "0.34"
                MilitaryAlloment = False
                DirectDeposit = False
		self.GrossAnnualIncome = str(float(self.IncomeSource1_GMI) + float(self.IncomeSource2_GMI) + float(self.IncomeSource3_GMI) + float(self.IncomeSource3_GMI) + float(self.IncomeSource4_GMI) + float(self.IncomeSource5_GMI))
		self.save()
		try:
			fico_model_used = str(int(self.fico_model_used))
			debt_to_income = str(float(self.debt_to_income))
		except:
			pass
		try:
			MilitaryAlloment = self.MilitaryAllotment
			DirectDeposit = self.DirectDeposit
		except:
			pass
		Credit_Score = [600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800]
		DTI = [0.50, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.40, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.30]
		Val = [29.9, 28.3, 27.7, 27.2, 26.6, 26.1, 25.5, 25.0, 24.4, 23.9, 23.3, 22.8, 22.2, 21.7, 21.1, 20.6, 20.0, 19.5, 18.9, 18.4, 17.9,17.3, 16.8, 16.2, 15.7, 15.1, 14.6, 14.0, 13.5, 12.9, 12.4, 11.8, 11.3, 10.7, 10.2, 9.6, 9.1, 8.5, 8.0, 7.4, 6.9]

		Interest_Rate = []

		for i in range(21) :
			P = []
			for j in range(21) :
				P.append(Val[i + j])
			Interest_Rate.append(P)

		Discounts = [0.10, 0.10, 0.25]
		Original_Fees = [4.99, 3.99, 2.99, -1.00, -1.00, -2.00]
		cre = int(fico_model_used)
		dit = float(debt_to_income)
		if (cre < 600 or dit > 0.50) :
			decision = "Rejected"
			interest_rate = 0.0
			original_fee = 0.0
			self.decision = decision
			self.save()
			return 
		if (cre > 800) :
			cre = 800
		else :
			for i in range(21) :
				if (Credit_Score[i] > cre) :
					cre = Credit_Score[i - 1]
					break 
		
		
		if (dit < 0.30) :
			dit = 0.30
		
		r = 0
		c = 0
		for i in range(21) :
			if (Credit_Score[i] == cre) :
				r = i
				break 
		
		for i in range(21) :
			if (DTI[i] <= dit) :
				c = i
				break 
		
		
		decision = "Approved"
		interest_rate = Interest_Rate[r][c] / 100.0
		interest_rate_MA = interest_rate * (1 - Discounts[0])
		interest_rate_DD = interest_rate * (1 - Discounts[1])
		interest_rate_MA_DD = interest_rate * (1 - Discounts[2])
		if (cre < 700) :
			original_fee = Original_Fees[0]
		elif (cre < 750) :
			original_fee = Original_Fees[1]
		else :
			original_fee = Original_Fees[2]

		if (MilitaryAlloment == True and DirectDeposit == True) :
			finalRate = interest_rate_MA_DD
			original_fee += Original_Fees[5]
		elif (MilitaryAlloment == False and DirectDeposit == True) :
			finalRate = interest_rate_DD
			original_fee += Original_Fees[4]
		elif (MilitaryAlloment == True and DirectDeposit == False) :
			finalRate = interest_rate_MA
			original_fee += Original_Fees[3]
		else :
			finalRate = interest_rate
			original_fee = original_fee

		self.interestRate = str(finalRate)
		self.interestRatePercent = str(finalRate * 100)
		self.originationFee = str(original_fee * 0.01 * float(self.LoanAmount))
		#self.decision = decision
		self.save()
		                #Calculate amortization payment
                monthlyInterest = float(self.interestRate) / 12.0
                tmp = pow(1+monthlyInterest, int(self.term))
                monthlyPmt = float(self.LoanAmount) * monthlyInterest * tmp / (tmp - 1)
		self.monthlyPayment = str(monthlyPmt)
		self.save()

	def get_fields(self):
    		return [(field.name, field.value_to_string(self)) for field in TFSBLoanApp._meta.fields]

	def allfields_as_list(self):
        	return self.allFields.split('  ')

class MidLoanStart(models.Model):
	allFields = models.CharField(default='',max_length=50024)
        streetAddress = models.CharField(default='',max_length = 500)
        city = models.CharField(default='',max_length = 80)
        state = models.CharField(default='',max_length = 2)
        zipCode = models.CharField(default='',max_length = 5)


class EClickLoanApp(models.Model):
        allFields = models.CharField(default='',max_length=50024)
	streetAddress = models.CharField(default='',max_length = 500)
	city = models.CharField(default='',max_length = 80)
	state = models.CharField(default='',max_length = 2)
	zipCode = models.CharField(default='',max_length = 5)
        ltv = models.CharField(default='',max_length=100)
        dti = models.CharField(default='',max_length=100)
        address = models.CharField(default='',max_length=100)
        name = models.CharField(default='',max_length=100)
        apr = models.CharField(default='',max_length=100)
        piti = models.CharField(default='',max_length=100)
        loan_amount = models.CharField(default='',max_length=100)
        fico_score = models.CharField(default='',max_length=100)
        reserveratio = models.CharField(default='',max_length=100)
        creditreportid = models.CharField(default='',max_length=100)
        decision = models.CharField(default='',max_length=100)
        totalMonthlyObligations = models.CharField(default='',max_length=100)
        totalMonthlyIncome = models.CharField(default='',max_length=100)
	timeStamp = models.DateTimeField(default=datetime.now())
	
	def allfields_as_list(self):
        	return self.allFields.split('  ')

class LeadReferral(models.Model):
	inputName = models.CharField(max_length=512)
	inputName1 = models.CharField(max_length=512)
	inputCompany = models.CharField(max_length=1024)
	inputPhone = models.CharField(max_length=1024)
	inputEmail = models.CharField(max_length=1024)
	inputMessage = models.CharField(max_length=1024)
	inputMessage1 = models.CharField(max_length=1024)
class BankInformation(models.Model):
	username = models.CharField(max_length=512)
	account_type = models.CharField(max_length=512)
	access_token = models.CharField(max_length=1024)
class Message(models.Model):
	sender = models.ForeignKey(User, related_name='message_senders')
	receiver = models.ForeignKey(User, related_name='message_receivers')
	subject = models.CharField(max_length=100)
	date = models.DateField(default=date.today())
	body = models.CharField(max_length=512)
	read = models.BooleanField(default=False)

class Person(models.Model):
	firstname = models.CharField(max_length = 30)
	lastname = models.CharField(max_length = 30)
	streetAddress = models.CharField(default='',max_length = 500)
	city = models.CharField(default='',max_length = 80)
	state = models.CharField(default='',max_length = 2)
	zipCode = models.CharField(default='',max_length = 5)
	month = models.CharField(default='',max_length = 2)
	day = models.CharField(default='',max_length = 2)
	year = models.CharField(default='',max_length = 4)

class Neighborhoods(models.Model):
    state = models.CharField(max_length=600, db_column='State', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=600, db_column='CountyName', blank=True) # Field name made lowercase.
    regionname = models.CharField(max_length=600, db_column='RegionName', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=600, db_column='City', blank=True) # Field name made lowercase.
    metro = models.CharField(max_length=600, db_column='Metro', blank=True) # Field name made lowercase.
    rent = models.CharField(max_length=600, db_column='Rent', blank=True) # Field name made lowercase.
    mediansales = models.CharField(max_length=600, db_column='MedianSales', blank=True) # Field name made lowercase.
    unemployed = models.CharField(max_length=200)
    workforce = models.CharField(max_length=200)
    employed = models.CharField(max_length=200)
    unemploymentrate = models.CharField(max_length=200)
    fipsstate = models.CharField(max_length=200)
    state_sales = models.CharField(max_length=200)
    fipscounty = models.CharField(max_length=200)

    class Meta:
        db_table = 'home_neighborhooddata5'


class Residence(models.Model):
        streetAddress = models.CharField(max_length = 500)
	underwriter_id = models.IntegerField(max_length = 10)	
	active = models.BooleanField(default=True)	
        city = models.CharField(max_length = 80)
        state = models.CharField(max_length = 20)
        zipCode = models.CharField(max_length = 5)
        neighborhood = models.ForeignKey(Neighborhoods)
        person = models.ForeignKey(Person, null=True)
        crimeScore = models.CharField(max_length = 1000)
        larcch = models.CharField(max_length = 1000)
        propch = models.CharField(max_length = 1000)
        robch = models.CharField(max_length = 1000)
        burgch = models.CharField(max_length = 1000)
        larcpt = models.CharField(max_length = 1000)
        proppt = models.CharField(max_length = 1000)
        robpt = models.CharField(max_length = 1000)
        burgpt = models.CharField(max_length = 1000)
        larcenycrimeScore = models.CharField(max_length = 1000)
        burglarycrimeScore = models.CharField(max_length = 1000)
        robberycrimeScore = models.CharField(max_length = 1000)
        propertycrimeScore = models.CharField(max_length = 1000)
        violentcrimeScore = models.CharField(max_length = 1000)
        std = models.CharField(max_length = 1000)
        median = models.CharField(max_length = 1000)
        count = models.CharField(max_length = 1000)
        walkScore = models.CharField(max_length = 1000)
        lastSoldDate = models.CharField(max_length = 1000)
        schoolScore = models.CharField(max_length = 1000, default=' ')
        economicData = models.CharField(max_length = 1000)
        pcpop = models.CharField(max_length = 1000)
        pop = models.CharField(max_length = 1000)
        pi = models.CharField(max_length = 1000)
        pcpi = models.CharField(max_length = 1000)
        comps = models.CharField(max_length = 1000)
        actualcomps = models.CharField(max_length = 1000)
        crimereport = models.CharField(max_length = 1000)

        def schoolScore_as_list(self):
            return self.schoolScore.split('@@')
        def comps_as_list(self):
            return self.actualcomps.split('@@')
        def crimereport_as_list(self):
            return self.crimereport.split('was recorded.')




class FilterProperty(models.Model):
        active = models.BooleanField(default=False)
        includeGrades = models.CharField(max_length=7, null=True)
        excludeGrades = models.CharField(max_length=7, null=True)
        portfolioMin = models.FloatField(default=0)
        portfolioMax = models.FloatField(default=100.0)
        minGrowth = models.FloatField(default=0)
        maxGrowth = models.FloatField(default=100.0)
        minoccupancy = models.FloatField(default=0)
        maxoccupancy = models.FloatField(default=100.0)
        mincaprate = models.FloatField(default=0)
        maxcaprate= models.FloatField(default=100.0)
        minrentgrowth = models.FloatField(default=0)
        maxrentgrowth = models.FloatField(default=100.0)
        def clear(self):
                self.active = False
                self.excludePublicRecords = False
                self.excludeDelinquencies = False
                self.excludePartiallyFunded = False
                self.includeGrades = ''
                self.excludeGrades = ''
                self.portfolioMin = 0
                self.portfolioMax = 100.0
		self.minGrowth = 0
		self.maxGrowth = 100.0
		self.minoccupancy = 0
		self.maxoccupancy  = 100.0
		self.mincaprate = 0
		self.maxcaprate = 100.0
		self.minrentgrowth = 0
		self.maxrentgrowth = 0
                self.save()




class Crestatistics(models.Model):
    one_month = models.CharField(max_length=3000)
    portfoliopct = models.FloatField(default=0.0)
    three_month = models.CharField(max_length=3000)
    six_month = models.CharField(max_length=3000)
    one_year = models.CharField(max_length=3000)
    three_year = models.CharField(max_length=3000)
    ten_year = models.CharField(max_length=3000)
    overall_economy = models.CharField(max_length=3000)
    economic_momentum = models.CharField(max_length=3000)
    longterm_growth = models.CharField(max_length=3000)
    volatility = models.CharField(max_length=3000)
    economic_diversification = models.CharField(max_length=3000)
    office_sector = models.CharField(max_length=3000)
    apartment_sector = models.CharField(max_length=3000)
    retail_sector = models.CharField(max_length=3000)
    industrials_sector = models.CharField(max_length=3000)
    singlefamily_sector = models.CharField(max_length=3000)
    hospitality_sector = models.CharField(max_length=3000)
    region = models.CharField(max_length=3000)
    completion12 = models.CharField(max_length=3000)
    completion13 = models.CharField(max_length=3000)
    completion14 = models.CharField(max_length=3000)
    completion15 = models.CharField(max_length=3000)
    absorption12 = models.CharField(max_length=3000)
    absorption13 = models.CharField(max_length=3000)
    absorption14 = models.CharField(max_length=3000)
    absorption15 = models.CharField(max_length=3000)
    occupancy12 = models.CharField(max_length=3000)
    occupancy13 = models.CharField(max_length=3000)
    occupancy14 = models.CharField(max_length=3000)
    occupancy15 = models.CharField(max_length=3000)
    rent_level12 = models.CharField(max_length=3000)
    rent_level13 = models.CharField(max_length=3000)
    rent_level14 = models.CharField(max_length=3000)
    rent_level15 = models.CharField(max_length=3000)
    rent_growth12 = models.CharField(max_length=3000)
    rent_growth13 = models.CharField(max_length=3000)
    rent_growth14 = models.CharField(max_length=3000)
    rent_growth15 = models.CharField(max_length=3000)
    valuation_index12 = models.CharField(max_length=3000)
    valuation_index13 = models.CharField(max_length=3000)
    valuation_index14 = models.CharField(max_length=3000)
    valuation_index15 = models.CharField(max_length=3000)
    cap_rate12 = models.CharField(max_length=3000)
    cap_rate13 = models.CharField(max_length=3000)
    cap_rate14 = models.CharField(max_length=3000)
    cap_rate15 = models.CharField(max_length=3000)
    cap_rate_spread12 = models.CharField(max_length=3000)
    cap_rate_spread13 = models.CharField(max_length=3000)
    cap_rate_spread14 = models.CharField(max_length=3000)
    cap_rate_spread15 = models.CharField(max_length=3000)
    class Meta:
        db_table = u'crestatistics'

    def property_new_list(self):
	news = self.propertydesc_set.all().filter(active=True)
	return news
    def portfoliopct_percent(self):
	try:
	    return '{:.2%}'.format(float(self.portfoliopct))
	except:
	    return self.portfoliopct

    def one_month_percent(self):
	try:
	    return '{:.2%}'.format(float(self.one_month))
	except:
	    return self.one_month

    def six_month_percent(self): 
	try:
	    return '{:.2%}'.format(float(self.six_month))
	except:
	    return self.six_month
    def one_year_percent(self):
	try:
	    return '{:.2%}'.format(float(self.one_year))
	except:
	    return self.one_year

    def ten_year_percent(self):
	try:
	    return '{:.2%}'.format(float(self.ten_year))
	except:
	    return self.ten_year

class PropertyDesc(models.Model):
    currentBalance = models.FloatField(default=0.0)
    active = models.BooleanField(default=True)
    streetAddress = models.CharField(max_length=3000)
    city = models.CharField(max_length=3000)
    state = models.CharField(max_length=3000)
    zipCode = models.CharField(max_length=3000)
    owner = models.CharField(max_length=3000)
    property_type = models.CharField(max_length=3000)
    receiver = models.ForeignKey(Crestatistics)
    walkScore = models.CharField(max_length=3000)
    crimeScore = models.CharField(max_length=3000)
    reportLink = models.CharField(max_length=3000)
    def tenants_as_list(self):
	return self.tenantdesc_set.all().order_by('-sf_occupied')	

class TenantDesc(models.Model): 
    name = models.CharField(default='', max_length=3000)
    rent_price_sqft = models.CharField(default='', max_length=3000)
    sf_occupied = models.FloatField(default=0)
    industry = models.CharField(default='', max_length=3000)
    lease_exp_date = models.CharField(default='', max_length=3000)
    lease_beg_date = models.CharField(default='', max_length=3000)
    streetAddress = models.CharField(default='', max_length=3000)
    city = models.CharField(default='', max_length=3000)
    state = models.CharField(default='', max_length=3000)
    zipCode = models.CharField(default='', max_length=3000)
    employees = models.CharField(default='', max_length=3000)
    total_employees = models.CharField(default='', max_length=3000)
    move_in_date = models.CharField(default='', max_length=3000)
    property_desc = models.ForeignKey(PropertyDesc, null=True, blank=True)

class TradeLine(models.Model):
    name = models.CharField(default='', max_length=3000)
    tradeType = models.CharField(default='', max_length=3000)
    balance = models.CharField(default='0.0', max_length=3000)
    minPayment = models.CharField(default='0.0', max_length=3000)
    loanapp = models.ForeignKey(TFSBLoanApp)
 

    
class Newmasterstats(models.Model):
    one_month = models.CharField(max_length=3000, blank=True)
    three_month = models.CharField(max_length=3000, blank=True)
    six_month = models.CharField(max_length=3000, blank=True)
    one_year = models.CharField(max_length=3000, blank=True)
    three_year = models.CharField(max_length=3000, blank=True)
    ten_year = models.CharField(max_length=3000, blank=True)
    overall_economy = models.CharField(max_length=3000, blank=True)
    economic_momentum = models.CharField(max_length=3000, blank=True)
    longterm_growth = models.CharField(max_length=3000, blank=True)
    volatility = models.CharField(max_length=3000, blank=True)
    economic_diversification = models.CharField(max_length=3000, blank=True)
    office_sector = models.CharField(max_length=3000, blank=True)
    apartment_sector = models.CharField(max_length=3000, blank=True)
    retail_sector = models.CharField(max_length=3000, blank=True)
    industrials_sector = models.CharField(max_length=3000, blank=True)
    singlefamily_sector = models.CharField(max_length=3000, blank=True)
    hospitality_sector = models.CharField(max_length=3000, blank=True)
    region = models.CharField(max_length=3000, blank=True)
    completion12 = models.CharField(max_length=3000, blank=True)
    completion13 = models.CharField(max_length=3000, blank=True)
    completion14 = models.CharField(max_length=3000, blank=True)
    completion15 = models.CharField(max_length=3000, blank=True)
    absorption12 = models.CharField(max_length=3000, blank=True)
    absorption13 = models.CharField(max_length=3000, blank=True)
    absorption14 = models.CharField(max_length=3000, blank=True)
    absorption15 = models.CharField(max_length=3000, blank=True)
    occupancy12 = models.CharField(max_length=3000, blank=True)
    occupancy13 = models.CharField(max_length=3000, blank=True)
    occupancy14 = models.CharField(max_length=3000, blank=True)
    occupancy15 = models.CharField(max_length=3000, blank=True)
    rent_level12 = models.CharField(max_length=3000, blank=True)
    rent_level13 = models.CharField(max_length=3000, blank=True)
    rent_level14 = models.CharField(max_length=3000, blank=True)
    rent_level15 = models.CharField(max_length=3000, blank=True)
    rent_growth12 = models.CharField(max_length=3000, blank=True)
    rent_growth13 = models.CharField(max_length=3000, blank=True)
    rent_growth14 = models.CharField(max_length=3000, blank=True)
    rent_growth15 = models.CharField(max_length=3000, blank=True)
    valuation_index12 = models.CharField(max_length=3000, blank=True)
    valuation_index13 = models.CharField(max_length=3000, blank=True)
    valuation_index14 = models.CharField(max_length=3000, blank=True)
    valuation_index15 = models.CharField(max_length=3000, blank=True)
    cap_rate12 = models.CharField(max_length=3000, blank=True)
    cap_rate13 = models.CharField(max_length=3000, blank=True)
    cap_rate14 = models.CharField(max_length=3000, blank=True)
    cap_rate15 = models.CharField(max_length=3000, blank=True)
    cap_rate_spread12 = models.CharField(max_length=3000, blank=True)
    cap_rate_spread13 = models.CharField(max_length=3000, blank=True)
    cap_rate_spread14 = models.CharField(max_length=3000, blank=True)
    cap_rate_spread15 = models.CharField(max_length=3000, blank=True)
    state = models.CharField(max_length=600, db_column='State', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=600, db_column='CountyName', blank=True) # Field name made lowercase.
    regionname = models.CharField(max_length=600, db_column='RegionName', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=600, db_column='City', blank=True) # Field name made lowercase.
    metro = models.CharField(max_length=600, db_column='Metro', blank=True) # Field name made lowercase.
    rent = models.CharField(max_length=600, db_column='Rent', blank=True) # Field name made lowercase.
    mediansales = models.CharField(max_length=600, db_column='MedianSales', blank=True) # Field name made lowercase.
    workforce = models.CharField(max_length=600, blank=True)
    employed = models.CharField(max_length=600, blank=True)
    unemployed = models.CharField(max_length=600, blank=True)
    unemploymentrate = models.CharField(max_length=600, blank=True)
    fipsstate = models.CharField(max_length=600, blank=True)
    fipscounty = models.CharField(max_length=600, blank=True)
    state_sales = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'newmasterstats2'

class Profile(models.Model):
	user = models.OneToOneField(User)
	firstLogin = models.BooleanField(default=True)
	firstName = models.CharField(max_length = 30)
	lastName = models.CharField(max_length = 30)
	lastLogin = models.DateTimeField(default=datetime.now())
	failedLoginCount = models.IntegerField(default=0)
	streetAddress = models.CharField(max_length = 500)
	city = models.CharField(max_length = 80)
	state = models.CharField(max_length = 2)
	zipCode = models.CharField(max_length = 5)
	month = models.CharField(max_length = 2)
	day = models.CharField(max_length = 2)
	year = models.CharField(max_length = 4)
	passwordResetKey = models.CharField(max_length = 25)
	resetExpiration = models.DateTimeField(null=True)
	cim_profile_id = models.IntegerField(default=0000)
	cim_payment_profile = models.IntegerField(default=0000)
	invalid_cim_count = models.IntegerField(default=0)
	locked = models.BooleanField(default=False)
	registered = models.BooleanField(default=False)
        social_security=models.IntegerField(max_length = 9)
	phone = models.IntegerField(max_length = 10)	
	def __str__(self):
			return str(self.user)

	def principalAccount(self):
		return self.user.account_set.all()[0]

	def isLender(self):
		a = self.user.account_set.all()[0]
		return a.isLender

	def creditProfile(self):
		try:
			cp = CreditProfile.objects.get(account=self.principalAccount)
		except CreditProfile.DoesNotExist:
			return None
		return cp

	def sbcreditProfile(self):
                try:
                        cp = SBCreditProfile.objects.get(account=self.principalAccount)
                except SBCreditProfile.DoesNotExist:
                        return None
                return cp		
	def lenderProfile(self):
		a = self.user.account_set.all()[0]
		try:
			lend = Lender.objects.get(account=a)
		except Lender.DoesNotExist:
			lend = Lender(account=a)
			lend.save()
		return lend
	
	def invalid_cim_attempt(self, message):
		if self.invalid_cim_count == 4:
			self.locked = True
			#message = message + '\n' + 'Your account has been locked due to repeated attempts to enter an invalid credit card number. To unlock your account, email help@daric.com with a description of what you were doing.'
		else:
			self.invalid_cim_count += 1
			message = message + '\n' + 'You have ' + str(5 - self.invalid_cim_count) + ' attempts remaining until your account is locked. If you are sure your information is correct, please email help@daric.com.'
		self.save()
		return message
	
	def numUnreadMessages(self):
		return Message.objects.filter(receiver=self.user, read=False).count()
	
