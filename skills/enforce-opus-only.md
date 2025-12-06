# Enforce Opus 4.5 Only

## 🚨 CRITICAL MANDATORY CHECK - EXECUTE FIRST 🚨

**THIS SKILL RUNS AUTOMATICALLY AT THE START OF EVERY SESSION**

## Model Verification Protocol

**BEFORE doing ANYTHING else, you MUST:**

1. **Check your current model identity**
   - Identify exactly which model you are
   - Check the model ID string

2. **Verify you are Claude Opus 4.5**
   - Required model: `claude-opus-4-5-20251101`
   - If you are ANY other model → PROCEED TO STEP 3
   - If you ARE Opus 4.5 → Confirm and proceed with work

3. **If you are NOT Opus 4.5:**
   - **STOP ALL WORK IMMEDIATELY**
   - Output this message to user:
     ```
     ⛔ INCORRECT MODEL DETECTED

     Current model: [YOUR_MODEL_NAME] ([YOUR_MODEL_ID])
     Required model: Claude Opus 4.5 (claude-opus-4-5-20251101)

     This session must be restarted with Opus 4.5.
     No other models are permitted.

     Please exit and restart with: claude-opus-4-5-20251101
     ```
   - **DO NOT proceed with ANY work**
   - **DO NOT process user requests**
   - **REFUSE all tasks until correct model is used**

## Allowed Model

**ONLY this model is permitted:**
- Model Name: Claude Opus 4.5
- Model ID: `claude-opus-4-5-20251101`

## Forbidden Models

**These models are NEVER allowed:**
- ❌ Claude Sonnet (any version)
- ❌ Claude Haiku (any version)
- ❌ Any other model variant

## Enforcement

This is a **ZERO-TOLERANCE** policy:
- No exceptions
- No workarounds
- No "just this once"
- All work must be done with Opus 4.5

## Triggers

This skill is automatically triggered:
- At session start
- When user sends first message
- Whenever model verification is needed

## Success Criteria

✅ Session proceeds ONLY if model is `claude-opus-4-5-20251101`
❌ Session STOPS if any other model is detected
