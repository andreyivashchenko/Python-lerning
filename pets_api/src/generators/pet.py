
from pets_api.src.baseclasses.builder import BuilderBaseClass
from faker import Faker
fake = Faker("en_US")


class PetGenerator(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.reset()

    def set_pet_id(self, id=None):
        self.result['id'] = id
        return self

    def set_status(self, status='sold'):
        self.result['status'] = status
        return self

    def set_category(self, category={"name": "testName"}):
        self.result['category'] = category
        return self

    def set_photo_urls(self, urls=['test1', 'test2']):
        self.result["photoUrls"] = urls
        return self

    def set_name(self, name=fake.first_name()):
        self.result['name'] = name
        return self

    def set_tags(self, tags = [{'name': 'test1'}]):
        self.result['tags']=tags
        return self

    def reset(self):
        self.set_pet_id().set_name().set_status().set_category().set_photo_urls().set_tags()
        return self


