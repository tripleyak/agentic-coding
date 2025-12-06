# MonorepoSetup Skill

Monorepo config. **Triggers:** `MonorepoSetup`, `Turborepo setup`, `workspace setup`

| Tool | Config |
|------|--------|
| Turborepo | turbo.json |
| Nx | nx.json |
| pnpm | pnpm-workspace.yaml |

**Structure:** `apps/` (web, mobile, api) + `packages/` (ui, config, utils, types)

**Commands:** `pnpm turbo build`, `--filter=web`, `pnpm add pkg --filter=@repo/utils`
