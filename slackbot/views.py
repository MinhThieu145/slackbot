from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, World!")

def slacks(request):
    # This is the view that will be called when the Slackbot sends a request to the /slack/ endpoint.
    # print(request.POST)
    print("Response to Slack url", request.body)

    # return the request body as a response
    return HttpResponse("Hello, World!")