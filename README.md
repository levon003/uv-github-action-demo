# UV GitHub Action Demo

Brief demonstration of using UV with a GitHub Action.

## Usage

### GitHub Action

A GitHub Action runs on every push to this repository.

Here's what the Action does:

 - Identifies files that were added or modified on the current branch, relative to the `main` branch.
 - Fail the GitHub Action if 20+ files were changed.

This is a very unreasonable thing to do, but it demonstrates multiple things:
 - A GitHub Action that uses git to identify and process added, changed, and deleted paths relative to `main`, which is more finicky than it looks
 - A simple Python package structure that works with UV
 - A multi-stage GitHub Action that installs UV and needed dependencies to execute a validation script

Here's a sample GitHub Action log when validation succeeds:

```
2025-01-28 04:03:19,215 - INFO - Validating relative to branch 'main'.
2025-01-28 04:03:19,217 - INFO - Identified 2 git file changes.
2025-01-28 04:03:19,217 - INFO - Validation succeeded.
```

Here's a sample GitHub Action log when validation fails:

```
2025-01-28 04:14:09,364 - INFO - Validating relative to branch 'bad-pr'.
2025-01-28 04:14:09,366 - INFO - Identified 20 git file changes.
2025-01-28 04:14:09,366 - ERROR - 20 files have changed, which is more than should be touched in a single change!
```

### Local usage

#### Initial setup

[Install `uv`](https://docs.astral.sh/uv/getting-started/installation/): `curl -LsSf https://astral.sh/uv/install.sh | sh`

#### Running the validation script

Run the validation script: 

```bash
uv run python -m demo_python_package
```

## Development

This demo uses `uv` for managing dependencies.

You should [install `uv`](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Tests

```bash
uv run pytest
```

### Dependencies

Add a dependency:

```bash
uv add requests
```