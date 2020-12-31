x = input(">")
print("<h1>")
for i,char in enumerate(x):
    i+=1
    print(f'\t<span class="char{i}">{char}</span>')
print("</h1>")


print("\n\n")
gap = 360//len(x)
for i,char in enumerate(x):
    i+=1
    print(f".char{i} {{ transform: translate(-50%, -50%) rotate({i*gap}deg); }}")
