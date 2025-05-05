echo "Hi, initializing the devcontainer..."

echo "Starting Docker Compose..."
docker compose -f '.devcontainer/compose.yaml' up -d --build

echo "Installing dependencies..."
if [ ! -f ".venv/bin/python" ]; then
    echo "🎍 make venv"
    uv venv && \
        source .venv/bin/activate && \
        uv sync --frozen
else
    echo "skip make venv"
fi

echo "Devcontainer initialized."