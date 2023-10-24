from DB.src.base_classes.builder import BuilderBaseClass
from faker import Faker
fake = Faker("en_US")


class UserGenerator(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.result['first_name'] = fake.first_name()
        self.result['last_name'] = fake.last_name()
        self.result['full_name'] = fake.name()
        self.result['job_title'] = fake.job()
        self.result['job_type'] = "Full-time"
        self.result['phone'] = fake.phone_number()
        self.result['email'] = fake.safe_email()
        self.result['image'] = fake.image_url()
        self.result['country'] = fake.country()
        self.result['city'] = fake.city()
        self.result['onboarding_completion'] = fake.random_int(min=1, max=100)
        return self

