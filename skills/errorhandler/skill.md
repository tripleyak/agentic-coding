# ErrorHandler Skill

Error handling & logging. **Triggers:** `ErrorHandler`, `error handling`, `logging setup`

**Hierarchy:** AppError (base) → ValidationError (400) → NotFoundError (404) → UnauthorizedError (401)

**Middleware:** Log (message, stack, path, userId) → Operational? Return code+message : Return 500

**Logging:** pino, structured JSON, redact sensitive fields

**Monitoring:** Sentry (errors), Datadog (APM), LogRocket (replay)
