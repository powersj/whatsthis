all: build

build:
	go build -o whatsthis ./cmd/whatsthis

clean:
	rm -f whatsthis coverage.out go.sum
	rm -rf dist/ site/

docs:
	mkdocs build

docs-api:
	echo "View docs at: http://localhost:6060/pkg/whatsthis/"
	godoc -http=localhost:6060

lint:
	golangci-lint run

release: clean
	goreleaser

release-snapshot: clean
	goreleaser --rm-dist --skip-publish --snapshot

test:
	go test -cover -coverprofile=coverage.out  ./internal/... ./pkg/...

test-coverage: test
	go tool cover -html=coverage.out

.PHONY: all build clean docs docs-api lint release release-snapshot test test-coverage
