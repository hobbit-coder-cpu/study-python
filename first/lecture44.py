# 44강. join() 함수

print("*"*10)
print(f"""
    입력한 문자열
    """)
print("*"*10)


print("*"*10)
print(f"""\
    입력한 문자열\
    """)
print("*"*10)

print(
    f"입력한 문자열\n"
    f"짝수"
)
print("\n".join([
    f"입력한 문자열",
    f"짝수"    
]))

# join() 
print("\n".join(["A", "B", "C"]))



print(
    "A"
    "B"
    "C"
)

d = [
    [3, 2, 4, 5],
    [1, 2, 2, 6],
    [-1. -2, 2, 4]
]

print("\n".join([
    f"{d[0]}",
    f"{d[1]}",
    f"{d[2]}"
]))

print(",".join(["hello", "world"]))
