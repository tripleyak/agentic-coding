# Frontend Design Skill

Distinctive UIs avoiding AI slop. **Triggers:** Any frontend/UI work

## Typography
**FORBIDDEN:** Inter, Roboto, Arial, Helvetica, Open Sans, Lato, system fonts

| Context | Display | Body |
|---------|---------|------|
| Editorial | Playfair Display, Crimson Pro | Source Sans 3, IBM Plex Sans |
| SaaS | Space Grotesk, Bricolage Grotesque | IBM Plex Sans, DM Sans |
| Dev Tools | JetBrains Mono, Cascadia Code | IBM Plex Mono |
| E-commerce | Crimson Pro, Fraunces | Work Sans, General Sans |
| Creative | Bricolage Grotesque, Syne | DM Sans, Outfit |
| Luxury | Cormorant Garamond, Cinzel | Jost, Raleway |

**Rules:** Weight extremes (100-300 vs 700-900), scale 1.333+, fluid `clamp()` sizing

## Color & Backgrounds
**AVOID:** Purple/blue gradients on white, flat #FFF/#000

| Technique | Use |
|-----------|-----|
| OKLCH | Color tokens, gradients |
| Gradient mesh | Hero backgrounds |
| Noise (0.03 opacity) | Atmosphere |
| Glassmorphism | Cards, overlays |

**Layering:** Base → Primary gradient → Accent → Noise (0.02-0.05) → Vignette | **Color:** 60-30-10, 4.5:1 contrast

## Animation
**Rules:** Only `transform` + `opacity` (GPU) | micro 100-200ms, transitions 200-300ms, page 400-500ms

| Library | Best For | Size |
|---------|----------|------|
| Framer Motion | React gestures | 45kb |
| GSAP | Timelines, scroll | 60kb |
| Auto Animate | Zero-config | 2kb |

**Effects:** Text reveal (GSAP SplitText), Magnetic cursor (Framer), Parallax (ScrollTrigger), Page transitions (AnimatePresence)

## 3D (Three.js)
**Use:** Heroes, product showcases | **Avoid:** Forms, mobile-critical
**Stack:** `@react-three/fiber` + `drei` + `postprocessing`
**Perf:** `<Suspense>`, throttle useFrame, mobile `dpr={[1,1.5]}`

## UI Libraries
| Library | Best For |
|---------|----------|
| shadcn/ui | Full control |
| Aceternity UI | Marketing effects |
| Magic UI | SaaS animations |

**Effects:** Bento grid, Spotlight, Glowing border, Shimmer, Background beams, Aurora

## Modern CSS
`:has()`, Container queries, CSS Nesting, `@layer`, Subgrid, `color-mix()`, View Transitions

## Checklist
`□ No forbidden fonts □ OKLCH colors □ Layered bg □ GPU animations □ Asymmetry □ Premium library □ No AI look`

**Targets:** LCP <2.5s | FID <100ms | CLS <0.1 | Bundle <200kb | 60fps
