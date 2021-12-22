Feature: get_roots function

  Scenario: test no winner
      Given player1 cards: 2 clubs, 10 hearts; player2 cards: 2 hearts, king diamonds
      When check_finish run
      Then there is no winner

  Scenario: test any winner
     Given player1 cards: a clubs, 10 hearts; player2 cards: 2 hearts, king diamonds
     When check_finish run_
     Then winner is player1

  Scenario: test new card
     Given gamer has no cards
     When gamer gets clubs king
     Then gamers cards are: clubs king

  Scenario: test count sum
     Given gamer has no cards_
     When gamer gets clubs king, diamonds king, hearts king
     Then the sum is 18