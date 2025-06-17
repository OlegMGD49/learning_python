from faker import Faker

from logger.logger import Logger
from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_client_anonym):
        group_helper = GroupHelper(api_utils=university_api_client_anonym)
        response = group_helper.post_group(json={"name": faker.name()})

        assert response.status_code == 401, \
            f"Wrong status code. Actual: '{response.status_code}', but expected: '401'"
