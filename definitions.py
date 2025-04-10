import featureform as ff


postgres = ff.register_postgres(
            name="postgres3",
            description="Local PostgreSQL offline store",
            team="featureform",
            host="feature-form-server-1-postgres-1",
            port="5432",
            user="postgres",
            password="postgres",
            database="postgres"
        )


redis = ff.register_redis(
            name="redis2",
            description="Local Redis inference store",
            team="featureform",
            host="host.docker.internal",
            port=6379,
            password="",
            db=0,
        )


transactions = postgres.register_table(
    name="transactions",
    table="transactions",  # This is the table's name in Postgres
)


@postgres.sql_transformation(inputs=[transactions])
def average_user_transaction(tr):
    return (
        "SELECT CustomerID as user_id, avg(TransactionAmount) "
        "as avg_transaction_amt from {{tr}} GROUP BY user_id"
    )


@ff.entity
class User:
    avg_transactions = ff.Feature(
        average_user_transaction[
            ["user_id", "avg_transaction_amt"]
        ],  # We can optional include the `timestamp_column` "timestamp" here
        # variant="random2",
        type=ff.Float32,
        inference_store=redis,
    )

    fraudulent = ff.Label(
        transactions[["customerid", "isfraud"]], 
        # variant="random2", 
        type=ff.Bool,
    )


ff.register_training_set(
    name="fraud_training",
    label=User.fraudulent,
    features=[User.avg_transactions],
    # variant="random2",
)



