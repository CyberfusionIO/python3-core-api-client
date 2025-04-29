import json

import faker
import pytest

from cyberfusion.CoreApiClient._encoders import CustomEncoder
from ipaddress import IPv4Address, IPv6Address


def test_CustomEncoder_datetime(faker: faker.Faker) -> None:
    date_time = faker.date_time()

    with pytest.raises(TypeError):
        json.dumps(date_time)

    assert json.dumps(date_time, cls=CustomEncoder)


def test_CustomEncoder_IPv6Address(faker: faker.Faker) -> None:
    ipv6_address = IPv6Address(faker.ipv6())

    with pytest.raises(TypeError):
        json.dumps(ipv6_address)

    assert json.dumps(ipv6_address, cls=CustomEncoder)


def test_CustomEncoder_IPv4Address(faker: faker.Faker) -> None:
    ipv4_address = IPv4Address(faker.ipv4())

    with pytest.raises(TypeError):
        json.dumps(ipv4_address)

    assert json.dumps(ipv4_address, cls=CustomEncoder)


def test_CustomEncoder_builtin(faker: faker.Faker) -> None:
    word = faker.word()

    assert json.dumps(word)

    assert json.dumps(word, cls=CustomEncoder)
