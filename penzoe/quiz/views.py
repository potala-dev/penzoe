from django.shortcuts import render

from .utils import get_sentence_with_correct_spelling_choices


def get_spelling_mcq(request, level):
    lelft_context, right_context, choices = get_sentence_with_correct_spelling_choices(
        level
    )

    context_data = {
        "left_context": lelft_context,
        "right_context": right_context,
        "choices": choices,
    }

    return render(request, "quiz/mcq.html", context_data)
