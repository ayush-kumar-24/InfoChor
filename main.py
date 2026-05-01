import json
from src.pipeline.orchestrator import Pipeline

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=8jPQjjsBbIc"  


    # 🔥 Create object (this was missing)
    pipeline = Pipeline()

    # Run pipeline
    result = pipeline.run(url)

    # Handle output
    if isinstance(result, dict) and result.get("status") == "failed":
        print("❌ Pipeline Failed:", result["reason"])
    else:
        print("✅ Success:", result)
        print(url)
print("\n🚀 INFOCHOR OUTPUT\n")
print(json.dumps(result, indent=2))