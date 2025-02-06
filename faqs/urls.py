from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet
from .views import faq_view


router = DefaultRouter()
router.register(r"faqs", FAQViewSet, basename="faq")

urlpatterns = [
    path("api/", include(router.urls)),
    path("", faq_view, name="faq_view"),
]  # Rooted at 'api/faqs/'
