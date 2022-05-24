class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(f'middleware: {request}')
        # for k,v in request.__dict__.items():
        #     print(f'{k:<20} : {v}')
        # if request.path.startswith('/api'):
        #     print('api*****************')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response