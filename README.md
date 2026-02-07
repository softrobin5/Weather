# Weather App

A minimal Flask application that fetches current conditions from the OpenWeatherMap API and renders them in a lightweight web UI. Users submit a city name, the backend queries the remote API, and the template displays temperature, humidity, wind speed, and a short textual description. The project also includes Docker/Docker Compose assets for containerized deployments.

## Features
- Flask server with a single route that handles both GET form display and POST submissions.
- `requests`-based client for OpenWeatherMap with metric units selected by default.
- Friendly HTML/CSS frontend located under `templates/` and `static/`.
- Dockerfile and `docker-compose.yaml` for reproducible builds plus `.env`-style configuration through environment variables.

## Tech Stack
- Python 3.11
- Flask
- Requests
- Docker (optional)

## Prerequisites
- Python 3.11+ with `pip`
- OpenWeatherMap API key (free tier works)
- Optional: Docker + Docker Compose v2

## Configuration
| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `WEATHER_API_KEY` | Yes | `PUT_YOUR_API_KEY_HERE` (in `bot.py`) | API key used when calling OpenWeatherMap. Override via environment variable in production or Compose. |

> **Tip:** Never commit your real API keys. Use `export WEATHER_API_KEY=...` locally or populate the value in `docker-compose.yaml` before deploying.

## Project Structure
```
.
├── bot.py               # Main Flask application
├── templates/
│   └── index.html       # Jinja2 template rendered by the root route
├── static/
│   └── style.css        # Styling for the weather card UI
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container image definition
└── docker-compose.yaml  # Local multi-container orchestration file
```

## Local Development
1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Export your API key (replace the placeholder):
   ```bash
   export WEATHER_API_KEY="your_real_key"
   ```
4. Start the Flask app:
   ```bash
   python bot.py
   ```
5. Visit http://localhost:80 (or the port you configure) and search for any city.

## Running with Docker
### Build manually
```bash
docker build -t weather-app .
docker run -it --rm -p 80:80 -e WEATHER_API_KEY="your_real_key" weather-app
```

### Docker Compose (recommended)
```bash
docker compose up --build
```
- Edit `docker-compose.yaml` to set a valid `WEATHER_API_KEY`.
- The service publishes port 80 from the container to your host.

## Testing
It exposes `http://localhost/` and should respond with `Working!`. Use this script as a quick sanity check or adapt it for integration tests.

## Usage Notes
- API responses are returned in metric units; adjust the `units` query parameter in `bot.py` if you need imperial values.
- Errors from OpenWeatherMap (e.g., invalid city) are surfaced in the UI as a simple message—extend the handling block in `index()` for richer feedback if needed.
- Set `debug=False` before shipping to production environments.

## Improving This Project
- Add input validation and debounce logic to reduce unnecessary API calls.
- Display additional metrics such as sunrise/sunset or multi-day forecasts via the One Call API.
- Cache responses using Redis or Flask-Caching to stay within free-tier API limits.
- Wire up an automated test suite (pytest) and CI pipeline.

## License
Specify your preferred license terms here (MIT, Apache-2.0, etc.) if you intend to share or distribute the project.
