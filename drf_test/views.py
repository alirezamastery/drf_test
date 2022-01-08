from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print(f'BAD REQUEST: {context["request"]}')
    if response is not None:
        print(response.__dict__.get('data'))
    return response
