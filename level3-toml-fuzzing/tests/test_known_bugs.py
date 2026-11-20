
import pytest
import toml


# BUG-001: Backspace serialization defect
@pytest.mark.parametrize(
    "data",
    [
        {"A": ["\x08"]},
        {"A": ["0\x08"]}
    ]
)
@pytest.mark.xfail(
    reason="BUG-001: Backspace serialization defect",
    strict=True
)
def test_bug_001_backspace_serialization(data):
    toml_text = toml.dumps(data)
    result = toml.loads(toml_text)

    assert result == data


# BUG-002: Parser accepts an incomplete array
@pytest.mark.xfail(
    reason="BUG-002: Parser accepts array without closing bracket",
    strict=True
)
def test_bug_002_incomplete_array():
    document = "A = [1,"

    with pytest.raises(toml.TomlDecodeError):
        toml.loads(document)
