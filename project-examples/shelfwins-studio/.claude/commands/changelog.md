# Add Changelog Entry

Add a new entry to CHANGELOG.md.

## Arguments
$ARGUMENTS = changelog message (e.g., "Add ProductLibrary modal with grid layout")

## Instructions

1. Read current CHANGELOG.md to understand the format

2. Get today's date in format: YYYY-MM-DD

3. Determine the entry type based on the message:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `refactor:` for code improvements
   - `perf:` for performance improvements
   - `docs:` for documentation
   - `style:` for UI/styling changes

4. Add the entry near the top of the file, under the most recent section or create a new dated section

5. Format:
   ```markdown
   ## [Date] or add to existing date section
   - **type**: message
   ```

6. Confirm the entry was added

Changelog message: $ARGUMENTS
