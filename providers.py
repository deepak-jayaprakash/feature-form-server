import featureform as ff
import sys

def main():
    try:
        print("Initializing Featureform client...")
        client = ff.Client(insecure=True)
        print("Client initialized successfully")
        client.apply()
        print("Initial client configuration applied")

        print("\nRegistering PostgreSQL provider...")
        postgres = ff.register_postgres(
            name="postgres1",
            description="Local PostgreSQL offline store",
            team="featureform",
            host="feature-form-server-1-postgres-1",
            port="5432",
            user="postgres",
            password="postgres",
            database="featureform"
        )    
        client.apply()
    
        print("PostgreSQL provider applied")

        print("\nRegistering Redis provider...")
        redis = ff.register_redis(
            name="redis-quickstart",
            description="Local Redis inference store",
            team="featureform",
            host="host.docker.internal",
            port=6379,
            password="",
            db=0,
        )
        print("Redis provider registered successfully")
        client.apply()
        print("Redis provider applied")

        print("\nRegistering transactions table...")
        transactions = postgres.register_table(
            name="transactions",
            table="transactions",
        )
        print("Transactions table registered successfully")
        client.apply()
        print("Transactions table applied")

        print("\nDefining SQL transformation...")
        @postgres.sql_transformation(inputs=[transactions])
        def max_user_transaction(tr):
            return (
                "SELECT CustomerID as user_id, max(TransactionAmount) "
                "as max_transaction_amt from {{tr}} GROUP BY user_id"
            )
        print("SQL transformation defined successfully")
        client.apply()
        print("SQL transformation applied")

        print("\nDefining User entity and features...")
        @ff.entity
        class User:
            sum_transactions = ff.Feature(
                max_user_transaction[
                    ["user_id", "max_transaction_amt"]
                # ],
                # variant="quickstart3",
                type=ff.Float32,
                inference_store=redis,
            )

            fraudulent2 = ff.Label(
                transactions[["customerid", "isfraud"]], 
                # variant="quickstart3", 
                type=ff.Bool,
            )
        client.list_sources
        print("User entity and features applied")

        # print("\nRegistering training set...")
        # ff.register_training_set(
        #     name="fraud_training",
        #     label=User.fraudulent2,
        #     features=[User.sum_transactions],
        #     variant="quickstart3",
        # )
        # client.apply()

        print("\nAll steps completed successfully!")

    except Exception as e:
        print(f"\nError occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()