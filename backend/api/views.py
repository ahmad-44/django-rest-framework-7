from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "This is your django API response"})
