# Versioning

The project follows [Sematic Versioning](https://semver.org/).

## Release a new version

The current under-development release version is kept in
`pkg/cmd/whatsthis/cmd/root.go`:

```go
const (
    version = "v1.2.0"
)
```

To release a new version create and push a new tag, then run the goreleaser:

```shell
git tag -a v1.2.0 -m "Summary of release"
git push origin v1.2.0
make release
```

This will create the corresponding
[GitHub Releases page](https://github.com/powersj/whatsthis/releases/) and
upload the artifacts to it.

Then increment the version in `pkg/cmd/whatsthis/cmd/root.go` and push that
change to open the next version:

```shell
git commit -am "Open release v1.3.0"
git push
```
