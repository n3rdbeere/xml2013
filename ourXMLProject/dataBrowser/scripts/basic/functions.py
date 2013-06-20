from dataBrowser.models.basic.models import *

# wrapper function in order to be able to read some necessary data from request
def getClientRequestData(viewFunction):
    def wrapper(request):
        clientRequest = ClientRequest(request)
        return viewFunction(clientRequest)
    return wrapper
