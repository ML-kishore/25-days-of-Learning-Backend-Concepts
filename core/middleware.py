from django.http import HttpResponse
from rest_framework import status



class AuthMiddleware:
    def __init__(self, get_response):
        print("Authentication Middleware gateway ........ ✅")
        self.get_response = get_response

    def __call__(self, request):
        print("Auth middleware triggered......")

        if request.path == "/login/":
            print("Now its login time........ voh vhoh 200 status code....")
            return self.get_response(request)

        if not request.user.is_authenticated:
            print("Middleware is Blocked ❌❌")
            return HttpResponse("<h3>Unauthorized. . . . </h3>",status=403)
        
        

        print("Auth passed...... ✅✅✅✅☝🏻☝🏻")
        response = self.get_response(request)
        return response
    

class MyMiddleware:
    def __init__(self,get_response):
        print("Middleware Gateway opened 🏰🏰 .... . . . . ✅")
        self.get_response = get_response


    def __call__(self, request):
        print("Heading to view .... ")

        #you can modify the request using middleware

        request.custom_data = "Added by Middleware......➕ ➕"

        #calling the middleare

        response = self.get_response(request)

        print("After view......")

        #modify the response

        response["X-Demo"] = "Header modfied"

        return response
    



