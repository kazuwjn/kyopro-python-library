# a^b (mod m) を O(log b) で計算する
def modpow(a, b, m):
  res = 1
  while b:
    if b & 1:
      res *= a
      res %= m
    a *= a
    a %= m
    b >>= 1
  return res