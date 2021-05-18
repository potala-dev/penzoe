import io

from django.conf import settings
from github import Github


def get_bits(file):
    f = io.BytesIO()
    for chunk in file.chunks():
        f.write(chunk)
    return f.getvalue()


def create_file_name(file, title):
    ext = file.name.split(".")[-1]
    return f"{title}.{ext}"


def handle_uploaded_file(file, title):
    ORG = Github(settings.GITHUB_TOKEN).get_organization(settings.GITHUB_ORG)
    file_name = create_file_name(file, title)
    content = get_bits(file)
    repo = ORG.get_repo(settings.GITHUB_BOOK_CATALOG)
    gh_file_obj = repo.create_file(file_name, "added a book", content)
    download_url = gh_file_obj["content"]._download_url.value
    return file_name, download_url
