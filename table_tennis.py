class TableTennisClub:
    """A class representing a table tennis club, consisting of many members"""

    def __init__(self):
        self.members = []

    def add_member(self, member):
        """Add a member to the club"""
        self.members.append(member)

    def __str__(self):
        """Automatic string conversion: Print all members"""
        output = ""
        for member in self.members:
            output += str(member)
            output += "\n"
        return output


class TableTennisPlayer:
    """A class representing a table tennis club member"""

    def __init__(self, name, has_table=False):
        """Create a TableTennisPlayer object. Arguments:
        name: The name of the member
        has_table: Whether the member owns a table tennis board (default False)
        """
        self.name = name
        self.has_table = has_table

    def __str__(self):
        """Automatic string conversion: Print member information"""
        output = f"{self.name}"

        if self.has_table:
            output += " has a table"
        else:
            output += " does not have a table"

        return output


class RatedPlayer(TableTennisPlayer):
    """A class representing a table tennis club member who participates in tournaments"""

    def __init__(self, name, rating, has_table=False):
        """Create a TableTennisPlayer object. Arguments:
        name: The name of the member
        rating: The player's tournament rating
        has_table: Whether the member owns a table tennis board (default False)
        """
        # Delegate most initialization to the parent class's __init__() method
        super().__init__(name, has_table)

        # At this point, name and has_table have been initialized.
        # Now, initialize the attributes that makes a RatedPlayer unique
        self.rating = rating

    def __str__(self):
        """Automatic string conversion: Print member information"""

        # Delegate most string conversion to the parent class's __str__() method
        output = super().__str__()

        # At this point, our output variable contains a string representation of
        # a TableTennisPlayer. We have the opportunity to add additional information
        # unique to a Rated Player
        output += f" rating {self.rating}"
        return output


if __name__ == "__main__":
    # Main program: Ask user to input table tennis club members
    # (similar to the square footage calculator)

    # Create a TableTennisClub object
    club = TableTennisClub()

    while True:
        # Get basic player information
        name = input("Player name: ")
        has_table = input("Has a table? (y/n)")

        # Convert input string into Boolean
        if has_table == "y":
            has_table = True
        else:
            has_table = False

        # The most important question here: the answer determines
        # whether we will create a TableTennisPlayer object or a
        # RatedPlayer object:
        is_rated = input("Plays competitively? (y/n)")

        if is_rated == "y":
            # If the user states that the new member plays competitively, we will
            # create a RatedPlayer object. Since RatedPlayer objects require
            # a rating, we must ask the user for additional input:
            rating = int(input("Rating? "))

            # Create a RatedPlayer object and add it to the club
            player = RatedPlayer(name, rating, has_table)
            club.add_member(player)
        else:
            # If the user states that the new member does not play competitively,
            # then we already have enough information to create a basic
            # TableTennisPlayer object. Create it and add it to the club
            player = TableTennisPlayer(name, has_table)
            club.add_member(player)

        # If the user declines to add another player, we exit the loop
        another = input("Add another? (y/n)")
        if another == "n":
            break
        
    print()

    # Final output: Print the club roster. Notice (depending on input) that some
    # players have a rating and some don't, but in all cases there is only a
    # __str__() method being called. This is polymorphism.
    print(club)