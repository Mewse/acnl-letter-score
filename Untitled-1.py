
"""
    Checks as defined in article: https://www.polygon.com/2018/8/7/17660344/animal-crossing-letter-system-game-design-explained
    Takes a string and returns the calculated scoring
    >100 Is considered to be good
    <50 Is considered to be bad
"""
import logging

logging.basicConfig()
logger = logging.getLogger("ACNL")



def score_message(str:message) -> int:
    score = 0
    score += checkPunctuation(message)
    score += check_trigrams(message)
    score += check_capital(message)
    score += check_for_repitition(message)
    score += check_space_ratio(message)
    score += check_length(message)
    score += check_spaces(message)
    return score

# A
def checkPunctuation(str:message) -> int:
    score = 0
    # Check for use of punctuation
    # Check for capitals
    logger.info("Checking punctuation for string: %s" % message)
    # Find all punctuation indices
    punc_ids = [id for punc,id in enumerate(message) if punc.isalnum()]
    logger.info("Found punctuation at indexes: %s" % punc_ids)
    for id in punc_ids:
        # Check the 3 characters after the punctuation for a capital
        found_cap = False
        for i in range(3):
            if len(message) <= id+i:
                # End of string
                break
            else:
                if message[id+i].isupper():
                    foundCap = True
                    break;
        logger.info("%s capital after char %s at index %s" % (found_cap ? "Found" : "Did not find", message[id], id))
        if found_cap:
            score += 10
        else:
            score -= 10
        logger.info("New score: %s" % score)
    # Check final character for punctuation
    if len(message) > 0 and message[:-1] in ["?", ".", "!"]:
        logger.info("Final character is punctuation")
        score += 20

    logger.info("Returned score: %s" score)c
    return score
    

#B
def check_trigrams(str:message) -> int:
    pass

#C
def check_capital(str:message) -> int:
    # Check first letter is a capital
    pass

#D
def check_for_repitition(str:message) - > int:
    # Check for 3 or more consecutive letters

#E
def check_space_ratio(str:message) -> int:
    # <=2:10 loses 20 points
    pass

#F
def check_length(str:message) -> int:
    pass

#G
def check_spaces(str:message) -> int:
    pass