import uvicorn
from fastapi import FastAPI
from accounts.models.address import Address
from accounts.models.customer import Customer
from accounts.models.account import Account
from accounts.repositories.address import AddressRepository
from accounts.services.address import AddressService
from typing import List

address_repo = AddressRepository()
app = FastAPI()
address_service = AddressService(address_repo)

@app.post('/api/address/new')
async def create_address(address: Address):
    return address_service.add_new(address)

@app.get('/api/address', response_model=List[Address])
async def retrieve_addresses():
    return address_service.get_all()

if __name__ == '__main__':
    #inserted = Address(id=23, address="asdf", city="chino", state="CA", zip_code="91710")
    #address_repo.insert(inserted)
    #print(address_repo.get_all())

    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True,
                timeout_keep_alive=3600, workers=10)