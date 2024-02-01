from django.http import JsonResponse
import json
def api_home(request, *args, **kwargs):
    #this request is HttpRequest from Django
    # print(dir(request))
    print(request.GET)
    body = request.body #byte string of JSON data
    # now convert tht data from byte string to json
    data = {}
    try:
        data = json.loads(body) # takes string of json data and turns into Python Dictionary
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
