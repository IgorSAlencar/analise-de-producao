"""
Conexão compartilhada com SQL Server.

Ajuste SERVER / DATABASE / DRIVER conforme o ambiente.
Os notebooks 01–03 importam daqui: from db import read_sql
"""

from __future__ import annotations

import pyodbc
import pandas as pd

SERVER = "SEU_SERVIDOR"
DATABASE = "TESTE"
DRIVER = "ODBC Driver 17 for SQL Server"


def get_connection() -> pyodbc.Connection:
    """Abre conexão ODBC com Trusted_Connection (Windows Auth)."""
    return pyodbc.connect(
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"Trusted_Connection=yes;"
    )


def read_sql(query: str) -> pd.DataFrame:
    """Executa query e retorna DataFrame. Fecha a conexão ao terminar."""
    with get_connection() as conn:
        return pd.read_sql(query, conn)
