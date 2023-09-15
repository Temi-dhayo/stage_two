from django.urls import path
from stagetwo.views import PersonCreateView,PersonDetailsView

app_name = 'stagetwo'

urlpatterns = [
    path('',PersonCreateView.as_view(),name='person-create'),
    path('<str:id>/',PersonDetailsView.as_view(),name='person-detail'),
]
