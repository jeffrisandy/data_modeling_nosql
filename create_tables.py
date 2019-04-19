from cassandra.cluster import Cluster
from queries import create_table_queries, drop_table_queries


def create_db():
    """
    Create & connect database
    INPUT : None
    RETURN :
        session: establish connection 
        cluster: cassandra cluster
    """

    cluster = Cluster()

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()

    # session.execute("DROP KEYSPACE IF EXISTS udacity")
    session.execute("""
            CREATE KEYSPACE IF NOT EXISTS udacity 
            WITH REPLICATION = 
            { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
                    )

    # Set KEYSPACE to the keyspace specified above
    session.set_keyspace('udacity')

    return session, cluster


def connect_db():
    """
    Connect to existing database
    INPUT: None
    RETURN:
        session: establish connection 
        cluster: cassandra cluster
    """

    cluster = Cluster()

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()

    # Set KEYSPACE to the keyspace specified above
    session.set_keyspace('udacity')

    return session, cluster


def create_tables(session):
    """
    Creating tables 
    INPUT: 
        session: establish connection to database
    RETURN:
        None
    """
    for query in create_table_queries:
        session.execute(query)


def drop_tables(session):
    """
    Dropping tables 
    INPUT: 
        session: establish connection to database
    RETURN:
        None
    """
    for query in drop_table_queries:
        session.execute(query)


def disconnect_db(session, cluster):
    """
    Close & disconnect session & cluster to database 
    INPUT: 
        session: establish connection 
        cluster: cassandra cluster
    RETURN:
        None
    """
    session.shutdown()
    cluster.shutdown()


def main():
    """
    Main program for this module
    INPUT : None
    RETURN: None
    """
    session, cluster = create_db()
    drop_tables(session)
    create_tables(session)
    disconnect_db(session, cluster)


if __name__ == "__main__":
    main()
