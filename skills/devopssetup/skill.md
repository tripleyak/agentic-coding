# DevOpsSetup Skill

CI/CD & deployment. **Triggers:** `DevOpsSetup`, `setup CI/CD`, `Docker setup`

**Pipeline:** checkout → npm ci → lint → test:coverage → build → security (npm audit, CodeQL) → deploy

**Docker:** Multi-stage build (builder → runner), USER node, EXPOSE 3000

| Platform | Config |
|----------|--------|
| Vercel | vercel.json |
| Railway | railway.json |
| AWS | terraform/, cdk/ |
| Fly.io | fly.toml |

**Monitoring:** Logs (Datadog), Metrics (Prometheus), Tracing (OpenTelemetry), Errors (Sentry)
