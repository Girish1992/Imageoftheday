from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView 
from models import ImageOfTheDay
import json, datetime
from django.shortcuts import render


# Create your views here.
developer_team = {"9404505206" : {"first_name": "Nikhil", "last_name": "Rane", "mobile_no": 9404505206, "email": "nikhilrane1992@gmail.com", "designation": "Software Developer and Trainer", "company_name": "Sahaj Academy Edutech LLP"}}


def image_of_the_day(request):
	image=ImageOfTheDay.objects.all()
	imageList=[]
	for i in image:
		date=int(i.date.strftime("%s")) * 1000
		obj={"imageUrl": 'Media/'+str(i.image),"date": date,"title": i.title,"subTitle": i.subtitle,"description": i.decription}
		imageList.append(obj)
		
	return HttpResponse(json.dumps({"imageList": imageList}), content_type="application/json")

def upload_image_data(request):
	print  request.POST
	
	if request.POST:
		iName=request.FILES['imageName']
		iDate=request.POST['date']
		date_object = datetime.datetime.strptime(iDate,'%m/%d/%Y')
		iTitle=request.POST['title']
		sTitle=request.POST['subTitle']
		dec=request.POST['desc'] 
		eve=ImageOfTheDay(image=iName,date=date_object,title=iTitle,subtitle=sTitle,decription=dec)
		eve.save()
		return render_to_response('imageoftheday.html')
	else:
		return render_to_response('imageoftheday.html')

def get_request(request):
	obj = {"first_name": "Nikhil", "last_name": "Rane", "mobile_no": 9404505206, "email": "nikhilrane1992@gmail.com", "designation": "Software Developer and Trainer", "company_name": "Sahaj Academy Edutech LLP"}
	return HttpResponse(json.dumps({"obj": obj,  "status": True}), content_type="application/json")

def post_request(request):
	data_dictonary = json.loads(request.body)
	mobile_no = data_dictonary['mobile_no']
	try:
		obj = developer_team[str(mobile_no)]
	except Exception, e:
		print e
		return HttpResponse(json.dumps({"validation": "Entry not found..!!", "status": False}), content_type="application/json")
	return HttpResponse(json.dumps({"obj": obj, "status": True}), content_type="application/json")