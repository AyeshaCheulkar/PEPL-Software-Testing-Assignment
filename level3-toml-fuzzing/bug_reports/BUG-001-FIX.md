# BUG-001 Fix Report: Backspace String Serialization

## 1. Bug Summary

The TOML encoder in `toml==0.10.2` incorrectly handles backspace characters (`\x08`) during string serialization.

Two behaviours were identified:
- A string containing only a backspace causes an `IndexError`.
- A string containing ordinary text followed by a backspace is serialized incorrectly, resulting in data loss.

## 2. Original Reproduction

```python
import toml

data = {"A": ["\x08"]}
print(toml.dumps(data))
```

The original encoder raises:

`IndexError: list index out of range`

Another reproduction:

```python
data = {"A": ["0\x08"]}
print(toml.dumps(data))
```

The original encoder does not preserve the original backspace character.

## 3. Expected Behaviour

The encoder should serialize backspace using the valid TOML basic-string escape `\b` and preserve the original Python string when parsed again.

## 4. Root Cause

The defect was identified in `toml/encoder.py`, inside `_dump_str()`.

The original implementation uses string splitting and reconstruction around hexadecimal escape sequences. This logic incorrectly handles certain backspace-containing strings.

## 5. Proposed Fix

The copied encoder was updated to use JSON string escaping, with an additional replacement for the DEL character:

```python
def _dump_str(v):
    """Serialize a Python string as a valid TOML basic string."""
    return json.dumps(v, ensure_ascii=False).replace("\x7f", "\\u007f")
```

The `json` module was imported in the copied encoder.

## 6. Regression Testing

Tested:
- Backspace characters
- Null and escape characters
- DEL character
- C1 control characters (U+0080–U+009F)
- Quotes and backslashes
- Newlines
- Non-ASCII text

Both the patched TOML parser and Python's `tomllib` were used for verification.

## 7. Test Results

- Both original BUG-001 reproductions were confirmed as expected failures.
- Targeted string serialization tests passed.
- Additional 32 control-character checks passed.
- Round-trip property testing passed.
- TOML compatibility testing passed.

## 8. Conclusion

The proposed encoder modification resolves the observed backspace serialization failures in the tested cases and preserves the tested strings when serialized and parsed again.