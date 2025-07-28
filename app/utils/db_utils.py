from sqlalchemy.orm import inspect

def row_to_dict(row) -> dict:
    return {key: getattr(row, key) for key in inspect(row).mapper.column_attrs.keys()}