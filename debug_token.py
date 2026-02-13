from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def test_inference():
    try:
        client = InferenceClient(token=HF_TOKEN)
        # Try a very standard model like distilbert-base-uncased-finetuned-sst-2-english
        print("Testing with distilbert-base-uncased-finetuned-sst-2-english...")
        result = client.text_classification("I love you", model="distilbert-base-uncased-finetuned-sst-2-english")
        print("Success!", result)
    except Exception as e:
        print("Failed with standard model:", e)

    try:
        print("\nTesting with tabularisai/multilingual-sentiment-analysis...")
        client = InferenceClient(token=HF_TOKEN)
        result = client.text_classification("I love you", model="tabularisai/multilingual-sentiment-analysis")
        print("Success!", result)
    except Exception as e:
        print("Failed with target model:", e)

if __name__ == "__main__":
    test_inference()
