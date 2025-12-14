from pydantic import BaseModel

from cyberfusion.CoreApiClient.models import RootModelCollectionMixin
import faker
import pytest


def test_RootModelCollectionMixin_iter_not_dict_or_list(faker: faker.Faker) -> None:
    class Model(RootModelCollectionMixin, BaseModel):
        root: int

    model = Model(root=faker.pyint())

    with pytest.raises(TypeError, match="^Type does not support iter$"):
        for _ in model:
            pass


def test_RootModelCollectionMixin_getitem_not_dict_or_list(faker: faker.Faker) -> None:
    class Model(RootModelCollectionMixin, BaseModel):
        root: int

    model = Model(root=faker.pyint())

    with pytest.raises(TypeError, match="^Type does not support getitem$"):
        model["a"]


def test_RootModelCollectionMixin_items_not_dict(faker: faker.Faker) -> None:
    class Model(RootModelCollectionMixin, BaseModel):
        root: int

    model = Model(root=faker.pyint())

    with pytest.raises(TypeError, match="^Type does not support items$"):
        model.items()


def test_RootModelCollectionMixin_dict_iter(faker: faker.Faker) -> None:
    dict_ = {"a": "b"}

    class Model(RootModelCollectionMixin, BaseModel):
        root: dict[str, str]

    model = Model(root=dict_)

    for k in model:
        assert k == "a"

    for k, v in model.items():
        assert k == "a"
        assert v == "b"


def test_RootModelCollectionMixin_dict_items(faker: faker.Faker) -> None:
    dict_ = {"a": "b"}

    class Model(RootModelCollectionMixin, BaseModel):
        root: dict[str, str]

    model = Model(root=dict_)

    items = model.items()

    assert list(items) == [("a", "b")]


def test_RootModelCollectionMixin_list_iter(faker: faker.Faker) -> None:
    list_ = ["a", "b"]

    class Model(RootModelCollectionMixin, BaseModel):
        root: list[str]

    model = Model(root=list_)

    assert [v for v in model] == list_


def test_RootModelCollectionMixin_list_getitem(faker: faker.Faker) -> None:
    list_ = ["a"]

    class Model(RootModelCollectionMixin, BaseModel):
        root: list[str]

    model = Model(root=list_)

    assert model[0] == "a"


def test_RootModelCollectionMixin_dict_getitem(faker: faker.Faker) -> None:
    dict_ = {"a": "b"}

    class Model(RootModelCollectionMixin, BaseModel):
        root: dict[str, str]

    model = Model(root=dict_)

    assert model["a"] == "b"
