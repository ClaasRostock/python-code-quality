# Changelog

All notable changes to the [python-code-quality] project will be documented in this file.<br>
The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Dependencies
* Updated to ruff>=0.14.3  (from ruff>=0.11.0)
* Updated to pyright>=1.1.407  (from pyright>=1.1.396)
* Updated to sourcery>=1.40  (from sourcery>=1.35)
* Updated to dictIO>=0.4.2  (from dictIO>=0.4.1)
* Updated to pytest>=8.4  (from pytest>=8.3)
* Updated to pytest-cov>=7.0  (from pytest-cov>=6.0)
* Updated to Sphinx>=8.2  (from Sphinx>=8.1)
* Updated to sphinx-argparse-cli>=1.20  (from sphinx-argparse-cli>=1.19)
* Updated to sphinx-autodoc-typehints>=3.5  (from sphinx-autodoc-typehints>=3.0)
* Updated to furo>=2025.9  (from furo>=2024.8)
* Updated to pre-commit>=4.3  (from pre-commit>=4.1)
* Updated to mypy>=1.18  (from mypy>=1.15)
* Updated to checkout@v5  (from checkout@v4)
* Updated to setup-python@v6  (from setup-python@v5)
* Updated to setup-uv@v7  (from setup-uv@v5)
* Updated to upload-artifact@v5  (from upload-artifact@v4)
* Updated to download-artifact@v5  (from download-artifact@v4)
* pyproject.toml: added required-environments to uv.tools (windows, linux)
* pyproject.toml: updated required Python version to ">= 3.11, < 3.15"
* pyproject.toml: updated supported Python versions to 3.11, 3.12, 3.13, 3.14
* ruff.toml: updated target Python version to "py311"
* .sourcery.yaml: updated the lowest Python version the project supports to '3.11'
* pyproject.toml: removed deprecated pyright setting 'reportShadowedImports'
* pyproject.toml: removed deprecated mypy plugin 'numpy.typing.mypy_plugin'
* pyproject.toml: removed leading carets and trailing slashes from 'exclude' paths
* GitHub workflow _test.yml: updated Python versions in test matrix to 3.11, 3.12, 3.13, 3.14
* GitHub workflow _test_future.yml: updated Python version in test_future to 3.15.0-alpha - 3.15.0
* GitHub workflow _test_future.yml: updated name of test_future job to 'test315'
* GitHub workflow _test_future.yml: updated Python specifier in comment to 3.15
* GitHub workflow _test_future.yml: updated Python specifier in workflow name to py315
* GitHub workflow _build_and_publish_documentation.yml: changed 'uv sync --upgrade' to 'uv sync --frozen' to avoid unintentional package upgrades.
* .pre-commit-config.yaml: updated rev of pre-commit-hooks to v6.0.0
* .pre-commit-config.yaml: updated rev of ruff-pre-commit to v0.14.3
* .pre-commit-config.yaml: updated id of ruff to ruff-check
* Sphinx conf.py: removed ruff rule exception on file level
* VS Code settings: (Recommended extensions): Removed deprecated IntelliCode extension and replaced it by GitHub Copilot Chat as recommended replacement.
* VS Code Settings: (Recommended extensions): Removed 'njqdev.vscode-python-typehint' (Python Type Hint). Not maintained since 1 year, and the functionality is now covered by GitHub Copilot.
VS Code Settings: (Recommended extensions): Added 'ms-python.debugpy' (Python Debugger).
VS Code Settings: (Recommended extensions): Added 'ms-python.vscode-python-envs' (Python Environments).
* VS Code settings: Updated 'mypy-type-checker.reportingScope' to 'custom'.

### Dependencies
* Updated to Sphinx>=8.1  (from Sphinx>=8.2)
* Updated to sphinx-autodoc-typehints>=3.0  (from sphinx-autodoc-typehints>=3.1)

### Dependencies
* Updated to ruff>=0.11.0  (from ruff>=0.9.5)
* Updated to pyright>=1.1.396  (from pyright>=1.1.393)
* Updated to sourcery>=1.35  (from sourcery>=1.33)
* Updated to Sphinx>=8.2  (from Sphinx>=8.1)
* Updated to sphinx-autodoc-typehints>=3.1  (from sphinx-autodoc-typehints>=3.0)
* Updated to pre-commit>=4.1  (from pre-commit>=4.0)

-/-


## [0.2.0] - 2025-03-13

### Changed
* GitHub workflows: Disabled cache by default, as `uv.lock` does not get committed by default. <br>
(If a user opts to make the `uv.lock` file part of the repository, the caching can be enabled again.)
* Changed from `pip`/`tox` to `uv` as package manager
* README.md : Completely rewrote section "Development Setup", introducing `uv` as package manager.
* Replaced black formatter with ruff formatter

### Added
* Added support for Python 3.13
* Added `mypy` as static type checker (in addition to `pyright`)

### Removed
* VS Code settings: Removed the setting which added the /src folder to PythonPath. This is no longer necessary. `uv` installs the project itself as a package in "editable" mode, which removes the need to manually add /src to the PythonPath environment variable.

#### Dependencies
* Updated to ruff>=0.9.5  (from ruff>=0.9.2)
* Updated to pyright>=1.1.393  (from pyright>=1.1.392)
* Updated to sourcery>=1.33  (from sourcery>=1.31)
* Updated to ruff>=0.9.2  (from ruff>=0.8.3)
* Updated to pyright>=1.1.392  (from pyright>=1.1.390)
* Updated to sourcery>=1.31  (from sourcery>=1.27)
* Updated to sphinx-autodoc-typehints>=3.0  (from sphinx-autodoc-typehints>=2.5)
* Updated to mypy>=1.14  (from mypy>=1.13)
* Updated to setup-uv@v5  (from setup-uv@v2)
* Updated to dictIO>=0.4.1  (from dictIO>=0.4.0)
* Updated to dictIO>=0.4.0  (from dictIO>=0.2.9)
* Updated to pytest>=8.3  (from pytest>=7.4)
* Updated to pytest-cov>=6.0  (from pytest-cov>=4.1)
* Updated to Sphinx>=8.1  (from Sphinx>=7.2)
* Updated to sphinx-argparse-cli>=1.19  (from sphinx-argparse-cli>=1.11)
* Updated to myst-parser>=4.0  (from myst-parser>=2.0)
* Updated to furo>=2024.8  (from furo>=2023.9.10)
* Updated to checkout@v4  (from checkout@v3)
* Updated to setup-python@v5  (from setup-python@v4)
* Updated to actions-gh-pages@v4  (from actions-gh-pages@v3)
* Updated to upload-artifact@v4  (from upload-artifact@v3)
* Updated to download-artifact@v4  (from download-artifact@v3)


## [0.1.0] - 2023-02-27

* Initial release

### Added

* demo_type_hints_and_naming
* demo_comments_and_docstrings
* demo_sourcery
* demo_dynamic_typing
* demo_duck_typing



<!-- Markdown link & img dfn's -->
[unreleased]: https://github.com/ClaasRostock/python-code-quality/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/ClaasRostock/python-code-quality/releases/tag/v0.1.0...v0.2.0
[0.1.0]: https://github.com/ClaasRostock/python-code-quality/releases/tag/v0.1.0
[python_code_quality]: https://github.com/ClaasRostock/python-code-quality
