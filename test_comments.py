import requests
import test_data
#import hashlib

POST_ID = 13
COMMENTS_TEST_URL = f"https://jsonplaceholder.typicode.com/comments?postId={POST_ID}"
#EXPECTED_POST_CONTENT_MD5 = '387bef30ec1e9123759e663ca5e0ae86'
COMMENT_ELEMENTS = ['postId', 'id', 'name', 'email', 'body']
COMMENT_ELEMENTS_NOT_EMPTY = ['postId', 'id', 'email', 'body']

EXPECTED_COMMENTS_LEN = 5

class TestComments:

    @classmethod
    def setup_class(cls):
        resp = requests.get(COMMENTS_TEST_URL)
        cls.resp = resp
        cls.resp_json = resp.json()

    def test_response_ok(self):
        assert self.resp

    def test_response_is_json(self):
        assert self.resp_json

    def test_comments_len(self):
        assert len(self.resp_json) == EXPECTED_COMMENTS_LEN

    def test_comments_structure(self):
        """If the number of comments is much higher than 5 in test response it would be better to
        check selected few of them or even only one """
        for comment in self.resp_json:
            assert type(comment) == dict

    def test_comments_contain_proper_fields(self):
        for comment in self.resp_json:
            for comment_element in COMMENT_ELEMENTS:
                assert comment_element in comment

    def test_comment_fields_not_empty(self):
        for comment in self.resp_json:
            for comment_element in COMMENT_ELEMENTS_NOT_EMPTY:
                assert comment[comment_element]

    def test_correct_post_id(self):
        for comment in self.resp_json:
            assert comment['postId'] == POST_ID

    def test_incrementing_ids(self):
        first_comment_id = self.resp_json[0]['id']
        for enum, comment in enumerate(self.resp_json, 0):
            assert comment['id'] == first_comment_id + enum

    # Comparisons with expected response

    """"It's possible to check only the md5 of expected response, it is useful in cases where we can't hold 
        whole expected response as test data due to its size, its downside is that we won't get useful print 
        output in test running console"""

    # def test_response_md5(self):
    #     assert hashlib.md5(self.resp.text.encode('utf-8')).hexdigest() == EXPECTED_POST_CONTENT_MD5

    def test_response_text(self):
        assert test_data.POST_COMMENTS_EXP_RESPONSE_TEXT == self.resp.text

