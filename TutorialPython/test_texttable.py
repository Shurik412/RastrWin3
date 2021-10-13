import termtables as tt

string = tt.to_string(
    [["Alice", 24], ["Bob", 19]],
    header=["Name", "Age"],
    style=tt.styles.ascii_thin_double,
    # alignment="ll",
    # padding=(0, 1),
)
print(string)
