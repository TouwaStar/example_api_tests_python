import requests

POST_ID = 1
POST_REMOVE_URL = f"https://jsonplaceholder.typicode.com/posts/{POST_ID}"
NON_EXISTENT_POST_ID = 0
POST_REMOVE_URL_NON_EXISTENT_ID = f"https://jsonplaceholder.typicode.com/posts/{NON_EXISTENT_POST_ID}"


class TestPostUpdating:

    def test_remove_post_non_existent(self):
        resp = requests.get(POST_REMOVE_URL_NON_EXISTENT_ID)
        # Assert post doesnt exist
        assert resp.status_code != 200

        resp = requests.delete(POST_REMOVE_URL_NON_EXISTENT_ID)
        assert resp.status_code != 200

    def test_remove_post(self):
        # TODO: Post to remove should be recreated every test, consider merging with post_adding tests
        #  (could possibly create an overly inflated test class etc.)
        resp = requests.get(POST_REMOVE_URL)
        # Assert post to delete exists
        assert resp.status_code == 200

        resp = requests.delete(POST_REMOVE_URL)
        assert resp.status_code == 200
        resp = requests.get(POST_REMOVE_URL)

        # Assert post was deleted
        assert resp.status_code != 200
