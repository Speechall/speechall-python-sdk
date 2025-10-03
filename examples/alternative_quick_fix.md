# Quick Fix for Local SDK Packaging

Add the following section to the repository's `pyproject.toml` to point setuptools at the current directory for the `speechall` package:

```toml
[tool.setuptools.package-dir]
speechall = "."
```

This tells the build backend that the package lives at the repository root, matching the existing module layout without moving files. After saving the change, reinstall the editable package from the examples directory:

```bash
.venv/bin/pip install -e ..
```

Once installation succeeds, the example scripts can import `speechall` from the local SDK.
