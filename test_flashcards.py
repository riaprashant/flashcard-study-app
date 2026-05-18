from flashcard_challenge import FlashCard


def test_correct_answer():
    card = FlashCard("2 + 2", "4")
    assert card.check_answer("4") is True


def test_wrong_answer():
    card = FlashCard("Capital of France", "Paris")
    assert card.check_answer("London") is False


def test_case_insensitive():
    card = FlashCard("Color", "Blue")
    assert card.check_answer("blue") is True


def test_extra_spaces():
    card = FlashCard("Planet", "Earth")
    assert card.check_answer("   earth   ") is True
