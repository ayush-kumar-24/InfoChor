from src.pipeline.orchestrator import Pipeline

if __name__ == "__main__":
    url = "https://blog.python.org/2023/10/python-3120-is-now-available.html"   # change to real URL later

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
        