from sqlalchemy import select, delete

from models.model import Client


class ClientService:

    def __init__(self, db):
        self.db = db

    async def create_client(self, payload):

        result = await self.db.execute(
            select(Client).where(
                Client.client_name == payload.client_name
            )
        )

        existing_client = result.scalar_one_or_none()

        if existing_client:
            raise Exception(
                "Client already exists"
            )

        client = Client(
            client_name=payload.client_name,
            contact_person=payload.contact_person,
            email=payload.email,
            phone=payload.phone,
            address=payload.address,
            status=payload.status,
            created_by=payload.created_by
        )

        self.db.add(client)

        await self.db.commit()

        await self.db.refresh(client)

        return client

    async def get_clients(self):

        result = await self.db.execute(
            select(Client)
        )

        return result.scalars().all()

    async def get_client(self, client_id):

        result = await self.db.execute(
            select(Client).where(
                Client.id == client_id
            )
        )

        return result.scalar_one_or_none()

    async def update_client(
        self,
        client,
        payload
    ):
        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(client, key, value)

        await self.db.commit()

        await self.db.refresh(client)

        return client

    async def delete_client(
        self,
        client_id
    ):

        await self.db.execute(
            delete(Client).where(
                Client.id == client_id
            )
        )

        await self.db.commit()