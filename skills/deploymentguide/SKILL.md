# DeploymentGuide Skill

Step-by-step deployment to Vercel, Railway, Fly.io, and other platforms with pre-flight checks. Prevents "works locally, breaks in prod" issues.

**Triggers:** `deploy`, `go live`, `push to production`, `deploy to vercel`, `deploy to railway`

**Domain:** DevOps

**Dependencies:** DependencyAuditor (pre-flight)

## Process

| Phase | Action |
|-------|--------|
| 1. Pre-flight | Run checks before deployment |
| 2. Platform | Detect or select deployment target |
| 3. Configure | Ensure config files exist |
| 4. Deploy | Execute deployment commands |
| 5. Verify | Confirm deployment succeeded |

## Pre-flight Checklist

| Check | Command | Must Pass |
|-------|---------|-----------|
| Build succeeds | `npm run build` | Yes |
| Tests pass | `npm run test:run` | Yes |
| No TypeScript errors | `tsc --noEmit` | Yes |
| No security vulnerabilities | `npm audit --production` | Warning only |
| Environment variables set | Check .env.example vs platform | Yes |
| No secrets in code | Scan for API keys, passwords | Yes |
| Git clean | No uncommitted changes | Warning only |

## Platform Guides

### Vercel
```bash
# Install CLI
npm i -g vercel

# Deploy
vercel

# Production deploy
vercel --prod
```

| Config File | Purpose |
|-------------|---------|
| `vercel.json` | Build settings, redirects, headers |
| `.vercelignore` | Files to exclude |

### Railway
```bash
# Install CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

| Config File | Purpose |
|-------------|---------|
| `railway.json` | Build and start commands |
| `Procfile` | Process types |

### Fly.io
```bash
# Install CLI
curl -L https://fly.io/install.sh | sh

# Launch (first time)
fly launch

# Deploy
fly deploy
```

| Config File | Purpose |
|-------------|---------|
| `fly.toml` | App config, scaling, regions |
| `Dockerfile` | Container build |

## Environment Variables

| Platform | How to Set |
|----------|------------|
| Vercel | Dashboard → Settings → Environment Variables |
| Railway | Dashboard → Variables tab |
| Fly.io | `fly secrets set KEY=value` |

## Output Format

```markdown
# Deployment Guide: [Platform]

## Pre-flight Results
| Check | Status | Notes |
|-------|--------|-------|
| Build | ✅ | — |
| Tests | ✅ | 42 passed |
| Types | ✅ | — |
| Security | ⚠️ | 1 moderate vulnerability |
| Env vars | ✅ | 3 required, all set |

## Deploy Commands
```bash
[platform-specific commands]
```

## Post-Deploy Verification
- [ ] Site loads at [URL]
- [ ] Key features work
- [ ] No console errors
- [ ] Environment variables applied

## Rollback (if needed)
```bash
[rollback commands]
```
```

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Build fails on platform | Different Node version | Set `engines` in package.json |
| Missing env vars | Not configured on platform | Add via dashboard/CLI |
| 404 on routes | SPA routing not configured | Add rewrite rules |
| CORS errors | API URL mismatch | Update API_URL env var |

## Integration

| With Skill | Purpose |
|------------|---------|
| DependencyAuditor | Pre-flight security check |
| BackupSnapshot | Snapshot before deploy |
| ErrorExplainer | Explain deploy failures |
