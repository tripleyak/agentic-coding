# EnvManager Skill

Manages .env files across environments. Syncs variables, validates configs, prevents missing env var issues.

**Triggers:** `setup env`, `sync env vars`, `check env`, `environment variables`, `missing env`

**Domain:** DevOps / Configuration

## Process

| Phase | Action |
|-------|--------|
| 1. Scan | Find all .env* files |
| 2. Compare | Diff against .env.example |
| 3. Validate | Check required vars are set |
| 4. Report | Show missing/extra vars |
| 5. Fix | Help add missing vars |

## File Hierarchy

| File | Purpose | Git |
|------|---------|-----|
| `.env.example` | Template with dummy values | ✅ Commit |
| `.env.local` | Local development overrides | ❌ Ignore |
| `.env` | Default values | ⚠️ Usually ignore |
| `.env.development` | Dev-specific | ❌ Ignore |
| `.env.production` | Prod-specific | ❌ Ignore |
| `.env.test` | Test-specific | ❌ Ignore |

## Validation Rules

| Rule | Check |
|------|-------|
| Required vars exist | All vars in .env.example have values |
| No empty values | `VAR=` is flagged |
| No placeholder values | `your-key-here` is flagged |
| Format valid | Key=value format |
| No secrets in .env.example | API keys, passwords flagged |

## Output Format

```markdown
# Environment Audit

## Files Found
| File | Variables | Status |
|------|-----------|--------|
| .env.example | 12 | ✅ Template |
| .env.local | 10 | ⚠️ 2 missing |
| .env.production | 0 | ❌ Not found |

## Missing Variables
| Variable | In | Missing From | Required |
|----------|-------|--------------|----------|
| `DATABASE_URL` | .env.example | .env.local | Yes |
| `API_KEY` | .env.example | .env.local | Yes |

## Extra Variables (not in template)
| Variable | Found In | Action |
|----------|----------|--------|
| `DEBUG` | .env.local | Add to .env.example or remove |

## Placeholder Values (need real values)
| Variable | Current Value | File |
|----------|---------------|------|
| `API_KEY` | `your-key-here` | .env.local |

## Commands to Fix
```bash
# Add missing to .env.local
echo "DATABASE_URL=" >> .env.local
echo "API_KEY=" >> .env.local
```
```

## Common Patterns

### Creating .env.example from .env
```bash
# Copy structure without values
sed 's/=.*/=/' .env > .env.example
```

### Syncing with team
```bash
# Check what's missing
diff <(cut -d= -f1 .env.example | sort) <(cut -d= -f1 .env.local | sort)
```

## Security Checks

| Pattern | Risk | Action |
|---------|------|--------|
| Actual API keys in .env.example | High | Replace with placeholder |
| .env committed to git | High | Add to .gitignore |
| Secrets in error messages | Medium | Never log env values |
| Hardcoded in source | High | Move to env var |

## Platform Sync

| Platform | Command |
|----------|---------|
| Vercel | `vercel env pull` |
| Railway | `railway env` |
| Fly.io | `fly secrets list` |
| Heroku | `heroku config` |

## Integration

| With Skill | Purpose |
|------------|---------|
| DeploymentGuide | Verify env vars before deploy |
| SecurityAudit | Check for exposed secrets |
| ErrorExplainer | Diagnose missing env var errors |
