from sqlalchemy import (
    Column, DateTime, Integer,
    MetaData, Table,
)

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

statistics_table = Table(
    "statistics",
    metadata,
    Column("calculation_dt", DateTime, primary_key=True),
    Column("exchange_rate", Integer, nullable=False),
    Column("asset_value", Integer, nullable=False),
    Column("current_PnL", Integer, nullable=False),
    Column("current_Index_PnL", Integer, nullable=False),
)