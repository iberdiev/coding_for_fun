
def comp10001huxxy_score(cards):
    """
    This function takes a single argument in the format of a list consisting of
    two letter strings and takes the first element of each string, which
    corresponds to a value and adds up the values to indicate a score for the
    combined cards
    """

    # Dictionary assigning the values of each card
    my_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

    counter = 0

    # Case of empty list, the function should return 0
    if cards == []:
        return 0

    # Selecting the first element of each two letter string in the cards list
    # and finding their corresponding values in my_dict. Counter is the score
    # for the combined cards
    for i in range(len(cards)):
        key = cards[i][0]
        value = my_dict[key]
        counter += value

    return counter

# Function checks if group is of a kind


def group_is_of_kind(group):
    values = [card[0] for card in group]
    return len(values) == values.count(values[0])

# Function that checks if group in a sequence


def group_is_a_run(group):
    scores = sorted([comp10001huxxy_score([card]) for card in group])
    return True if list(range(min(scores), max(scores) + 1)) else False

# Function that checks if run in alternate in color

def run_is_alternate_in_color(group):
    group = [[card, comp10001huxxy_score([card])] for card in group]
    group = sorted(group, key=lambda card: card[1])
    suits = {'red': 'SC', 'black': 'HD'}
    color_sequence = [('red' if card[0][1] in suits['red'] else 'black') for card in group]
    for i in range(len(color_sequence) - 1):
        if color_sequence[i] == color_sequence[i + 1]:
            return False
    return True

# Function checks if number of unique suits are equal to 4 for length of group

def group_of_kind_with_unique_suits(group):
    suits = set()
    for card in group:
        suits.add(card[1])
    return True if len(suits) in [4, len(group)] else False

# Function that checks if there are cards from 3 or more decks, which
# results to invalid case

def two_more_decks_used(groups):
    from collections import defaultdict
    d = defaultdict(int)
    for group in groups:
        for card in group:
            d[card] += 1
    for l in d:
        if d[l] > 2:
            return True
    return False

# Function that checks if the table contains valid groups

def comp10001huxxy_valid_table(groups):
    for group in groups:  # Check if each group contains more that 2 cards
        if len(group) < 3:
            return False
    if two_more_decks_used(groups):  # Check if used more than 2 decks
        return False
    for group in groups:
        if group_is_of_kind(group):
            if not group_of_kind_with_unique_suits(group):  # Check if group contains unique suits
                return False
        else:  # Check if run is alternate in color
            if not group_is_a_run(group) or not run_is_alternate_in_color(group):
                return False
    return True

# Function that checks if the number of plays are less then 7

def valid_number_of_moves(play_history, active_player):
    queue_str = ''.join([str(play[0]) for play in play_history]) + str(active_player)
    current = queue_str[0]
    count_current = 1
    for i in range(len(queue_str) - 1):
        if queue_str[i + 1] == current:
            count_current += 1
            if count_current == 7:
                return False
        else:
            count_current = 1
            current = queue_str[i + 1]
    return True

# Function that checks if the game in on oppenning turn based on play history

def is_openning_turn(play_history):
    play_sequence = [play[0] for play in play_history]
    i = 0
    while i < len(play_sequence) - 1:
        if play_sequence[i] == play_sequence[i + 1]:
            play_sequence.pop(i)
            continue
        else:
            i += 1
    return True if len(play_sequence) < 5 else False

# Functions that checks if the play is valid

def comp10001huxxy_valid_play(play, play_history, active_player, hand, table):
    """
    Arguments:
        - play = (play_player_id, play_status, play_instructions)
        - play_history = list of previous plays(play arguments)
        - active_player = play_player_id
        - hand = list of cards of active_player
        - table = list of lists, representing groups of cards
    """
    # if there is a history
    if play_history:
        # checking for max possible plays (1-6)
        if not valid_number_of_moves(play_history, active_player):
            return False
        # checking if first move of a player is playing card
        if play_history[-1][0] != active_player and play[1] != 1:
            return False
    # Checking if at the end of opening turn, there are cards with at least 24
    # points combined
    if is_openning_turn(play_history) and play[1] == 3:
        if sum([comp10001huxxy_score(group) for group in table]) < 24:
            return False
    # Returns False if wrong player makes the move
    if play[0] != active_player:
        return False
    # Returns False if card does not exist
    if play[2] and play[2][0] not in hand:
        return False
    # Returns False group does not exist
    if play[2] and (play[2][1] > len(table)):
        return False
    # handling the last move validation
    if play[1] == 3:
        # Returns False if no moves were made
        if not play_history:
            return False
        # Returns False if the user ends without making a move
        if play_history and play_history[-1][0] != active_player:
            return False
        # returns False if the table is not valid
        if not comp10001huxxy_valid_table(table):
            return False
    return True


def comp10001huxxy_play(play_history, active_player, hand, table):
    pass

# print(comp10001huxxy_play([(0, 1, ('KC', 0)), (0, 1, ('KC', 0)), (0, 1, ('KS', 0)), (0, 1, ('KH', 0)), (0, 1, ('KD', 0))], 0, ['3S', '8S', '4H', '2C', '6S', '5H', '8C'], [['KC', 'KC', 'KS', 'KH', 'KD']]))
# (0, 3, None)
