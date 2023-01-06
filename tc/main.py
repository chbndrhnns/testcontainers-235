import sqlalchemy

from testcontainers.postgres import PostgresContainer


if __name__ == "__main__":
    postgres_container = PostgresContainer("postgres:9.5")
    with postgres_container as postgres:
        e = sqlalchemy.create_engine(postgres.get_connection_url())
        result = e.execute("select version()")
        (version,) = result.fetchone()
    print(version)
