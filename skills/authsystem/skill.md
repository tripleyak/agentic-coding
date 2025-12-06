# AuthSystem Skill

Authentication. **Triggers:** `AuthSystem`, `setup auth`, `login system`

| Pattern | Best For |
|---------|----------|
| Session | Traditional web |
| JWT | API, mobile, SPA |
| OAuth 2.0 | Social login |
| Magic link | Passwordless |
| Passkeys | Modern passwordless |

**JWT:** Access (15m) + Refresh (7d), verify middleware, RBAC permissions

**Checklist:** Passwords hashed, HTTPS, Rate limiting, Lockout, CSRF, Refresh rotation
