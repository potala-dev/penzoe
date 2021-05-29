from rest_framework import views
from rest_framework.response import Response

from ..utils import get_sentence_with_correct_spelling_choices
from .serializers import FBSerializer


class SpellFBMCQView(views.APIView):
    """
    API endpoint for Spelling Fill-in-the-Blank mcq.
    """

    def get(self, request):
        (
            lelft_context,
            right_context,
            choices,
            correct_choice,
        ) = get_sentence_with_correct_spelling_choices(request.GET.get("level", "C1"))

        data = {
            "left_context": lelft_context,
            "right_context": right_context,
            "choices": choices,
            "correct_choice": correct_choice,
        }
        result = FBSerializer(data).data
        return Response(result)
