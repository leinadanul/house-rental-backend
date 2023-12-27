'''from sqlalchemy.orm import Session
from sqlalchemy import create_engine, engine, Table, MetaData, Column, Integer, String
from sqlalchemy import insert
from models.landlord import Landlord
from managers.database.implementations.models.landlord import LandlordRecords
from managers.database.db_manager import DatabaseManager

class SqlalchemyDBManager(DatabaseManager):
    def __init__(self):
        SQLALCHEMY_DATABASE_URL = "postgresql://postgres:toor@localhost:5432/house_rental"
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.metadata = MetaData()



    def insert_landlord(self, landlord: Landlord) -> Landlord:
        with Session(self.engine) as session:
                ins = landlord.insert().values(
                    first_name = 'fist_name',
                    last_name = 'last_name',
                    email = 'email',
                    phone_number = 23232,
                    mobile_number = 1213,
                    company_name = 'company_name',
                    picture = 'picture',
                    )
                result = session.execute(ins.returning(landlord.c.id))
                autogenerated_id = result.fetchone()[0]
                print(f'The autogenerated ID is: {autogenerated_id}')




    def insert_landlord(self, landlord: Landlord) -> Landlord:
        with Session(self.engine) as session:
            new_landlord = LandlordRecords(
                first_name=landlord.first_name,
                last_name=landlord.last_name,
                email=landlord.email,
                phone_number=landlord.phone_number,
                mobile_number=landlord.mobile_number,
                company_name=landlord.company_name,
                picture=landlord.picture
            )
            result = session.execute(new_landlord.id)
            autogenerated_id = result.fet


        return landlord





#                with Session(self.engine) as session:
#                            session.add(new_landlord)
#                            session.commit()
#                return landlord


'''