from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None



class Customer(User):
    customer_id: str
    address: str | None = None
    phone_number: str | None = None
