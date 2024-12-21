from pathlib import Path

def load_input(day: int) -> str:
    input_file = Path(__file__).parent.parent / 'input' / f'input_{day}.txt'
    return input_file.read_text(encoding='utf-8')

def solve(input_data: str) -> int:
    return 5

def main() -> None:
    day = int(Path(__file__).stem.split('_')[1])
    input_data = load_input(day)
    answer = solve(input_data)
    print(answer)

if __name__ == '__main__':
    main()
