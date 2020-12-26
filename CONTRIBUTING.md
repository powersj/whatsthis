# Contributing

## How to contribute

I want your help. No really, I do.

There might be a little voice inside that tells you you're not ready; that you
need to do one more tutorial, or learn another framework, or write a few more
blog posts before you can help me with this project.

I assure you, that's not the case.

This project has some clear Contribution Guidelines and expectations that you
can read below.

The contribution guidelines outline the process that you will need to follow to
get a patch merged. By making expectations and process explicit, I hope it will
make it easier for you to contribute.

And you don't just have to write code. You can help out by writing
documentation, tests, or even by giving feedback about this work. (And yes,
that includes giving feedback about the contribution guidelines.)

Thank you for contributing!

(The above is from [Adrienne Lowe](https://github.com/adriennefriend/imposter-syndrome-disclaimer))

## Getting started

* Fork the [repository](https://github.com/powersj/whatsthis) on GitHub
* Read the [index.md](../index.md) for getting started and look through the
  documentation for any other basic help.
* Play with the project on a variety of systems and environments, submit bugs,
  and submit pull requests!

## Developing a merge request

* Find an issue or create your own.
* Create a feature or bug fix branch in your fork of the repo.
* Write your feature or fix your bug. Make commits of logical units.
* If needed, update the documentation in either the README or docs folder.
* Ensure the project passes the lint tests, builds, and tests pass.
* Push and submit your pull request!

### Code changes

The project has a basic CI setup already, which will run a lint, build, and
tests. These need to pass and I am more than willing to help you work through
any issues you come across. This includes disabling or changing the config
on the linters.

These CI steps are very easy to run using the makefile via:

```text
make lint
make build
make test
```

### Documentation changes

If you are working on the documentation, ensure it continues to build using
the steps outlined on the [documentation](documentation.md) page.

### Commit message

This is the rough convention I follow for commit messages:

```text
topic: <short title for what changed>
<BLANK LINE>
<why this change was made and what changed>
<BLANK LINE>
Fixes #1
```

The first line is the subject and should be no longer than 70 characters, the
second line is always blank, and other lines should be wrapped at 80
characters.

## Acceptance

These things will make a PR more likely to be accepted:

* a well-described requirement
* tests for new code
* tests for old code!
* new code and tests follow the conventions in old code and tests
* a good commit message

In general, I will merge a PR once I reviewed and approved it. Trivial changes
(e.g., corrections to spelling) will get waved through. For substantial
changes, you might get asked to resubmit the PR or divide the changes into
more than one PR.
