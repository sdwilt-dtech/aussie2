![Tests](https://github.com/sdwilt-dtech/gh-actions-test/actions/workflows/test.yml/badge.svg)

## GitHub Actions Test Project

This project demonstrates how to use GitHub Actions for CI workflows in Python, including automated testing, linting, formatting, and branch protection.

## CI Workflow with GitHub Actions

We use a GitHub Actions workflow (`.github/workflows/test.yml`) that runs on every push or pull request.

It performs the following steps:
- ✅ Checks out the repo
- 🐍 Sets up Python (v3.13)
- 📦 Installs dependencies
- 🧪 Runs `pytest` for unit tests
- 🧹 Lints code using `flake8`
- 🎨 Verifies formatting using `black`

You can view the workflow in the **Actions tab** or inspect `.github/workflows/test.yml`.

## Local Development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install


#### 4. 🔁 Pull Request Process
```md
## Pull Request Process

All changes must be made in a feature branch. When you open a pull request:
- ✅ The test workflow runs automatically
- 🚫 The PR cannot be merged unless all checks pass
- 🔍 Optionally, code reviews can be required via branch protection settings

## Status

![Tests](https://github.com/YOUR_USERNAME/gh-actions-test/actions/workflows/test.yml/badge.svg)

