from django.http import JsonResponse

# Create your views here.

data = {

   "Name" : "Georgia Adam",

    "Track" : "Backend(Python)",

    "Message" : "Thank you for helping us to learn! I have found the content valuable"

}



def index(request):
    return JsonResponse(data)