from looping import *

def test_happy_new_year():
    """Test happy_new_year function by capturing printed output"""
    import sys
    from io import StringIO
    
    # Capture print statements
    captured_output = StringIO()
    sys.stdout = captured_output
    
    happy_new_year()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Get the output
    output = captured_output.getvalue().strip().split('\n')
    
    # Check first 10 lines are 10 down to 1
    for i in range(10):
        assert output[i] == str(10 - i)
    
    # Check last line is "Happy New Year!"
    assert output[10] == "Happy New Year!"
    
    print("✓ happy_new_year tests passed")

def test_square_integers():
    """Test square_integers function"""
    assert square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert square_integers([-1, -2, -3]) == [1, 4, 9]
    assert square_integers([0]) == [0]
    assert square_integers([]) == []
    print("✓ square_integers tests passed")

def test_fizzbuzz():
    """Test fizzbuzz function by capturing printed output"""
    import sys
    from io import StringIO
    
    # Capture print statements
    captured_output = StringIO()
    sys.stdout = captured_output
    
    fizzbuzz()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Get the output
    output = captured_output.getvalue().strip().split('\n')
    
    # Test specific positions (remember indices are 0-based)
    # Position 2 (value 3) should be "Fizz"
    assert output[2] == "Fizz"
    # Position 4 (value 5) should be "Buzz"
    assert output[4] == "Buzz"  
    # Position 14 (value 15) should be "FizzBuzz"
    assert output[14] == "FizzBuzz"
    # Position 98 (value 99) should be "Fizz"
    assert output[98] == "Fizz"
    
    print("✓ fizzbuzz tests passed")

if __name__ == "__main__":
    test_happy_new_year()
    test_square_integers()
    test_fizzbuzz()
    print("\n🎉 All tests passed!")