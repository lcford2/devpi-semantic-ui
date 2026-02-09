Devpi Semantic UI
#################

A modern Semantic UI theme for devpi (PyPI-compatible package server).

This theme provides a clean, responsive web interface for devpi using the Semantic UI framework.

Requirements
============

- Python ≥ 3.9
- devpi-server ≥ 6.12.1
- devpi-web ≥ 4.0

Installation
============

### Install from source

Clone the repository and install:

```bash
git clone https://github.com/apihackers/devpi-semantic-ui.git
cd devpi-semantic-ui
pip install -e .
```

Or install directly from the local directory:

```bash
pip install /path/to/devpi-semantic-ui
```

### Verify installation

Verify the theme is installed correctly:

```bash
python -c "from importlib.metadata import entry_points; eps = entry_points(); devpi_eps = eps.select(group='devpi_server') if hasattr(eps, 'select') else eps.get('devpi_server', []); print('\n'.join(f'{ep.name}: {ep.value}' for ep in devpi_eps))"
```

You should see `devpi-semantic-ui: devpi_semantic_ui` in the output.

Usage
=====

### Basic usage

Start devpi-server with the Semantic UI theme:

```bash
devpi-server --theme semantic-ui
```

### Complete setup example

If you're setting up devpi from scratch:

```bash
# 1. Install devpi-server (if not already installed)
pip install "devpi-server>=6.12.1"

# 2. Install the theme
pip install -e /path/to/devpi-semantic-ui

# 3. Initialize devpi (first time only)
devpi-init

# 4. Start devpi with the Semantic UI theme
devpi-server --theme semantic-ui --host 0.0.0.0 --port 3141
```

### Access the web interface

Open your browser and navigate to:
- `http://localhost:3141` (if running locally)
- `http://your-server-ip:3141` (if running on a remote server)

### Development mode

For theme development with auto-reload:

```bash
CHAMELEON_RELOAD=true devpi-server --theme semantic-ui
```

This enables template reloading without restarting the server.

Troubleshooting
===============

### Theme not found

If you get an error that the theme cannot be found, verify:

1. The package is installed:
   ```bash
   pip list | grep devpi-semantic-ui
   ```

2. The entry point is registered:
   ```bash
   python -c "from importlib.metadata import entry_points; print([ep.name for ep in entry_points().select(group='devpi_server')])"
   ```

3. You're using the correct theme name: `--theme semantic-ui`

### devpi-server version

This theme requires devpi-server ≥ 6.12.1. Check your version:

```bash
devpi-server --version
```

If your version is older, upgrade:

```bash
pip install --upgrade "devpi-server>=6.12.1"
```

Screenshots
===========


![Home screenshot](screenshots/home.png "Home page")

![index screenshot](screenshots/index.png "Index page")
