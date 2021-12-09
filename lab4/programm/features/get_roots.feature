Feature: get_roots function

  Scenario: test no roots
      Given A = 1, B = 2, C = 3
      When get_roots run
      Then roots array is empty

  Scenario: test one root
     Given A = 1, B = 1, C = 0
     When get_roots execute1
     Then roots is [0]

  Scenario: test two root
     Given A = 1, B = -2, C = -8
     When get_roots execute2
     Then roots are [-2, 2]

  Scenario: test three root
     Given A = 1, B = -1, C = 0
     When get_roots execute3
     Then roots are [-1, 0, 1]

  Scenario: test four root
     Given A = 4, B = -5, C = 1
     When get_roots execute4
     Then roots are [-1, 1, 0.5, -0,5]

