# IBTestMaker

I tutor students studying math and physics at high school and early university level! A significant section of students are in IB Math under the SL curriculum.

I particularly like using [Christos Nikolaidis'](https://www.christosnikolaidis.com/en/maa/) problem sets for practice tests and assignments.

I made this repo to streamline test-making so I can help my students prepare for exams and tests in a similar environment and difficulty.

# How it works

**Parser**: Scrapes PDF files from the website to make a question bank. It stores these questions based on marks, calculator use and topic.

**Test Maker**: Takes an input mark scheme, and pulls questions from the bank to make unique tests with the appropriate amount of calculator and non-calculator questions.

*Solving the full optimization is an NP-complete problem! The coin change problem is a great approximation that I use to make the tests within a certain tolerance.*
