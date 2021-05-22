import factory


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Book"

    user = factory.SubFactory("penzoe.users.tests.factories.UserFactory")
