from datetime import datetime
def idade(y):
    if 67>=datetime.now().year-y>=18:
        return f"idade: {datetime.now().year-y}: Você vota"
    elif datetime.now().year-y>=68:
        return f"idade: {datetime.now().year-y}: OPCIONAL"
    else:
        return f"idade: {datetime.now().year-y}: Você não vota"

print(idade(int(input("ano do seu nascimento: "))))