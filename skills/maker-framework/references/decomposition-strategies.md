# Decomposition Strategies

Task-type specific patterns for breaking complex work into atomic, verifiable steps.

## Contents

1. [Coding Tasks](#coding-tasks)
2. [Data & Analysis Tasks](#data--analysis-tasks)
3. [Workflow & Automation](#workflow--automation)
4. [General Problem-Solving](#general-problem-solving)
5. [Anti-Patterns](#anti-patterns)

---

## Coding Tasks

### Interface-First Pattern

1. Define interface/types
2. Write function signature
3. Implement happy path
4. Add error handling
5. Write unit tests
6. Integration test

**Example decomposition for "Add user authentication":**
```
├── Define User type/interface
├── Create auth service interface
├── Implement password hashing function
├── Implement token generation
├── Implement token validation
├── Create login endpoint handler
├── Create logout endpoint handler
├── Write unit tests for auth service
├── Write integration tests for endpoints
└── Update API documentation
```

### Bug Fix Pattern

1. Reproduce the bug (create failing test)
2. Locate root cause
3. Implement fix (minimal change)
4. Verify fix (test passes)
5. Check for regressions
6. Document the fix

### Refactoring Pattern

1. Write characterization tests
2. Identify extraction target
3. Extract (one refactoring move)
4. Verify tests still pass
5. Repeat for each move

**Key principle:** One refactoring operation per step. Never combine "extract method" with "rename variable."

### Feature Addition Pattern

```
├── Milestone 1: Interface Design
│   ├── Define data models
│   ├── Define API contracts
│   └── Review interfaces
├── Milestone 2: Core Implementation
│   ├── Implement data layer
│   ├── Implement business logic
│   └── Implement API handlers
├── Milestone 3: Integration
│   ├── Wire components together
│   ├── Add error handling
│   └── Add logging/metrics
└── Milestone 4: Testing
    ├── Unit tests
    ├── Integration tests
    └── Manual verification
```

---

## Data & Analysis Tasks

### ETL Pattern

```
├── Extract
│   ├── Connect to data source
│   ├── Validate connection
│   ├── Fetch data subset (test)
│   ├── Fetch full dataset
│   └── Verify extraction complete
├── Transform
│   ├── Validate input schema
│   ├── Apply transformation 1
│   ├── Validate intermediate result
│   ├── Apply transformation 2
│   ├── Validate final schema
│   └── Handle edge cases
└── Load
    ├── Prepare destination
    ├── Load test batch
    ├── Verify test batch
    ├── Load full dataset
    └── Verify load complete
```

### Analysis Pattern

```
├── Data Preparation
│   ├── Load dataset
│   ├── Validate data quality
│   ├── Handle missing values
│   └── Normalize/standardize
├── Exploration
│   ├── Summary statistics
│   ├── Distribution analysis
│   ├── Correlation analysis
│   └── Identify patterns
├── Analysis
│   ├── Apply method 1
│   ├── Validate results
│   ├── Apply method 2
│   └── Compare results
└── Reporting
    ├── Create visualizations
    ├── Write findings
    └── Document methodology
```

### Data Migration Pattern

1. Schema comparison
2. Migration script draft
3. Dry run on test data
4. Validate test migration
5. Backup production data
6. Execute migration
7. Validate production migration
8. Rollback plan verification

---

## Workflow & Automation

### State Machine Pattern

Model the workflow as states with explicit transitions:

```
├── State: Initial
│   └── Transition: validate_input → Validated
├── State: Validated
│   ├── Transition: process_success → Processed
│   └── Transition: process_failure → Failed
├── State: Processed
│   └── Transition: finalize → Complete
├── State: Failed
│   ├── Transition: retry → Validated
│   └── Transition: abort → Aborted
└── State: Complete (terminal)
```

**Each transition is one step.**

### CI/CD Pipeline Pattern

```
├── Build Stage
│   ├── Install dependencies
│   ├── Compile/transpile
│   ├── Run linter
│   └── Verify build artifacts
├── Test Stage
│   ├── Run unit tests
│   ├── Run integration tests
│   ├── Generate coverage report
│   └── Verify coverage threshold
├── Deploy Stage
│   ├── Prepare deployment package
│   ├── Deploy to staging
│   ├── Run smoke tests
│   ├── Deploy to production
│   └── Verify production health
└── Rollback Procedures
    ├── Define rollback trigger
    ├── Implement rollback script
    └── Test rollback procedure
```

### Error Handling as Explicit Steps

Don't embed error handling in main steps. Create explicit error-handling steps:

```
├── Attempt operation
├── [Success path] Process result
├── [Error: Timeout] Retry with backoff
├── [Error: Auth failed] Refresh credentials
├── [Error: Not found] Create resource
└── [Error: Unknown] Log and escalate
```

---

## General Problem-Solving

### Goal-Subgoal Hierarchy

```
Goal: Improve application performance
├── Subgoal: Identify bottlenecks
│   ├── Profile application
│   ├── Analyze profiling data
│   └── Prioritize bottlenecks
├── Subgoal: Optimize critical path
│   ├── Optimize bottleneck 1
│   ├── Measure improvement
│   ├── Optimize bottleneck 2
│   └── Measure improvement
└── Subgoal: Verify improvements
    ├── Run benchmark suite
    ├── Compare to baseline
    └── Document results
```

### Research-Then-Implement Pattern

Separate discovery from implementation:

```
├── Research Phase
│   ├── Identify options
│   ├── Evaluate option A
│   ├── Evaluate option B
│   ├── Compare trade-offs
│   └── Select approach
└── Implementation Phase
    ├── [Implementation steps]
    └── ...
```

### Decision Points as Steps

Make decisions explicit:

```
├── Gather requirements
├── DECISION: Which database?
│   ├── Document: PostgreSQL vs MongoDB
│   ├── Decision criteria listed
│   └── Selected: PostgreSQL (rationale)
├── Implement with PostgreSQL
└── ...
```

---

## Anti-Patterns

### Over-Decomposition

**Problem:** Steps so small they lose context.

**Signs:**
- More than 50 steps for a simple feature
- Steps like "open file" followed by "write line 1"
- Context needs to be re-established each step

**Fix:** Combine related micro-operations into logical units.

### Under-Decomposition

**Problem:** Steps too large, hiding complexity.

**Signs:**
- Single step takes >30 minutes
- User can't verify correctness without deep analysis
- "Implement the feature" as one step

**Fix:** Apply one of the patterns above to break down.

### Circular Dependencies

**Problem:** Step A needs B, but B needs A.

**Signs:**
- Can't determine execution order
- Steps reference each other

**Fix:** Extract shared dependency into separate step executed first.

### Implicit Ordering

**Problem:** Dependencies not explicitly tracked.

**Signs:**
- Steps fail because prerequisites missing
- "This should have been done first"

**Fix:** Use parent-child relationships in tracker, or explicit dependency notes.

### Mixed Concerns

**Problem:** One step does multiple unrelated things.

**Signs:**
- Step description uses "and" multiple times
- Step touches multiple components/files

**Fix:** Split into focused steps, one concern each.

---

## Quick Reference: Step Size Heuristics

| Type | Target Duration | Max Lines Changed | Verification Time |
|------|-----------------|-------------------|-------------------|
| Code implementation | 5-15 min | 50 lines | 1-2 min |
| Configuration | 2-5 min | 10 lines | 30 sec |
| Data transformation | 5-10 min | 1 operation | 1-2 min |
| Documentation | 5-10 min | 1 section | 1 min |
| Command/script | 1-5 min | 1 command | 30 sec |
| Decision | 2-10 min | N/A | 1-5 min |
