import json
import os
from datetime import datetime


class FileHandler:

    def save(self, data, folder="outputs"):
        os.makedirs(folder, exist_ok=True)

        filename = f"{folder}/output_{datetime.now().timestamp()}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return filename

    # 🔥 NEW METHOD (failure logging)
    def save_failed(self, data):
        folder = "outputs/failed"
        os.makedirs(folder, exist_ok=True)

        filename = f"{folder}/failed_{datetime.now().timestamp()}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return filename