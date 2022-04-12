from django.urls import path

from .views import *


app_name = 'queries'
urlpatterns = [
    path('', Responder.as_view()),
    path('self/', SelfReferenceView.as_view()),
    path('range/', BeforeAfterItemsView.as_view()),
    path('change-name/', FieldNameChangeView.as_view()),
    path('create/', CreateSelfView.as_view()),
    path('files/', MultipleFilesView.as_view()),
]
