"""Launch Streamlit from the artifact directory so its theme configuration is used."""

import os
import sys
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)
port = os.environ.get("PORT", "5000")
base_path = os.environ.get("BASE_PATH", "/").strip("/")
os.execv(
    sys.executable,
    [
        sys.executable, "-m", "streamlit", "run", "app.py",
        "--server.port", port,
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--server.baseUrlPath", base_path,
        "--browser.gatherUsageStats", "false",
    ],
)
