import json
from dataclasses import dataclass

""" A file which could hold all the dataclasses and expected responses for other tests 
currently expected responses is utilized only by comments tests but it could be extended for every other class"""

@dataclass()
class PostStr:
    userId: int = None
    title: str = None
    body: str = None


POST_FIELDS_SET = PostStr(1, 'abc', 'def')


POST_COMMENTS_EXP_RESPONSE_TEXT =r'''[
  {
    "postId": 13,
    "id": 61,
    "name": "quidem itaque dolores quod laborum aliquid molestiae",
    "email": "Aurelio.Pfeffer@griffin.ca",
    "body": "deserunt cumque laudantium\net et odit quia sint quia quidem\nquibusdam debitis fuga in tempora deleniti\nimpedit consequatur veniam reiciendis autem porro minima"
  },
  {
    "postId": 13,
    "id": 62,
    "name": "libero beatae consequuntur optio est hic",
    "email": "Vesta_Crooks@dora.us",
    "body": "tempore dolorum corrupti facilis\npraesentium sunt iste recusandae\nunde quisquam similique\nalias consequuntur voluptates velit"
  },
  {
    "postId": 13,
    "id": 63,
    "name": "occaecati dolor accusantium et quasi architecto aut eveniet fugiat",
    "email": "Margarett_Klein@mike.biz",
    "body": "aut eligendi et molestiae voluptatum tempora\nofficia nihil sit voluptatem aut deleniti\nquaerat consequatur eaque\nsapiente tempore commodi tenetur rerum qui quo"
  },
  {
    "postId": 13,
    "id": 64,
    "name": "consequatur aut ullam voluptas dolorum voluptatum sequi et",
    "email": "Freida@brandt.tv",
    "body": "sed illum quis\nut aut culpa labore aspernatur illo\ndolorem quia vitae ut aut quo repellendus est omnis\nesse at est debitis"
  },
  {
    "postId": 13,
    "id": 65,
    "name": "earum ea ratione numquam",
    "email": "Mollie@agustina.name",
    "body": "qui debitis vitae ratione\ntempora impedit aperiam porro molestiae placeat vero laboriosam recusandae\npraesentium consequatur facere et itaque quidem eveniet\nmagnam natus distinctio sapiente"
  }
]'''


POST_COMMENTS_EXP_RESPONSE_JSON = json.loads(POST_COMMENTS_EXP_RESPONSE_TEXT)
