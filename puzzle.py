from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A_statement0 = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Biconditional(AKnight, A_statement0),
    Biconditional(AKnave, Not(A_statement0)),
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_statement1 = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, A_statement1),
    Biconditional(AKnave, Not(A_statement1)),
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_statement2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_statement2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, A_statement2),
    Biconditional(AKnave, Not(A_statement2)),
    Biconditional(BKnight, B_statement2),
    Biconditional(BKnave, Not(B_statement2)),
)



# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AsaidKnight = Symbol("A said 'I am a knight'")
AsaidKnave  = Symbol("A said 'I am a knave'")
A_said_exactly_one = And(Or(AsaidKnight, AsaidKnave), Not(And(AsaidKnight, AsaidKnave)))
A_statement3_true = Or(And(AsaidKnight, AKnight), And(AsaidKnave, AKnave))
B_claim_A_said_knave = AsaidKnave
B_claim_C_is_knave   = CKnave

knowledge3 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),
    A_said_exactly_one,
    Biconditional(AKnight, A_statement3_true),
    Biconditional(AKnave, Not(A_statement3_true)),
    Biconditional(BKnight, And(B_claim_A_said_knave, B_claim_C_is_knave)),
    Biconditional(BKnave, And(Not(B_claim_A_said_knave), Not(B_claim_C_is_knave))),
    Biconditional(CKnight, AKnight),
    Biconditional(CKnave, Not(AKnight)),
)




def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
