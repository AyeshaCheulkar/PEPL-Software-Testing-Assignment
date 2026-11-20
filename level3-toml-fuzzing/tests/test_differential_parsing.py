
import toml
import tomllib
import string

from hypothesis import given, strategies as st


# Generate TOML keys
keys = st.text(
    alphabet=string.ascii_letters,
    min_size=1,
    max_size=8
)


# Generate valid TOML values as TEXT
toml_values = st.one_of(

    st.integers(
        min_value=-1000,
        max_value=1000
    ).map(str),

    st.booleans().map(
        lambda value: "true" if value else "false"
    ),

    st.text(
        alphabet=string.ascii_letters + " ",
        max_size=10
    ).map(
        lambda value: '"' + value + '"'
    )
)


# Generate valid TOML documents
valid_documents = st.dictionaries(
    keys=keys,
    values=toml_values,
    max_size=5
).map(
    lambda entries: "\n".join(
        f"{key} = {value}"
        for key, value in entries.items()
    )
)


# Generate deliberately invalid TOML documents
invalid_values = st.sampled_from([
    "tru",
    '"unterminated',
    "[1,",
    "01",
    "{"
])


invalid_documents = st.tuples(
    keys,
    invalid_values
).map(
    lambda item: f"{item[0]} = {item[1]}"
)


# Helper function to parse TOML
def parse_document(parser, document):

    try:
        return True, parser(document)

    except ValueError:
        return False, None


# Compare both parsers
def compare_parsers(document):

    toml_accepted, toml_result = parse_document(
        toml.loads, document
    )

    tomllib_accepted, tomllib_result = parse_document(
        tomllib.loads, document
    )

    # Both parsers must agree on acceptance
    assert toml_accepted == tomllib_accepted, (
        f"Acceptance mismatch!\n"
        f"Document: {document!r}\n"
        f"toml accepted: {toml_accepted}\n"
        f"tomllib accepted: {tomllib_accepted}"
    )

    # If both accept, results must match
    if toml_accepted:

        assert toml_result == tomllib_result, (
            f"Result mismatch!\n"
            f"Document: {document!r}\n"
            f"toml result: {toml_result!r}\n"
            f"tomllib result: {tomllib_result!r}"
        )


# Property 3A: Valid TOML documents
@given(document=valid_documents)
def test_valid_toml_parsers_agree(document):

    toml_accepted, _ = parse_document(
        toml.loads, document
    )

    tomllib_accepted, _ = parse_document(
        tomllib.loads, document
    )

    assert toml_accepted
    assert tomllib_accepted

    compare_parsers(document)


# Property 3B: Invalid TOML documents

@given(document=invalid_documents)
def test_invalid_toml_parsers_agree(document):

    # First verify that the reference parser rejects the document
    tomllib_accepted, _ = parse_document(
        tomllib.loads, document
    )

    assert not tomllib_accepted, (
        f"Invalid document generator produced valid TOML: {document!r}"
    )

    # Now compare both parsers
    compare_parsers(document)
