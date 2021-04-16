
import random


POSSIBLE_DICES = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)


def roll_the_dice(dice_code):
    """
    Calculate dice roll from dice pattern.
    :param str dice_code: dice pattern ex. `7D12-5`
    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))


def calculate_points(points):
    """Calculate points.
    :param int points:
    :rtype: int
    :return: new_points
    """
    roll = roll_the_dice("2D6")
    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points


def game_2001():
    """2001 game."""
    user_points = 0
    computer_points = 0

    input("Press ENTER to roll the dice")
    user_points += roll_the_dice("2D6")
    computer_points += roll_the_dice("2D6")

    while user_points < 2001 and computer_points < 2001:
        print(f"User points: {user_points}\nComputer points: {computer_points}")
        input("Press ENTER to roll the dice")
        user_points = calculate_points(user_points)
        computer_points = calculate_points(computer_points)

    print(f"User points: {user_points}\nComputer points: {computer_points}")
    if computer_points > user_points:
        print("Computer win!")
    elif user_points > computer_points:
        print("User win!")
    else:
        print("Draw")


if __name__ == '__main__':
    game_2001()