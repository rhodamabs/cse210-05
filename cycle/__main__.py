import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # Create two snakes, gets their position and color
    cycle = Cycle(Point(int(constants.MAX_X - 645), int(constants.MAX_Y / 2)))
    cycle1 = Cycle(Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
    cycle.set_color(constants.GREEN)
    cycle1.set_color(constants.RED)
    #snake_one_name = input("Please enter player 1 name: ")
    #snake_two_name = input("Please enter player 2 name: ")
    cycle_name = "You"
    cycle1_name = "Opponent"
    cycle.set_name(cycle_name)
    cycle1.set_name(cycle1_name)


    # create the cast

    # player 1 (You)
    cast = Cast()
    score1 = Score()
    score1.add_points(5)
    score1.set_name(cycle_name)
    cast.add_actor("cycle", cycle)
    cast.add_actor("score1", score1)
    score1.set_position(Point(constants.MAX_X+150, 10))

    # player 2 (Opponent)
    score2 = Score()
    score2.add_points(5)
    score2.set_name(cycle1)
    cast.add_actor("cycle1", cycle1)
    cast.add_actor("score2", score2)
    score2.set_position(Point(constants.MAX_X-200, 10))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()