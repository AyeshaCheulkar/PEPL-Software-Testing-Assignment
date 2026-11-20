
# BUG-002 Fix: Reject Incomplete TOML Arrays

## Original Bug

The `toml==0.10.2` decoder accepted incomplete arrays without a closing square bracket.

Example:

```toml
A = [1,
```

The original implementation incorrectly returned:

```python
{'A': [1]}
```

## Proposed Fix

File: `fixes/toml/decoder.py`

Method: `load_array()`

The following validation was added immediately after stripping whitespace:

```python
# BUG-002 FIX: Validate array boundaries
if not a.startswith('[') or not a.endswith(']'):
    raise ValueError("Invalid array: missing opening or closing bracket")
```

This checks that an array starts with `[` and ends with `]` before processing its contents.

## Before and After

| Input | Original implementation | Patched implementation |
|---|---|---|
| `[1]` | Accepted | Accepted |
| `[1, 2]` | Accepted | Accepted |
| `[]` | Accepted | Accepted |
| `[1,` | Incorrectly accepted | Rejected |
| `[1` | Incorrectly accepted | Rejected |
| `[1, 2` | Incorrectly accepted | Rejected |

## Regression Testing

Test file: `tests/test_bug_fixes.py`

The following tests were executed against the patched package:

- 3 valid array tests
- 3 incomplete array rejection tests

**Result: 6 passed in 0.46s**

## Verification

The Python package path was verified:

```text
level3-toml-fuzzing/fixes/toml/__init__.py
```

This confirms that the tests used the patched package rather than the original installed package.

## Conclusion

The proposed fix prevents the decoder from accepting arrays that are missing their opening or closing square brackets.

Valid array behaviour was preserved across the tested examples.

The patch is a proposed fix for the identified BUG-002 defect in `toml==0.10.2`.
