Feature: Music

	Scenario: try to win
		Given I have guess the melody game
		When I have entered number '3' as number of melody
		Then I lose the game