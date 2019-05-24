Feature: Music

	Scenario: try to win
		Given I have guess the music game
		And I have one music in variants
		And I have current music
		When I have entered number '3' as number of melody
		Then I lose the game

	Scenario: try to win
		Given I have guess the music game
		And I have one music in variants
		And I have current music
		When I have entered number '1' as number of melody
		Then I win the game