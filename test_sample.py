from weather import process

def test_one():

    assert process("Cass Field") == "Briggsdale"
    assert process("Lowell Field") == "Anchor Point"
    assert process("River Oak Airport") == "Okeechobee"
    assert process("Hammer Airport") == "Polo"