# APIDocGen Skill

Generates API documentation from code. Creates OpenAPI specs, endpoint references, and usage examples.

**Triggers:** `document API`, `generate docs`, `API documentation`, `openapi spec`, `swagger`

**Domain:** Documentation

## Process

| Phase | Action |
|-------|--------|
| 1. Scan | Find API routes/endpoints |
| 2. Extract | Parse request/response types |
| 3. Generate | Create OpenAPI 3.0 spec |
| 4. Format | Generate markdown docs |
| 5. Examples | Add usage examples |

## Detection Patterns

| Framework | Pattern |
|-----------|---------|
| Next.js App Router | `app/**/route.ts` |
| Next.js Pages | `pages/api/**/*.ts` |
| Express | `app.get/post/put/delete()` |
| Fastify | `fastify.route()` |
| tRPC | `router.query/mutation()` |

## Output Formats

### OpenAPI 3.0 Spec
```yaml
openapi: 3.0.0
info:
  title: [Project] API
  version: 1.0.0
  description: Auto-generated API documentation

servers:
  - url: http://localhost:3000
    description: Development
  - url: https://api.example.com
    description: Production

paths:
  /api/users:
    get:
      summary: List all users
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
    post:
      summary: Create a user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserInput'
      responses:
        '201':
          description: User created

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
```

### Markdown Reference
```markdown
# API Reference

## Authentication
All requests require `Authorization: Bearer <token>` header.

## Endpoints

### Users

#### GET /api/users
List all users.

**Response**
| Field | Type | Description |
|-------|------|-------------|
| id | string | User ID |
| email | string | User email |

**Example**
```bash
curl -X GET https://api.example.com/api/users \
  -H "Authorization: Bearer token"
```

#### POST /api/users
Create a new user.

**Request Body**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | User email |
| name | string | Yes | User name |

**Example**
```bash
curl -X POST https://api.example.com/api/users \
  -H "Authorization: Bearer token" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "name": "John"}'
```
```

## Type Extraction

| Source | Extracts |
|--------|----------|
| TypeScript types | Request/response schemas |
| Zod schemas | Validation rules |
| JSDoc comments | Descriptions |
| Function params | Required fields |

## Documentation Sections

| Section | Content |
|---------|---------|
| Overview | API description, base URL, auth |
| Authentication | How to authenticate |
| Endpoints | All routes with params |
| Schemas | Data models |
| Errors | Error codes and meanings |
| Examples | curl/fetch examples |

## Integration

| With Skill | Purpose |
|------------|---------|
| APIDesign | Generate docs from design |
| DocSync | Keep docs in sync with code |
| TestGen | Generate API tests from spec |
