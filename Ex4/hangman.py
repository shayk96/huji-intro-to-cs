###########################################################
# FILE : ex4.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex4 2020
# DESCRIPTION: a little program that lets you play hangman
###########################################################
import hangman_helper


MSG_WRONG_INPUT = "wrong input!"
MSG_LETTER_CHOSEN_BEFORE = "Letter chosen before, choose another"
MSG_SEE_WHAT_YOU_GOT = "let's see what you got"
MSG_WIN = "Congratulations, you won!"
MSG_LOSE = 'sorry! better luck next time, the word was: '


def update_word_pattern(word, pattern, letter):
    """
    compares the letter to the word and changes the pattern accordingly
    :param word: the word the player needs to uncover
    :param pattern: the pattern masking the word
    :param letter: the letter the player chose
    :return: the updated pattern
    """
    pattern = list(pattern)
    for i in range(len(word)):
        if letter == word[i]:
            pattern[i] = letter
    pattern = "".join(pattern)
    return pattern


def char(guess, points, word, pattern, wrong_guess_lst, msg):
    """
    handles the game phase when the user chooses a letter and checks the
    validity of the user input
    :param guess: the current guess
    :param points: the current points owned by the user
    :param word: the word the user trying to discover
    :param pattern: the current pattern
    :param wrong_guess_lst: the list containing letters the user chose than not
    in the word
    :param msg: the message the user gets
    :return: the updated versions of the parameters
    """
    if len(guess[1]) > 1 or ord(guess[1]) not in range(97, 123) \
            or guess[1] == " " or guess[1] in pattern:
        msg = MSG_WRONG_INPUT
        points += 1
    else:
        pattern = update_word_pattern(word, pattern, guess[1])
        if guess[1] not in pattern:
            if guess[1] not in wrong_guess_lst:
                wrong_guess_lst.append(guess[1])
            else:
                msg = MSG_LETTER_CHOSEN_BEFORE
                points += 1
        else:
            n = pattern.count(guess[1])
            points += n * (n + 1) // 2
            msg = MSG_SEE_WHAT_YOU_GOT
    return points, pattern, wrong_guess_lst, msg


def lyric(guess, points, word, pattern):
    """
    handles the game phase when the user chooses a word
    :param guess: the current guess
    :param points: the current points owned by the user
    :param word: the word the user trying to discover
    :param pattern: the current pattern
    :return: the updated versions of points and pattern
    """
    if guess[1] == word:
        n = pattern.count('_')
        points += n * (n + 1) // 2
        pattern = word
    return points, pattern


def end_game(points, word, pattern, wrong_guess_lst):
    """
    handles the end game phase, whereas the user won or lost
    :param points: the current points owned by the user
    :param word: the word the user trying to discover
    :param pattern: the current pattern
    :param wrong_guess_lst: the list containing letters the user chose that are
    not in the word
    """
    if pattern == word:
        msg = MSG_WIN
        hangman_helper.display_state(pattern, wrong_guess_lst, points, msg)
    if pattern != word:
        msg = MSG_LOSE + word
        hangman_helper.display_state(pattern, wrong_guess_lst, points, msg)


def word_fits_pattern(word, pattern):
    """
    checks if the word is in the right length and has the right letters
    :param word: word being checked
    :param pattern: the current pattern
    :return: True if the word is an option , else False
    """
    if len(word) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] != "_":
            if pattern[i] != word[i]:
                return False
            if pattern.count(pattern[i]) != word.count(word[i]):
                return False
    return True


def wrong_guess_in_word(word, wrong_guess_lst):
    """
    checks if the word containing a wrong guess letter
    :param word: word being checked
    :param wrong_guess_lst: wrong guess
    :return: True of the word containing a wrong guess, else False
    """
    for guess in wrong_guess_lst:
        if guess in word:
            return True
    return False


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    creates a list of possible words that can be the right word
    :param words: a list of words
    :param pattern: the current pattern
    :param wrong_guess_lst: letters than are not in the correct word
    :return: a list of possible words
    """
    matches = []
    for current_word in words:
        if word_fits_pattern(current_word, pattern) and \
                not wrong_guess_in_word(current_word, wrong_guess_lst):
            matches.append(current_word)
    number_of_suggestions = len(matches)
    if number_of_suggestions > hangman_helper.HINT_LENGTH:
        matches_cut = []
        for i in range(hangman_helper.HINT_LENGTH):
            matches_cut.append(matches[i*number_of_suggestions //
                                       hangman_helper.HINT_LENGTH])
        return matches_cut
    return matches


def run_single_game(words_list, score):
    """
    runs the game a single time
    :param words_list: a list the word to be discovered get chosen from
    :param score: the starting score of the player
    :return: the end score of the player
    """
    word = hangman_helper.get_random_word(words_list)
    pattern = '_' * len(word)
    wrong_guess_lst = []
    points = int(score)
    msg = MSG_SEE_WHAT_YOU_GOT
    while pattern != word and points != 0:
        hangman_helper.display_state(pattern, wrong_guess_lst, points, msg)
        guess = hangman_helper.get_input()
        points -= 1

        if guess[0] == hangman_helper.LETTER:
            points, pattern, wrong_guess_lst, msg = char(guess, points, word,
                                                         pattern,
                                                         wrong_guess_lst, msg)
        if guess[0] == hangman_helper.WORD:
            points, pattern = lyric(guess, points, word, pattern)
        if guess[0] == hangman_helper.HINT:
            matches = filter_words_list(words_list, pattern, wrong_guess_lst)
            hangman_helper.show_suggestions(matches)
    end_game(points, word, pattern, wrong_guess_lst)
    return points


def main():
    """
    starts the game and keeps going as long as the player wants
    """
    words = hangman_helper.load_words()
    counter = 1
    points = hangman_helper.POINTS_INITIAL
    while points >= 0:
        points = run_single_game(words, points)
        if points > 0:
            msg = 'number of games played: {0} current points: {1}, Want ' \
                    'to try your luck again?'.format(str(counter), str(points))
            if hangman_helper.play_again(msg):
                counter += 1
                continue
            else:
                break
        if points == 0:
            msg = "number of games played until defeated: " + str(counter) + \
                  " ,try again? "
            if hangman_helper.play_again(msg):
                points = hangman_helper.POINTS_INITIAL
            else:
                break


if __name__ == '__main__':
    main()