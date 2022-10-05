from django.shortcuts import render

#Can find out whether request was get or post. We can find shortcuts
#Various pieces of info in the request.
#This view is responsible for generating a response to the request.
def thingsPage(request):
    return render(request, 'things.html')
