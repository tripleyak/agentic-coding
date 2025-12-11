# ShelfWins-Studio - Claude Instructions

> Project-specific instructions for Claude Code sessions.
> For global instructions, see `~/.claude/CLAUDE.md`

## Project Context

**What:** Strategic merchandising & financial modeling app for retail
**Stack:** React 19 + TypeScript 5.8 + Vite 6 + Tailwind + Gemini AI
**Domain:** Planograms, GMROI calculations, buyer presentations

## Quick Commands

```bash
npm run dev          # Start dev server (localhost:5173)
npm run build        # Production build
npm run test:run     # Run tests once
npm run test         # Watch mode
npm run lint         # ESLint check
```

## Verification (Before Every Commit)

```bash
npx tsc --noEmit && npm run lint && npm run test:run && npm run build
```

All must pass with 0 errors. Fix issues before committing.

## Documentation Files

| File | Purpose | Update When |
|------|---------|-------------|
| `ROADMAP.md` | Future work with JSON status | Task status changes |
| `APP_MAP.md` | Architecture + UI navigation | Code structure changes |
| `SESSION_HANDOFF.md` | Session state for continuity | Every session end |
| `README.md` | Public GitHub documentation | Major features added |

## Code Patterns

### Adding a Component
1. Create in `components/` (or `components/[Feature]/` for complex ones)
2. Add types to `types.ts` if needed
3. If modal: add to `ModalRenderer.tsx` and `lazy.tsx`
4. If exports: call `addExportRecord()`

### Adding a Hook
1. Create in `hooks/`
2. Use `useCallback` for all handlers
3. Import and use in `App.tsx`

### Adding AI Capability
Edit `services/geminiService.ts`:
- `sendMessage()` - Strategy chat
- `generateImage()` - Text-to-image
- `generateProductImage()` - Imagen 3
- `analyzeShelfImage()` - Vision analysis
- `generateContent()` - Generic content

### Adding a Retailer
Edit `types.ts` → `RETAILER_PROFILES` object

### Adding Sample Products
Edit `constants.ts` → `SAMPLE_PRODUCTS` array

## Code Style

- Functional components only (no classes)
- TypeScript strict mode
- Tailwind for styling
- Lucide React for icons
- camelCase variables, PascalCase components
- Early returns for error handling
- Mac keyboard shortcuts (Cmd not Ctrl)
- Extract logic to custom hooks with useCallback
- Use React.memo for components receiving callbacks

## Key Files to Know

| File | Purpose |
|------|---------|
| `App.tsx` | Main orchestrator (~500 lines, uses 16 hooks) |
| `types.ts` | All TypeScript types, 12 retailer profiles |
| `constants.ts` | 37 sample products, fixture definitions |
| `components/layout/ModalRenderer.tsx` | Renders all 25+ modals |
| `hooks/usePlanogramHandlers.ts` | Physics engine for product placement |
| `services/geminiService.ts` | All Gemini AI integration |

## Common Gotchas

1. **Modal state**: Use `useModalManager` hook, not individual useState
2. **Product updates**: Must update library, staging, AND shelf items
3. **Heavy libraries**: html2canvas/jsPDF are lazy-loaded in exportService
4. **Physics**: Check `usePlanogramHandlers.ts` for placement rules
5. **Exports**: Always call `addExportRecord()` when generating exports

## Environment

```bash
# .env.local
VITE_GEMINI_API_KEY=your_key_here
```

---

*Keep this file lean - detailed docs are in APP_MAP.md*
