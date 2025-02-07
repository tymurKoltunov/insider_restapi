from constants.author_enums import Authors, AuthorsPoemCount
from controllers.poem_controller import PoemController


class TestAuthorsPoemCount:
    def test_authors_poem_count(self):
        author_to_check = Authors.WShakespeare.value
        number_of_poems_to_check = AuthorsPoemCount.WShakespeare.value
        poems = PoemController.get_titles_of(author_to_check)
        actual_poem_number = len(poems)
        assert actual_poem_number == number_of_poems_to_check, \
            f"{author_to_check} has more poems. Actual = {actual_poem_number}. Expected = {number_of_poems_to_check}"
