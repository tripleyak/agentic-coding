# DBSchema Skill

Database design. **Triggers:** `DBSchema`, `database design`, `schema design`

**Process:** Entities → Attributes → Normalize (3NF) → Indexes → Migrations

| Pattern | Use |
|---------|-----|
| Soft delete | `deleted_at TIMESTAMP NULL` |
| Polymorphic | `*_type`, `*_id` |
| Audit columns | `created_at`, `updated_at` |
| UUID | Distributed systems |

**Index Types:** B-tree (equality, range), GIN (full-text, JSON), GiST (geo)
