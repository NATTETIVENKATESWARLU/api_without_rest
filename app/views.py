from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse

import json
from django.views.generic import View


# Create your views here.

def emp_data_view(request):
    d={
        "eno":1,
        "ename":"venkat",
        "esal":12000,
        "eaddres":"sullurupeta"
    }
    responce="<h1> employee number  {}<br><br>employee name  {}<br> <br> employee sal  {}<br><br> employee  {}".format(d["eno"],d["ename"],d["esal"],d["eaddres"])

    return HttpResponse(responce)


def emp_data1(request):
    d={
        "eno":1,
        "ename":"venkat",
        "esal":12000,
        "eaddres":"sullurupeta"
    }
    data=json.dumps(d)
    return HttpResponse(data,content_type='application/json')





def emp_data2(request):
    d={
        "eno":1,
        "ename":"venkat",
        "esal":12000,
        "eaddres":"sullurupeta"
    }
    return JsonResponse(d)



class json_cbv(View):
    def get(self,request,*arg,**kwargs):
        d={
        "eno":1,
        "ename":"venkat",
        "esal":12000,
        "eaddres":"mumbai"
        }
        return JsonResponse(d)
    


class json_cbv1(View):
    def get(self,request,*arg,**kwargs):
        d={"massage":"get methode is called"}
        data=json.dumps(d)
        return HttpResponse(data,content_type='application/json')
    
    def post(self,request,*arg,**kwargs):
        d={"massage":"post methode is called"}
        data=json.dumps(d)
        return HttpResponse(data,content_type='application/json')
    
    def put(self,request,*arg,**kwargs):
        d={"massage":"put methode is called"}
        data=json.dumps(d)
        return HttpResponse(data,content_type='application/json')
    
    def delete(self,request,*arg,**kwargs):
        d={"massage":"delete methode is called"}
        data=json.dumps(d)
        return HttpResponse(data,content_type='application/json')
    

from app.mixi import *

class json_cbv2(mixinddata,View):
    def get(self,request,*arg,**kwargs):
        d={"massage":"get methode is called"}
        data=json.dumps(d)
        return self.jsondata(data)
    
    def post(self,request,*arg,**kwargs):
        d={"massage":"post methode is called"}
        data=json.dumps(d)
        return self.jsondata(data)
    
    def put(self,request,*arg,**kwargs):
        d={"massage":"put methode is called"}
        data=json.dumps(d)
        return self.jsondata(data)
    
    def delete(self,request,*arg,**kwargs):
        d={"massage":"delete methode is called"}
        data=json.dumps(d)
        return self.jsondata(data)




