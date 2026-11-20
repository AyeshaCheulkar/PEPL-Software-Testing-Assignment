# BUG-003 Fix Report: Incomplete Inline Table Accepted

## 1. Bug Summary

The TOML parser accepts an incomplete inline table without a closing brace.

## 2. Original Reproduction

```python
import toml

document = "A = {"
print(toml.loads(document))
```

**Original output:**
```python
{'A': {}}
```

The parser accepts the malformed document instead of raising an error.

## 3. Expected Behaviour

The parser should reject an inline table that does not have a closing `}`.

Python's standard library `tomllib` correctly rejects this input.

## 4. Root Cause

The issue was identified in `toml/decoder.py`, inside the `load_value()` function.

The original implementation checked whether the value started with `{`, but did not verify that it ended with `}` before calling `load_inline_object()`.

## 5. Proposed Fix

Added a closing-brace validation:

```python
elif v[0] == '{':
    if not v.endswith('}'):
        raise ValueError("Invalid inline table: missing closing brace")

    inline_object = self.get_empty_inline_table()
    self.load_inline_object(v, inline_object)
    return (inline_object, "inline_object")
```

## 6. Regression Testing

Valid inline tables tested:
- `A = {}`
- `A = {a = 1}`

Invalid inline tables tested:
- `A = {`
- `A = {a = 1`

## 7. Test Results

All 4 BUG-003-specific regression cases passed.

The broader test suite also passed:
- Round-trip property test
- Valid TOML differential test
- Invalid TOML differential test
- TOML compatibility test

## 8. Conclusion

The proposed fix prevents incomplete inline tables from being accepted while preserving the tested valid inline-table cases.