import duckdb
from datetime import date
from typing import Optional

class DuckDB:
    """
    duckdbの接続を管理するクラス
    dimension はベクトル長。モデル依存。
    """
    def __init__(self, s3uri: str, dimension: int = 384):
        con = duckdb.connect(database=":memory:",config = {'allow_unsigned_extensions': 'true'}) # type: ignore
        # faiss拡張をロード
        con.execute("INSTALL faiss FROM community;")
        con.sql("LOAD faiss;")
        con.execute('INSTALL httpfs;')
        con.sql('LOAD httpfs;')
        con.execute("SET force_download=true;")
        con.execute(f"""
            CREATE OR REPLACE TABLE speeches AS
            SELECT ROW_NUMBER() OVER () AS faiss_id -- 連番を付与してfaiss_idとして使用
            , * FROM read_parquet('{s3uri}');
        """)

        index_name = 'speeches_faiss_idx'  # A unique name for your FAISS index
        # 1. Create a FAISS index
        # 'IDMap,Flat' creates an index that maps FAISS internal IDs back to your provided IDs (original_id)
        # and uses a flat (exact L2) search. For larger datasets, consider other types like 'IDMap,HNSW32'.
        con.execute(f"CALL FAISS_CREATE('{index_name}', {dimension}, 'IDMap,Flat');")
        # 2. Add data to the FAISS index
        # This selects the 'faiss_id' and 'speech_vector' from your table.
        con.execute(f"CALL FAISS_ADD((SELECT faiss_id, speech_vector FROM speeches), '{index_name}');")

        self.con = con
        self.index_name = index_name
        self.dimension = dimension
    
    def query(self, 
        query: list[float],
        from_date: Optional[date] = None,
        until_date: Optional[date] = None,
        speaker: Optional[str] = None,
        topk: int = 5
    ):
        # クエリ条件を組み立て
        filter_parts: list[str] = []
        if from_date:
            filter_parts.append(f"date >= ''{from_date.isoformat()}''")
        if until_date:
            filter_parts.append(f"date <= ''{until_date.isoformat()}''")
        if speaker:
            safe_speaker = speaker.replace("'", "''")  # Basic SQL string escaping
            filter_parts.append(f"speaker = ''{safe_speaker}''")
        # The filter expression is a SQL boolean expression string
        filter_sql_expression = " AND ".join(filter_parts) if filter_parts else "TRUE"
        # The query vector needs to be in a SQL array format
        query_vector_sql_literal = f"CAST({query} AS FLOAT[])"

        # ベクトル検索（faiss）＋属性フィルタ
        # 4. Perform the search using FAISS_SEARCH_FILTER and join results
        sql = f"""
        WITH faiss_search_results AS (
            SELECT
                (result_item).label AS id_from_faiss,      -- This 'label' is the 'faiss_id'
                (result_item).distance AS l2_distance
            FROM
                UNNEST(FAISS_SEARCH_FILTER(
                    '{self.index_name}',                 -- Name of the FAISS index
                    {topk},                         -- Number of nearest neighbors to retrieve
                    {query_vector_sql_literal},     -- The query vector
                    '{filter_sql_expression}',      -- SQL filter condition to apply on 'speeches' table
                    'faiss_id',                  -- Column in 'speeches' providing IDs for filtering
                    'speeches'                      -- Table to apply the filter on
                )) AS tbl(result_item)              -- Unnest the list of structs returned by FAISS
        )
        SELECT
            s.speech_id
            -- s.*,  -- Select all columns from the original speeches table
            -- fsr.l2_distance AS l2  -- Add the L2 distance from FAISS results
        FROM
            speeches s
        JOIN
            faiss_search_results fsr ON s.faiss_id = fsr.id_from_faiss
        ORDER BY
            fsr.l2_distance ASC; 
        """
        # Note: The LIMIT {topk} is handled by the 'k' parameter in FAISS_SEARCH_FILTER.

        results = self.con.execute(sql).fetchdf()
        # speech_idを取得してlist[str]で返す
        ids: list[str] = [row[0] for row in results.itertuples(index=False)] # type: ignore
        return ids
        

# 使い方例
if __name__ == "__main__":
    import random
    s3uri = "http://localhost:9001/api/v1/download-shared-object/aHR0cDovLzEyNy4wLjAuMTo5MDAwL2tva2thaS1tY3AtYnVja2V0L2tva2thaV9zcGVlY2hfMjAyNS0wMS0wMV8yMDI1LTA0LTMwLnBhcnF1ZXQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD0wUVg2MTM0QzBCN0dBOUlTTVpJMyUyRjIwMjUwNTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUxNlQwMzU3MzJaJlgtQW16LUV4cGlyZXM9NDMxOTkmWC1BbXotU2VjdXJpdHktVG9rZW49ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmhZMk5sYzNOTFpYa2lPaUl3VVZnMk1UTTBRekJDTjBkQk9VbFRUVnBKTXlJc0ltVjRjQ0k2TVRjME56UXhNREkzTml3aWNHRnlaVzUwSWpvaWJXbHVhVzloWkcxcGJpSjkuTXE1bWI5QWI4RnkxZjRtaVhCRXlNM2RHeUlfT25mSjV6LUJvVnVsdk9ZNno2YUZpa3VNd0lseUFKbmg4NWZkdXROM2VzNDh2Z2t1MzlkZENDcGRqeHcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnZlcnNpb25JZD1udWxsJlgtQW16LVNpZ25hdHVyZT1kMjIxMTY3YjliODQ1NDU0ZmMyZmUyMDdjOWM1OGQ2YTY3ZjU3OTZjYzVlMmEzZjNjZDg2OTQyMTBjMWM2YmRh"
    db = DuckDB(s3uri=s3uri)
    query = [random.random() for _ in range(db.dimension)]  # クエリベクトル
    # from datetime import date
    df = db.query(
        query=query,
        from_date=date(2025, 3, 1),
        # until_date=date(2024, 12, 31),
        speaker="石破茂"
    )
    print(df)