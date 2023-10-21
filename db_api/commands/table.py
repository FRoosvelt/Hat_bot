from sqlalchemy import select

from db_api.database import get_session
from db_api.tables.table import Table


async def select_id(id: int):
    async with get_session() as session:
        sql = select(Table).where(
            Table.id == id
        )
        result = await session.execute(sql)
        return result.scalar()
