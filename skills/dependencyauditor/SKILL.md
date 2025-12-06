# DependencyAuditor Skill

Checks package.json for outdated, vulnerable, and unused packages. Safely updates them with breaking change warnings.

**Triggers:** `audit deps`, `check packages`, `update dependencies`, `npm audit`, `are my packages safe`

**Domain:** DevOps / Security

## Process

| Phase | Action | Command |
|-------|--------|---------|
| 1. Security | Check for vulnerabilities | `npm audit --json` |
| 2. Outdated | Find outdated packages | `npm outdated --json` |
| 3. Unused | Detect unused dependencies | `npx depcheck --json` |
| 4. Report | Generate audit report | — |
| 5. Update | Safe update commands | `npm update` / manual |

## Output Format

```markdown
# Dependency Audit Report
**Project:** [name]
**Date:** [date]
**Total Packages:** [count]

## Summary
| Category | Count | Severity |
|----------|-------|----------|
| Vulnerabilities | X | 🔴 Critical / 🟠 High / 🟡 Moderate |
| Outdated | X | 🟡 Behind latest |
| Unused | X | 🟢 Can remove |

## 🔴 Security Vulnerabilities (Fix First)
| Package | Severity | Issue | Fix |
|---------|----------|-------|-----|
| lodash | High | Prototype pollution | `npm update lodash` |

## 🟡 Outdated Packages
| Package | Current | Latest | Breaking Changes |
|---------|---------|--------|------------------|
| react | 18.2.0 | 19.0.0 | ⚠️ Yes - see migration guide |

## 🟢 Unused Packages (Safe to Remove)
| Package | Type | Command |
|---------|------|---------|
| moment | dependency | `npm uninstall moment` |

## Safe Update Commands
```bash
# Non-breaking updates (safe)
npm update

# Individual updates (review first)
npm install package@latest
```

## Breaking Change Warnings
[Details for any major version bumps]
```

## Severity Levels

| Level | Symbol | Action |
|-------|--------|--------|
| Critical | 🔴 | Fix immediately - security risk |
| High | 🟠 | Fix soon - potential exploit |
| Moderate | 🟡 | Plan to fix - minor risk |
| Low | 🟢 | Optional - minimal risk |

## Safe Update Rules

| Situation | Action |
|-----------|--------|
| Patch version (1.0.0 → 1.0.1) | Auto-update safe |
| Minor version (1.0.0 → 1.1.0) | Usually safe, verify |
| Major version (1.0.0 → 2.0.0) | Warn user, link changelog |
| Security vulnerability | Prioritize fix, even if breaking |

## Integration

| With Skill | Purpose |
|------------|---------|
| DeploymentGuide | Run as pre-flight check |
| SecurityAudit | Include in security review |
| ErrorExplainer | If install fails, explain why |
