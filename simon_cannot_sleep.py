hh, mm = map(int, input().split(":"))
time = hh + mm/60

# The first 1 counts the overlap at 00:00
# The formula (time * (1-1/12)) was taken after a little googling
# The int() is used to round down the value.
n = int(1 + time * ( 1 - 1/12))
print(n)
