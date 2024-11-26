from django.http import HttpResponse



class mixinddata(object):
    def jsondata(self,json_data):
        return HttpResponse(json_data,content_type='application/json')