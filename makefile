# Build: docker build -t cloudhealth .
build:
	docker build -t cloudhealth .

# Run: docker run -p 8000:8000 --env-file .env cloudhealth
run:
	docker run -p 8000:8000 --env-file .env cloudhealth

# Delete all containers and images
clean:
	docker rm -f $(shell docker ps -aq) || true
	docker rmi -f cloudhealth || true
