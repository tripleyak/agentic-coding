# SecurityAudit Skill

Security analysis. **Triggers:** `SecurityAudit`, `security scan`, `check vulnerabilities`

**OWASP Top 10:** Injection, Broken Auth, Data Exposure, XXE, Access Control, Misconfig, XSS, Deserialization, Vulnerable Components, Logging

**4-Agent Team:** Code (static analysis) | Dependencies (npm audit, CVEs) | Config (secrets, headers) | Infrastructure (Docker, CI/CD)

**Checks:** `npm audit --production`, secrets scan, headers review

**Output:** Risk level, Critical findings, Secrets detected, Dependency vulns, Security headers, Compliance checklist
