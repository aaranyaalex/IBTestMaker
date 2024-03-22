from myParser import Parser
from typing import List

class MathTest:
    """
    Constructor for different Math tests

    1. Tests the max amount of tests to be generate for given markscheme, and tolerance
    2. Even distribution of the marks (aka short and long questions)
    3. Constructs the tests and sends them to pdf with formatting

    """
    def __init__(self, data: Parser, num_tests: int, markscheme: List[int], tol=5) -> None:

        # run the tester for the values
        self.data = data
        self.params = [(num_tests, markscheme, tol)]
        self.indices = []

        self.check_params()
    
    def reset(self, num_tests, markscheme, tol=5):

        self.params = [(num_tests, markscheme, tol)]
        self.check_params()
        
    def check_params(self):
        # check that we can make tests with these vals

        #output results and ask for feedback
        pass

    def make(self):
        pass
    
    def review(self):
        pass
    
    def to_pdf():
        pass