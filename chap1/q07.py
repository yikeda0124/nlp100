def make_sentence(x: int, y: str, z: float) -> str:
    return str(x) + "時の" + y + "は" + str(z)

if __name__ == '__main__':
    print(make_sentence(12, "気温", 22.4))