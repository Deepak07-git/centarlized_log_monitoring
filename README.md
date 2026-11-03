# Centralized Log Monitoring & Security Analytics Platform

A containerized log monitoring platform built with Elasticsearch, Filebeat, Django, and Docker Compose. It uses deterministic, rule-based detection to identify suspicious log activity, classify threats, calculate risk scores, and trigger defensive workflows such as email alerts and IP-block records.

## Quick Start

### Prerequisites
- Docker Engine / Docker Desktop with Docker Compose
- At least 4 GB RAM (more may be needed for Elasticsearch)

### Launch
```bash
git clone https://github.com/hari-107/centarlized_log_monitoring.git
cd centarlized_log_monitoring
cp .env.example .env
docker compose up --build -d
```

Open the dashboard at **http://localhost:8000**.

## Architecture

```text
Log Generator / Monitored Servers
             |
             v
          Filebeat
             |
             v
       Elasticsearch
             |
             v
    Django processing pipeline
             |
      Rule-based detection
       |      |       |
       v      v       v
    Threat  Risk    IP extraction
    records scoring      |
       |                 v
       |          Active response records
       v
 Dashboard and email alerts
```

| Component | Responsibility |
|---|---|
| **Filebeat** | Collects log files and forwards events |
| **Elasticsearch** | Centralized log storage, search, and aggregation |
| **Django** | Rule evaluation, threat records, APIs, dashboard, and alerting |
| **Log Generator** | Simulates log activity from monitored servers |
| **Grafana** | Optional visualization |

## Detection

The processing pipeline uses predefined regular-expression and keyword patterns to identify events such as SSH brute force, SQL injection, XSS, DDoS patterns, directory traversal, web shells, command injection, privilege escalation, SSRF, remote code execution, data exfiltration, port scans, and unauthorized access.

Severity and risk are determined by configured detection rules. The project does not depend on an LLM, external AI API, or model runtime.

## Security Workflows

- Store detected events with severity, classification, source IP, and risk score.
- Record blocked IPs and handled-log actions through the active-response service.
- Send email alerts for High and Critical events when SMTP is configured.

> IP blocking is currently represented by application active-response records. It does not automatically install firewall rules on the monitored host.

## Database Migrations

The application runs migrations during container startup. To apply them manually:

```bash
docker compose exec django-app python manage.py migrate
```

## Email Alerting

Copy `.env.example` to `.env` and configure the SMTP values:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-sender@gmail.com
SMTP_PASSWORD=your-gmail-app-password
ALERT_EMAIL_FROM=your-sender@gmail.com
ALERT_EMAIL_TO=your-recipient@gmail.com
```

For Gmail, use an App Password rather than your normal account password.

## Service URLs

| Service | URL |
|---|---|
| Dashboard | http://localhost:8000 |
| Elasticsearch | http://localhost:9200 |
| Grafana | http://localhost:3000 |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/servers/` | List monitored servers and threat statistics |
| GET | `/api/logs/?server_id=&severity=&keyword=` | Search/filter Elasticsearch logs |
| GET | `/api/threats/?server_id=&severity=&status=` | Filter stored threats |
| GET | `/api/stats/` | Dashboard statistics |
| POST | `/api/detect/` | Trigger rule-based processing |
| POST | `/api/resolve/<id>/` | Mark a threat as resolved |

## Useful Commands

```bash
docker compose up --build -d
docker compose logs -f django-app
docker compose logs -f filebeat
docker compose down
```

Keep SMTP credentials in your local `.env` file and never commit that file.
