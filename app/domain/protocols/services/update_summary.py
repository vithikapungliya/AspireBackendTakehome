from .generate_summary import get_llm_response
import pandas as pd

from .sql_connection import make_conection
from .data_aggregation import update_module_summary

async def update_summary(label):
    connection= make_conection()
    response_summary = get_llm_response(label,connection)
    # response_summary="summary generated"
    res = update_module_summary(connection,label,response_summary)
    connection.close()
    return res