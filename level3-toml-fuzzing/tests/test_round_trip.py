import toml
from hypothesis import given, strategies as st
import string
# Generate basic scalar values
scalar_values = st.one_of(
    st.integers(
        min_value=-(2**63),
        max_value=2**63 - 1
    ),
    st.floats(
        allow_nan=False,
        allow_infinity=False
    ),
    st.text(
        alphabet=string.ascii_letters + string.digits + " _-",
        max_size=20
    ),
    st.booleans(),
    st.dates(),
    st.datetimes(timezones=st.none()),
    st.times()
)
# Generate lists
list_values = st.one_of(
    st.lists(st.integers(), max_size=5),
    st.lists(st.text(max_size=10), max_size=5),
    st.lists(st.booleans(), max_size=5),
    st.lists(
        st.floats(
            allow_nan=False,
            allow_infinity=False
        ),
        max_size=5
    )
)
# Generate dictionaries with different data types
simple_data = st.dictionaries(
    keys=st.text(
        alphabet=string.ascii_letters,
        min_size=1,
        max_size=10
    ),
    values=st.one_of(
        scalar_values,
        list_values
    ),
    max_size=10
)
# Property 1: Round-trip testing
@given(data=simple_data)
def test_toml_round_trip(data):
    toml_text = toml.dumps(data)
    result = toml.loads(toml_text)
    assert result == data
