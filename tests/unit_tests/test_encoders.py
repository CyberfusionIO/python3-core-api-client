import json

import faker
import pytest

from cyberfusion.CoreApiClient._encoders import DatetimeEncoder


def test_DatetimeEncoder(faker: faker.Faker) -> None:
    date_time = faker.date_time()

    with pytest.raises(TypeError):
        json.dumps(date_time)

    assert json.dumps(date_time, cls=DatetimeEncoder)
