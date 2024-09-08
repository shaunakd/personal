from enum import Enum
import pandas as pd
from pathlib import Path, PosixPath
from typing import Union, Any
import json

PathType = Union[str, Path, PosixPath]
FileType = Union[str, pd.DataFrame, dict]


class RawFileFormats(Enum):
    JSON = ".json"
    TEXT = ".txt"


class DataFrameFileFormats(Enum):
    CSV = ".csv"
    EXCEL = ".xlsx"
    EXCEL_OLD = ".xls"
    FEATHER = ".feather"
    JSON = ".json"
    PARQUET = ".parquet"
    SQL = ".sql"

    @classmethod
    def to_list(cls) -> list[str]:
        return [file_format.value for file_format in cls]


def invert_injective_dictionary(dictionary: dict[Any, Any]) -> dict[Any, Any]:
    "Inverts dictionary where each key has a unique value"
    inverted_dict = {v: k for k, v in dictionary.items()}
    return inverted_dict


def invert_non_injective_dictionary(dictionary: dict[Any, Any]) -> dict[Any, Any]:
    "Inverts dictionary where each key does not have a unique value"
    inverted_dict: dict[Any, Any] = {}
    for v in dictionary.values():
        inverted_dict[v] = []
        for k in dictionary.keys():
            if dictionary[k] == v and k not in inverted_dict[v]:
                inverted_dict[v].append(k)
    for k in inverted_dict:
        inverted_dict[k] = tuple(inverted_dict[k])
        if len(inverted_dict[k]) == 1:
            inverted_dict[k] = inverted_dict[k][0]
    return inverted_dict


def is_extension(file_path: PathType, ext: str) -> bool:
    if isinstance(file_path, str):
        is_ext = file_path.endswith(ext)
    elif isinstance(file_path, Path) or isinstance(file_path, PosixPath):
        is_ext = file_path.suffix == ext
    return is_ext


def read_dataframe(
    file_path: Union[str, Path, PosixPath], **kwargs: Any
) -> pd.DataFrame:
    """Reads various file formats into a pandas DataFrame.

    Supported formats:
    - CSV: .csv
    - Excel: .xlsx, .xls
    - JSON: .json
    - SQL: .sql (requires a connection or SQLAlchemy engine)
    - Parquet: .parquet
    - Feather: .feather
    """

    file_path = str(file_path)  # needed for endswith

    # Handling based on file extensions
    if is_extension(file_path, DataFrameFileFormats.CSV.value):
        df = pd.read_csv(file_path, **kwargs)

    elif is_extension(file_path, DataFrameFileFormats.EXCEL.value) or is_extension(
        file_path, DataFrameFileFormats.EXCEL_OLD.value
    ):
        df = pd.read_excel(file_path, **kwargs)

    elif is_extension(file_path, DataFrameFileFormats.FEATHER.value):
        df = pd.read_feather(file_path, **kwargs)

    elif is_extension(file_path, DataFrameFileFormats.JSON.value):
        with open(file_path, "r") as file:
            data = json.load(file)
        df = pd.json_normalize(data)  # Flatten nested JSON to DataFrame

    elif is_extension(file_path, DataFrameFileFormats.PARQUET.value):
        df = pd.read_parquet(file_path, **kwargs)

    elif is_extension(file_path, DataFrameFileFormats.SQL.value):
        # `sql` requires a connection string or engine
        conn = kwargs.get("conn")  # Provide the SQL connection as `conn=`
        if conn is None:
            raise ValueError(
                "A database connection must be provided with `conn=` for .sql files"
            )
        query = kwargs.get("query")  # Use a query if passed in
        if query is None:
            raise ValueError(
                "A SQL query must be provided with `query=` for .sql files"
            )
        df = pd.read_sql_query(query, conn, **kwargs)

    else:
        raise ValueError(f"Unsupported file format: {file_path}")

    return df


def read_file(
    file_path: Union[str, Path, PosixPath], as_dataframe: bool = False, **kwargs: Any
) -> Any:
    """
    Reads various file formats, either as a Pandas DataFrame or raw content.

    If the file is a JSON, `as_dataframe` determines whether to read it as a dataframe or a dictionary
    """
    data: Any = None
    are_dataframe_extensions = [
        is_extension(file_path, file_format)
        for file_format in DataFrameFileFormats.to_list()
    ]
    if is_extension(file_path, RawFileFormats.JSON.value) and as_dataframe:
        data = read_dataframe(file_path, **kwargs)
    elif is_extension(file_path, RawFileFormats.JSON.value):
        with open(file_path) as file:
            data = json.load(file)
    elif is_extension(file_path, RawFileFormats.TEXT.value):
        with open(file_path, "r") as file:
            data = file.read()
    elif any(are_dataframe_extensions):
        data = read_dataframe(file_path, **kwargs)
    return data
