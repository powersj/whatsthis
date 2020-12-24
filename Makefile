all: build

build:
	go build -o whatsthis ./cmd/whatsthis

clean:
	rm -f whatsthis
	rm -f coverage.out
	rm -f go.sum
	rm -rf dist

docs:
	echo "View docs at: http://localhost:6060/pkg/whatsthis/"
	godoc -http=localhost:6060

lint:
	golangci-lint run

release:
	goreleaser

release-snapshot:
	goreleaser --rm-dist --skip-publish --snapshot

test:
	go test -cover -coverprofile=coverage.out  ./...

test-coverage: test
	go tool cover -html=coverage.out

.PHONY: all build clean docs lint test test-coverage
