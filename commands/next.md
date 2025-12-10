# Suggest Next Task

Recommend what to work on next based on development plan priorities.

## Instructions

1. Read `DEVELOPMENT_PLAN.md`
2. Look at P6 (UI/Design) and P7 (Performance) checklists
3. Find the first unchecked `[ ]` item in each priority tier:
   - P6-Critical items first
   - P7-Critical items first
   - Then Important/High items
   - Then Nice-to-Have/Medium items

4. Check git status for any work in progress

5. Recommend ONE specific task to work on next

## Output Format

```
## Recommended Next Task

Based on the development plan, here's what to work on:

### Task: <Task Name>
**Phase**: P6-A / P7-B / etc.
**Priority**: Critical / High / Medium
**From checklist**: "[ ] <exact checklist item>"

### Why This Task
<1-2 sentences on why this is the right next step>

### Getting Started
1. <First step>
2. <Second step>
3. <Third step>

### Files Likely Involved
- <file1.tsx>
- <file2.tsx>
```
