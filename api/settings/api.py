from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.urls import path

from assessments.views import QuestionnaireViewset, AuthorViewset
from resources.views import LanguageViewset
from disorders.views import DisorderCategoryViewset,DisorderViewset

router = routers.DefaultRouter()
# model endpoint sets
router.register(r'author', AuthorViewset)
router.register(r'questionnaire', QuestionnaireViewset)
router.register(r'language', LanguageViewset)
router.register(r'disorder-category', DisorderCategoryViewset)
router.register(r'disorder-viewset', DisorderViewset)
extra_paths = [
    path('docs/', include_docs_urls(title='MHDB - REST API DOCS'))
]

router_urls = extra_paths + router.urls