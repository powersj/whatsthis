all: build

build:
	go build -o whatsthis ./cmd/whatsthis

clean:
	@rm -f $(BINNAME)
	@rm -f coverage.out
	@rm -f go.sum

docs:
	echo "View docs at: http://localhost:6060/pkg/whatsthis/"
	godoc -http=localhost:6060

lint:
	golangci-lint run

test:
	go test -cover -coverprofile=coverage.out  whatsthis/pkg/...

test-coverage: test
	go tool cover -html=coverage.out

.PHONY: all build clean docs lint test test-coverage
