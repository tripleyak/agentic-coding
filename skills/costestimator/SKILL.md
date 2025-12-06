# CostEstimator Skill

Estimates monthly costs when adding services, databases, auth, and APIs. Prevents billing surprises.

**Triggers:** `estimate costs`, `how much will this cost`, `pricing check`, `budget this`, `what will I pay`

**Domain:** Planning / DevOps

## Process

| Phase | Action |
|-------|--------|
| 1. Identify | List services being added |
| 2. Research | Look up current pricing |
| 3. Estimate | Calculate based on expected usage |
| 4. Compare | Show tier options |
| 5. Recommend | Suggest best value option |

## Common Services Pricing

### Hosting

| Service | Free Tier | Starter | Pro |
|---------|-----------|---------|-----|
| Vercel | 100GB bandwidth | $20/mo | $50/mo+ |
| Railway | $5 credit | ~$5-20/mo | Usage-based |
| Fly.io | 3 shared VMs | ~$5-15/mo | Usage-based |
| Netlify | 100GB bandwidth | $19/mo | $99/mo |

### Databases

| Service | Free Tier | Starter | Pro |
|---------|-----------|---------|-----|
| Supabase | 500MB, 2 projects | $25/mo | $599/mo |
| PlanetScale | 5GB, 1B reads | $29/mo | $99/mo |
| Neon | 512MB | $19/mo | $69/mo |
| MongoDB Atlas | 512MB | $9/mo | $57/mo |

### Auth

| Service | Free Tier | Starter | Notes |
|---------|-----------|---------|-------|
| Clerk | 10K MAU | $25/mo | Per 1K MAU after |
| Auth0 | 7K MAU | $23/mo | Per MAU |
| Supabase Auth | Unlimited | Included | With Supabase |
| NextAuth | Unlimited | Free | Self-hosted |

### AI/APIs

| Service | Free Tier | Cost | Notes |
|---------|-----------|------|-------|
| OpenAI GPT-4 | — | $0.03/1K tokens | Input tokens |
| Anthropic Claude | — | $0.015/1K tokens | Input tokens |
| Google Gemini | 60 req/min | $0.00025/1K chars | Generous free |
| Resend (email) | 100/day | $20/mo | 50K emails |
| Stripe | — | 2.9% + $0.30 | Per transaction |

## Output Format

```markdown
# Cost Estimate: [Project/Feature]

## Monthly Cost Summary

| Tier | Monthly | Annual | Best For |
|------|---------|--------|----------|
| 🟢 Free/Hobby | $0 | $0 | Development, MVP |
| 🟡 Starter | $X | $X | Early users |
| 🔴 Production | $X | $X | Growth |

## Service Breakdown

### [Service 1: e.g., Database]
| Option | Cost | Limits | Recommendation |
|--------|------|--------|----------------|
| Supabase Free | $0 | 500MB, 2 projects | ✅ Start here |
| PlanetScale | $29/mo | 5GB | For scale |

### [Service 2: e.g., Auth]
| Option | Cost | Limits | Recommendation |
|--------|------|--------|----------------|
| Supabase Auth | $0 | Unlimited | ✅ If using Supabase |
| Clerk | $0 | 10K MAU | Best DX |

## Scaling Projections

| Users | DB | Auth | Hosting | Total |
|-------|----|----- |---------|-------|
| 100 | $0 | $0 | $0 | **$0** |
| 1,000 | $0 | $0 | $0 | **$0** |
| 10,000 | $25 | $25 | $20 | **$70** |
| 100,000 | $99 | $150 | $50 | **$299** |

## Cost-Saving Tips
- Use free tiers during development
- [Specific tip for this project]
- [Another tip]

## Hidden Costs to Watch
- Bandwidth overages
- Database row limits
- API rate limits
- Support tier requirements
```

## Usage Estimation

| Metric | How to Estimate |
|--------|-----------------|
| MAU (Monthly Active Users) | Start with 100, plan for 10x |
| API calls | Estimate actions per user per day |
| Storage | Estimate data per user |
| Bandwidth | Page size × pageviews |

## Integration

| With Skill | Purpose |
|------------|---------|
| FeatureScoper | Estimate costs for scoped features |
| DeploymentGuide | Include cost info for platform |
| ArchitectPlan | Factor costs into architecture decisions |
