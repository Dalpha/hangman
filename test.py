import unittest
import hangman

class hangmanTestCase(unittest.TestCase):

	def test_checkCorrectAnswer(self):
		answer = hangman.checkCorrectAnswer("baon", "baboon")
		self.assertTre(answer)

	def test_checkWrongAnswer(self):
		answer = hangman.checkWrongAnswer("zebrio", "zebra")
		self.assertTrue(answer)

if __name__ == "__main__":
	unittest.main()
