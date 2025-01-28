"""Planning a cozy tea party."""

__author__: str = "730648394"


def main_planner(guests: int) -> None:
    """Bringing all functions together that produces printed output as entrypoint."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """A function to compute the number of tea bags needed based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Computes number of treats needed based on guests who will drink."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computing cost of tea bags and treats combined."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
