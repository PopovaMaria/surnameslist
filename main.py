from surnames_repositoty import SurnameRepository
from input_stategies.console_input_stategy import ConsoleInputStrategy


if __name__ == '__main__':
    input_strategy = ConsoleInputStrategy()
    surnames_repository = SurnameRepository(input_strategy)

    surnames_repository.add()
    surnames_repository.change()
    surnames_repository.pop()

    print(surnames_repository)
