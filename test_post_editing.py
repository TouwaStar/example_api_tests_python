import requests
import test_data
import dataclasses

POST_ID = 1
POST_UPDATE_URL = f"https://jsonplaceholder.typicode.com/posts/{POST_ID}"
NON_EXISTENT_POST_ID = 0
POST_UPDATE_URL_NON_EXISTENT_ID = f"https://jsonplaceholder.typicode.com/posts/{NON_EXISTENT_POST_ID}"


class TestPostUpdating:

    def assert_non_existent(self):
        resp = requests.get(POST_UPDATE_URL_NON_EXISTENT_ID)
        # Assert post doesnt exist
        assert resp.status_code != 200

    def test_update_post_non_existent_put(self):
        self.assert_non_existent()

        post = test_data.POST_FIELDS_SET
        post = dataclasses.asdict(post)
        post['id'] = NON_EXISTENT_POST_ID
        post['body'] = 'modified'

        resp = requests.put(POST_UPDATE_URL_NON_EXISTENT_ID, json=post)
        assert resp.status_code != 200

    def test_update_post_non_existent_patch(self):
        self.assert_non_existent()

        post = test_data.POST_FIELDS_SET
        post = dataclasses.asdict(post)
        post['body'] = 'modified'

        resp = requests.patch(POST_UPDATE_URL_NON_EXISTENT_ID, json=post)
        assert resp.status_code != 200

    def test_update_post_put(self):
        post = test_data.POST_FIELDS_SET
        post = dataclasses.asdict(post)
        post['id'] = POST_ID
        post['body'] = 'modified'

        resp = requests.put(POST_UPDATE_URL, json=post)
        assert resp.status_code == 200

        modified_post = requests.get(POST_UPDATE_URL)
        modified_post = modified_post.json()
        assert post == modified_post

    def test_update_post_patch(self):
        post = test_data.POST_FIELDS_SET
        post = dataclasses.asdict(post)
        post['body'] = 'modified'

        resp = requests.put(POST_UPDATE_URL, json=post)
        assert resp.status_code == 200

        modified_post = requests.get(POST_UPDATE_URL)
        modified_post = modified_post.json()
        post['id'] = POST_ID
        assert post == modified_post

