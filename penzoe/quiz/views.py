from django.shortcuts import render


def get_spelling_mcq(request, level):
    return render(request, "quiz/spell_fb_mcq.html", {"level": level})
