x = 9763

w_ys = {
    805: 5462,
    1112: 7545,
    880: 5971,
    319: 2165,
    425: 2884,
    295: 2002,
    136: 923,
    189: 1282,
    314: 2131,
    722: 4899
}


a_min = 0
a_max = float('inf')

for w, y in w_ys.items():
    denom = x * w
    lo = (y - 0.5) / denom
    hi = (y + 0.5) / denom

    print(f"w={w}, y={y}  =>  a ∈ [{lo:.10f}, {hi:.10f})")

    a_min = max(a_min, lo)
    a_max = min(a_max, hi)

print(f"定义 y = x * w * a")
print(f"\n最终交集: a ∈ [{a_min:.10f}, {a_max:.10f})")
print(f"\n最终交集: 1 / a ∈ [{1 / a_min:.10f}, {1 / a_max:.10f})")