from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from deep_translator import GoogleTranslator


class FAQViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        lang = request.query_params.get("lang", "en")
        faqs = FAQ.objects.all()
        data = []

        for faq in faqs:
            if lang != "en":
                try:
                    translated_question = GoogleTranslator(
                        source="auto", target=lang
                    ).translate(faq.question)
                    translated_answer = GoogleTranslator(
                        source="auto", target=lang
                    ).translate(faq.answer)
                except Exception as e:
                    print(f"Translation Error: {e}")
                    translated_question = faq.question
                    translated_answer = faq.answer
            else:
                translated_question = faq.question
                translated_answer = faq.answer

            data.append(
                {
                    "question": translated_question,
                    "answer": translated_answer,
                }
            )

        return Response(data)


def faq_view(request):
    return render(request, "faqs/index.html")
