from pathlib import Path


def load_dotenv(path: Path = Path(".env")) -> dict[str, str]:
    env = {}
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        env[key.strip()] = value.strip()
    return env
