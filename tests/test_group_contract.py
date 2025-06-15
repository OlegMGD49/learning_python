from faker import Faker

from src.services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_base_client_anonym):
        group_helper = GroupHelper(base_api_client=university_base_client_anonym)
        resp = group_helper.post_group({"name":faker.name()})

        assert resp.status_code == 401, resp.json()