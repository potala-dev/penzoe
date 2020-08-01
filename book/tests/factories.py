import factory


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "book.Book"

    user = factory.SubFactory("users.tests.factories.UserFactory")
