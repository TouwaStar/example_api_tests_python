import requests
import test_data
import dataclasses

POSTS_TEST_URL = f"https://jsonplaceholder.typicode.com/posts"


class TestPostAdding:

    def get_list(self):
        resp = requests.get(POSTS_TEST_URL)
        assert resp.status_code == 200
        post_list = resp.json()
        return post_list

    def test_post_add_wrong_data(self):
        resp = requests.post(POSTS_TEST_URL, 'abc')
        assert resp.status_code == 400

    def test_post_add_fields_empty(self):
        post = test_data.PostStr()
        resp = requests.post(POSTS_TEST_URL, json=dataclasses.asdict(post))
        assert resp.status_code == 400

    def test_post_add_fields_correct(self):
        post = test_data.POST_FIELDS_SET
        resp = requests.post(POSTS_TEST_URL, json=dataclasses.asdict(post))
        assert resp.status_code == 201

    def test_posts_list_increases(self):
        list_before_post = self.get_list()

        # Create new post
        post = test_data.POST_FIELDS_SET
        resp = requests.post(POSTS_TEST_URL, json=dataclasses.asdict(post))
        assert resp.status_code == 201

        list_after_post = self.get_list()

        # Assert len has increased, and the last post available is the one just posted
        # Don't assume newest id is the len of posts response since posts can be deleted
        assert len(list_before_post) == len(list_after_post) - 1
        newest_post = list_after_post[len(list_after_post)-1]

        expected_post = dataclasses.asdict(post)
        expected_post['id'] = newest_post['id']

        assert newest_post == dataclasses.asdict(post)

    def test_post_added_available(self):
        list_before_post = self.get_list()

        # Create new post
        post = test_data.POST_FIELDS_SET
        resp = requests.post(POSTS_TEST_URL, json=dataclasses.asdict(post))
        assert resp.status_code == 201

        # Assert added post available by id value which should be incremented by one in respect to last one
        expected_id = list_before_post[len(list_before_post)-1]['id'] + 1
        resp = requests.get(f"{POSTS_TEST_URL}/{expected_id}")
        assert resp.status_code == 200
        downloaded_post = resp.json()

        expected_post = dataclasses.asdict(post)
        expected_post['id'] = expected_id
        assert downloaded_post == expected_post

    def test_post_not_in_list_not_available(self):
        post_list = self.get_list()

        last_id_plus_one = post_list[len(post_list)-1]['id'] + 1
        resp = requests.get(f"{POSTS_TEST_URL}/{last_id_plus_one}")
        assert resp.status_code == 404

    # TODO: add utf-8 encoded strings tests,
    #  Unique generated test posts content with incrementing values for better tracking
    #  add whole response comparisons etc.
    #  post is available under GET	/posts?userId= path



