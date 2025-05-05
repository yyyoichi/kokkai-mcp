echo "Hi, initializing the devcontainer..."

echo "Starting Docker Compose..."
docker compose -f '.devcontainer/compose.yaml' up -d --build

echo "Devcontainer initialized."