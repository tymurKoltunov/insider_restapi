
from controllers.poem_controller import PoemController


class TestRandomRequest:
    def test_random_request(self):
        poem = PoemController.get_random_poem().root[0]
        PoemController.remove_empty_lines(poem)
        actual_poem_lines = len(poem.lines)
        server_response_poem_lines = int(poem.linecount)
        assert len(poem.lines) == int(poem.linecount), \
            f"Lines in the response do not match actual lines. Actual = {actual_poem_lines}. Expected = {server_response_poem_lines}"
