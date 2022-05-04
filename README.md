# Prepaid-Recharge-System
Prepaid Recharge System

Requirements :-
Must have to install rest_framework with django.

POST  http://127.0.0.1:8000/api/user-signup/  responsible for signup with name,email,mobile and password with post method.
POST  http://127.0.0.1:8001/api/user-signin/  responsible for signin with email and password and return a valid token with post method.
GET   http://127.0.0.1:8000/api/plans/        responsible for get the all available palns with get method with a valid token because this is protected endpoint.
POST  http://127.0.0.1:8000/api/recharge/     responsible for recharge as your given mobile number,valid operator, valid area/circle, valid user and with a valid plan.


Where user -> your registerd email id.

mobile -> valid 10 digit of mobile no.

valid operator -> Tata Docomo, BSNL MOBILE, Reliance Jio, VI, Airtel same as it is formate.

valid area/circle -> 
  	West Bengal & Andaman Nicobar
	UP West & Uttaranchal
	UP East
	Tamilnadu
	Rajasthan
	Punjab
	Odisha
	North East
	Maharashtra & Goa
	Madhya Pradesh & Chhattisgarh
	Kolkata
	Kerala
	write circle name same as it is formate,
 	and others mention in model.
  
  
valid plan ->
  	499,
	3359,
	1799,
	839,
	838,
	719,
	699,
	666,
	599,
	549,
	455,
	449,
	359,
	209,
	256,
	479,
	299,
	155,
	179,
	99,
	239
  
plans are indicate what is the price of your paln.

Thanks................
