from django.shortcuts import render


def get_spelling_mcq(request, level):
    return render(request, "quiz/mcq.html", {"level": level})
