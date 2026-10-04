from pydantic import BaseModel


class Address(BaseModel):
    zip_code: str
    city: str


class User(BaseModel):
    name: str
    id: int
    email: str
    address: Address
    is_cative: bool = False


user = User(name='Bob',
            id=1,
            email='bob@fake.com',
            is_cative=True,
            #address={"city": "New York", "zip_code": "100000"}
            address=Address(zip_code='123-45-67', city='Moscow')
            )

print(user.name)
print(user.address.city)
