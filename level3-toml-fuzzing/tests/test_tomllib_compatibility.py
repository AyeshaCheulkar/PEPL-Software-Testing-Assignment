
import toml
import tomllib

from hypothesis import given, strategies as st
import string


# Generate Python dictionaries
simple_data = st.dictionaries(
    keys=st.text(
        alphabet=string.ascii_letters,
        min_size=1,
        max_size=10
    ),
    values=st.one_of(
        st.integers(
            min_value=-(2**63),
            max_value=2**63 - 1
        ),
        st.text(
            alphabet=string.ascii_letters + string.digits + " _-",
            max_size=20
        ),
        st.booleans()
    ),
    max_size=10
)


# Property 2: Compatibility with tomllib
@given(data=simple_data)
def test_toml_dumps_compatible_with_tomllib(data):

    # Generate TOML using toml library
    toml_text = toml.dumps(data)

    # Parse the generated TOML using tomllib
    result = tomllib.loads(toml_text)

    # Verify that the original data is preserved
    assert result == data
