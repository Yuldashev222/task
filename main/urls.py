from django.urls import path, include
from .views import RegisterApi, WashCompanyCreateApi, GetCompany, JournalAPIView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register(r'journal', JournalAPIView)

urlpatterns = [
      path('', include(router.urls)),
      path('api/signUp/', RegisterApi.as_view()),
      path('api/washCompanyInsert/', WashCompanyCreateApi.as_view()),
      path('api/getWashCompanyId/', GetCompany.as_view()),
]