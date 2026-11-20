
import pytest
import toml
import tomllib
# BUG-002 FIX: Valid arrays must still work
@pytest.mark.parametrize(
    "document, expected",
    [
        ("A = [1]", {"A": [1]}),
        ("A = [1, 2]", {"A": [1, 2]}),
        ("A = []", {"A": []}),
    ]
)
def test_bug_002_fix_valid_arrays(document, expected):
    result = toml.loads(document)

    assert result == expected


# BUG-002 FIX: Incomplete arrays must be rejected
@pytest.mark.parametrize(
    "document",
    [
        "A = [1,",
        "A = [1",
        "A = [1, 2",
    ]
)
def test_bug_002_fix_invalid_arrays(document):
    with pytest.raises(toml.TomlDecodeError):
        toml.loads(document)
# BUG-001 FIX: Backspace and special-character serialization

@pytest.mark.parametrize(
    "value",
    [
        "\x08",
        "0\x08",
        "hello",
        'hello "world"',
        "C:\\Users\\Test",
        "line1\nline2",
        "\x00",
        "\x1b",
        "\x7f",
        "café",
    ]
)
def test_bug_001_fix_string_serialization(value):
    data = {"A": [value]}

    toml_text = toml.dumps(data)

    # Check round-trip using the patched parser
    result = toml.loads(toml_text)
    assert result == data

    # Check compatibility using Python's independent TOML parser
    reference_result = tomllib.loads(toml_text)
    assert reference_result == data

# BUG-003 FIX: Valid inline tables must still work
@pytest.mark.parametrize(
    "document, expected",
    [
        ("A = {}", {"A": {}}),
        ("A = {a = 1}", {"A": {"a": 1}}),
    ]
)
def test_bug_003_fix_valid_inline_tables(document, expected):
    result = toml.loads(document)
    assert result == expected


# BUG-003 FIX: Incomplete inline tables must be rejected
@pytest.mark.parametrize(
    "document",
    [
        "A = {",
        "A = {a = 1",
    ]
)
def test_bug_003_fix_invalid_inline_tables(document):
    with pytest.raises(toml.TomlDecodeError):
        toml.loads(document)