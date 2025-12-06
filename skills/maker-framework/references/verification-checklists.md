# Verification Checklists

Domain-specific checklists for validating step outputs.

## Contents

1. [Code Implementation](#code-implementation)
2. [Configuration & Setup](#configuration--setup)
3. [Data & Analysis](#data--analysis)
4. [Documentation](#documentation)
5. [Commands & Scripts](#commands--scripts)
6. [General Steps](#general-steps)

---

## Code Implementation

### Before Marking Verified

- [ ] Code compiles/parses without errors
- [ ] No new linter warnings introduced
- [ ] Follows existing code style
- [ ] Function/method does one thing
- [ ] Variable names are descriptive
- [ ] No hardcoded values that should be config
- [ ] Error cases handled appropriately

### Edge Cases

- [ ] Null/undefined inputs handled
- [ ] Empty collections handled
- [ ] Boundary values tested
- [ ] Invalid inputs rejected gracefully
- [ ] Concurrent access considered (if applicable)

### Security

- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Input validation present
- [ ] Sensitive data not logged
- [ ] Authentication/authorization checked

### Testing

- [ ] Unit tests written or updated
- [ ] Tests pass
- [ ] Existing tests still pass
- [ ] Edge cases covered
- [ ] Test names are descriptive

---

## Configuration & Setup

### Correctness

- [ ] All required fields present
- [ ] Values are valid types
- [ ] Paths are correct and accessible
- [ ] URLs are properly formatted
- [ ] Environment variables referenced correctly

### Security

- [ ] Secrets not committed to version control
- [ ] Appropriate file permissions set
- [ ] Sensitive values use environment variables
- [ ] No default credentials in config

### Portability

- [ ] Works across environments (dev/staging/prod)
- [ ] No hardcoded machine-specific paths
- [ ] Dependencies version-pinned appropriately
- [ ] Required environment documented

### Reversibility

- [ ] Change can be rolled back
- [ ] Backup taken if destructive
- [ ] Previous config preserved if needed

---

## Data & Analysis

### Input Validation

- [ ] Data source verified
- [ ] Schema matches expectations
- [ ] Row/record count verified
- [ ] No unexpected null values
- [ ] Data types correct

### Transformation Validity

- [ ] Transformation logic correct
- [ ] Output schema matches spec
- [ ] No data loss during transform
- [ ] Aggregations verified with samples
- [ ] Join keys validated

### Reproducibility

- [ ] Random seeds set (if applicable)
- [ ] Data version recorded
- [ ] Code version recorded
- [ ] Environment documented
- [ ] Steps documented

### Sanity Checks

- [ ] Output ranges reasonable
- [ ] Summary statistics make sense
- [ ] Known values verified
- [ ] No impossible values
- [ ] Trends match expectations

---

## Documentation

### Accuracy

- [ ] Matches current implementation
- [ ] Code examples run correctly
- [ ] Links are valid
- [ ] Version numbers correct
- [ ] API signatures accurate

### Completeness

- [ ] All parameters documented
- [ ] Return values described
- [ ] Error conditions covered
- [ ] Prerequisites listed
- [ ] Examples provided

### Clarity

- [ ] Jargon explained or avoided
- [ ] Steps in logical order
- [ ] Screenshots current (if used)
- [ ] Formatting consistent
- [ ] Audience appropriate

### Maintainability

- [ ] Easy to update
- [ ] No duplicated information
- [ ] Links to related docs
- [ ] Change log updated (if applicable)

---

## Commands & Scripts

### Safety

- [ ] Dry run performed first
- [ ] Non-destructive or backed up
- [ ] Correct environment targeted
- [ ] No unintended side effects
- [ ] Timeout/kill plan exists

### Correctness

- [ ] All arguments correct
- [ ] Paths exist and accessible
- [ ] Permissions sufficient
- [ ] Dependencies available
- [ ] Expected output produced

### Idempotency

- [ ] Can run multiple times safely
- [ ] State checked before action
- [ ] Errors don't leave partial state
- [ ] Recovery procedure exists

### Observability

- [ ] Progress visible
- [ ] Errors clearly reported
- [ ] Exit code meaningful
- [ ] Logs available

---

## General Steps

### Universal Checklist

- [ ] Step completed as described
- [ ] Output matches expectations
- [ ] No unintended side effects
- [ ] Reversible if needed
- [ ] Documentation updated (if applicable)

### Red Flag Indicators

Flag if any of these apply:
- [ ] Step took much longer than expected
- [ ] Required significant workarounds
- [ ] Uncertainty about correctness
- [ ] Unexpected errors encountered
- [ ] Dependencies on external systems failed

---

## Verification Response Format

When verifying a step, respond with:

```
VERIFIED - [brief confirmation]
```

or

```
UNCERTAIN - [what's unclear]
```

or

```
FAILED - [what went wrong]
```

### Examples

**Verified:**
```
VERIFIED - Function correctly returns sorted list, all tests pass
```

**Uncertain:**
```
UNCERTAIN - Code looks correct but I can't verify the API response format
```

**Failed:**
```
FAILED - Compilation error on line 42: undefined variable 'user'
```
