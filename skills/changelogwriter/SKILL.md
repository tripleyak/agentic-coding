# ChangelogWriter Skill

Auto-generates CHANGELOG entries from git commits. Keeps changelog up to date without manual effort.

**Triggers:** `update changelog`, `what changed`, `generate changelog`, `release notes`

**Domain:** Documentation

## Process

| Phase | Action |
|-------|--------|
| 1. Gather | Get commits since last changelog entry |
| 2. Categorize | Group by type (feat, fix, etc.) |
| 3. Format | Generate Keep a Changelog format |
| 4. Insert | Add to CHANGELOG.md |

## Commit Type Mapping

| Commit Prefix | Changelog Section |
|---------------|-------------------|
| `feat:` | Added |
| `fix:` | Fixed |
| `refactor:` | Changed |
| `perf:` | Changed |
| `docs:` | Documentation |
| `style:` | Changed |
| `test:` | — (skip) |
| `chore:` | — (skip) |
| `BREAKING:` | ⚠️ Breaking Changes |

## Commands

```bash
# Get commits since last tag
git log $(git describe --tags --abbrev=0)..HEAD --oneline

# Get commits since date
git log --since="2024-12-01" --oneline

# Get commits with type prefix
git log --oneline | grep -E "^[a-f0-9]+ (feat|fix|refactor):"
```

## Output Format (Keep a Changelog)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- New feature description ([commit](link))
- Another feature

### Fixed
- Bug fix description
- Another fix

### Changed
- Refactoring or behavior change

### Deprecated
- Features to be removed in future

### Removed
- Removed features

### Security
- Security fixes

---

## [1.2.0] - 2024-12-04

### Added
- [Previous release entries...]
```

## Smart Formatting

| Raw Commit | Formatted Entry |
|------------|-----------------|
| `feat: add user auth` | New user authentication system |
| `fix: login button not working` | Fixed login button not responding to clicks |
| `refactor: cleanup auth code` | Refactored authentication code for clarity |

## Version Detection

| Source | How |
|--------|-----|
| package.json | Read `version` field |
| Git tags | `git describe --tags` |
| Manual | Ask user |

## Integration

| With Skill | Purpose |
|------------|---------|
| GitWorkflow | Generate changelog before release |
| DeploymentGuide | Include in release checklist |
| DocSync | Keep docs in sync |
