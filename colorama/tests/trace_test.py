# BSD 3-Clause license, see LICENSE.txt file.
from unittest import TestCase, main

from ..ansi import Fore


class TraceTest(TestCase):

    def testForegroundCodes(self):
        """REQ-101 AC1: Fore.RED is ESC[31m and Fore.RESET is ESC[39m."""
        self.assertEqual(Fore.RED, '\033[31m')
        self.assertEqual(Fore.RESET, '\033[39m')


if __name__ == '__main__':
    main()
