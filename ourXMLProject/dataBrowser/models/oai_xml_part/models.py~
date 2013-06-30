class ClientRequest():
	acceptedMimeTypes = None
	browserType = None
	request = None

	def __init__(self, request):
		self.request = request
		self.acceptedMimeTypes = request.META['HTTP_ACCEPT']
		self.browserType = request.META['HTTP_USER_AGENT']
