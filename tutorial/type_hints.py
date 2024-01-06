from datetime import datetime
from pydantic import BaseModel
from typing import Annotated

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(items: list[str]):
    for item in items:
        print(item.capitalize())


print(process_items(["desktop", "laptop"]))


def process_items_tp(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name.upper())
        print(item_price)


print(process_items_dict({"tablet": 99.9, "smartphone": 899.9}))


# Union
def process_item_union(item: int | str):
    print(item)


# Possibility None
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hello {name}")
    else:
        print("Hello World")


print(say_hi("John"))
print(say_hi())


# Classes as types
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


# Pydantic models
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"]
}
user = User(**external_data)
print(user)  # id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id) # 123


# Type Hints with Metadata Annotations
def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


