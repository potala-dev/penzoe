import random

import requests
from bomisspell import get_misspelled_word

sentences_url = (
    "https://raw.githubusercontent.com/potala-dev/object-storage/main/sentences"
)


def get_content(url: str) -> str:
    r = requests.get(url)
    return r.text


def get_last_id(level_url: str) -> int:
    last_id_url = level_url + "/last_id"
    last_id = get_content(last_id_url)
    return int(last_id)


def parse_sentence_content(content: str) -> tuple:
    sentence, word_idxs_raw = content.splitlines()
    words = sentence.split()
    word_idxs = word_idxs_raw.split(",")[:-1]
    candidate_word_idx = int(random.choice(word_idxs))
    left_context = "".join(words[:candidate_word_idx])
    right_context = "".join(words[candidate_word_idx + 1 :])
    return left_context, words[candidate_word_idx], right_context


def get_choices(word):
    choices = get_misspelled_word(word)
    incorrect_choices = random.choices(choices[1:], k=3)
    choices = incorrect_choices + [word]
    random.shuffle(choices)
    return choices


def get_sentence_with_correct_spelling_choices(level: str):
    level_url = sentences_url + f"/{level}"
    last_id = get_last_id(level_url)
    sentence_id = random.randint(1, last_id)
    sentence_url = level_url + f"/{sentence_id}.txt"
    sentence_content = get_content(sentence_url)
    l_context, word, r_context = parse_sentence_content(sentence_content)
    choices = get_choices(word)
    return l_context, r_context, choices, word


if __name__ == "__main__":
    output = get_sentence_with_correct_spelling_choices("C1")
    print(output)
