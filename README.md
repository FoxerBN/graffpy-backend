# 🍓 Graffpy Backend

> 📈 A simple Flask-based Python app that schedules jobs to monitor a Raspberry Pi and visualize its history with graphs

## 🚀 Features

- 🔄 **Automated Monitoring** - Scheduled jobs to track Raspberry Pi metrics
- 📊 **Data Visualization** - Generate beautiful graphs from historical data
- 🐍 **Flask Framework** - Lightweight and efficient Python backend
- 📡 **API Endpoints** - RESTful API for data access
- 🗄️ **Database Integration** - Store and manage monitoring data

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Server**: Gunicorn WSGI
- **Database**: SQLite/PostgreSQL
- **Visualization**: Chart.js/Plotly
- **Testing**: Coverage & Unit Tests

## 📁 Project Structure

```
graffpy-backend/
├── 📂 src/           # Main application code
│   └── main.py       # Flask app entry point
├── 📂 database/      # Database files and migrations
├── 📂 templates/     # HTML templates
├── 📂 test/          # Unit tests
├── 📄 requirements.txt
├── 📄 gunicorn.conf.py
└── 📄 .coverage      # Test coverage report
```

## 🚀 Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run with Gunicorn (Production)**
   ```bash
   gunicorn src.main:app
   ```

3. **Access the application**
   ```
   http://localhost:3000
   ```

## 📊 API Endpoints

- `GET /api/metrics` - Retrieve system metrics
- `GET /api/graphs` - Get graph data
- `POST /api/schedule` - Schedule monitoring jobs
- `GET /health` - Health check endpoint

## 🧪 Testing

Run tests with coverage:
```bash
python -m pytest test/ --cov=src
```

## 🔧 Configuration

Edit `gunicorn.conf.py` to customize server settings:
- Port configuration
- Worker processes
- Logging settings

## 🤝 Contributing

Feel free to open issues and submit pull requests!

## 📄 License

This project is open source and available under the MIT License.

---
Made with ❤️ by [FoxerBN](https://github.com/FoxerBN)
