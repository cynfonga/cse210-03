import constants
from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle 
from game.scripting.control_actors import DrawActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.directing.director import Director
from game.scripting.draw_actors_action import DrawActorsAction
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():
    cast=Cast()
    cast.add_actor("foods" Food())
    cast.add_actor("cycles",Cycle(constants.RED))
    cast.add_actor("cycles",Cycle(constants.GREEN))
    cast.add_actor("scores",Score())
    cast.add_actor("")


# start the game 
keyboard_service=KeyboardService()
video_service=VideoService()
script=Script()
script.add_action("input",ControlActorsAction(KeyboardService))
script.add_action("update",MoveActorsAction())
script.add_action("output", DrawActorsAction(VideoService))
director=Director(video_service)
director.start_gmae(cast,script)
if _name_ =="_main_":
    main()