from featureform import Client
import sys

def initialize_client():
    """Initialize the Featureform client with insecure mode."""
    try:
        client = Client(insecure=True)
        print("Featureform client initialized successfully")
        return client
    except Exception as e:
        print(f"Error initializing client: {str(e)}")
        sys.exit(1)

def serve_feature_values(client: Client, feature_name: str, feature_variant: str, entity_id: str):
    """Serve feature values for a given entity."""
    try:
        print(f"\nServing feature values for {feature_name}:{feature_variant}")
        print("-" * 50)
        
        # Get feature values
        feature_values = client.features(
            [(feature_name, feature_variant)],
            {"user": entity_id}
        )
        
        print(f"Entity ID: {entity_id}")
        print(f"Feature Values: {feature_values}")
        return feature_values
    except Exception as e:
        print(f"Error serving feature values: {str(e)}")
        return None

def main():
    # Initialize client
    client = initialize_client()
    
    # Example feature and entity details
    feature_name = "avg_transactions"
    feature_variant = "quickstart"
    entity_id = "C2421688"  # Example user ID
    
    # Serve feature values
    serve_feature_values(client, feature_name, feature_variant, entity_id)

if __name__ == "__main__":
    main() 