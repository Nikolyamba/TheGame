import arcade
from arcade.gui import UIView

from models.player import Player
from models.resource import Resource


class GameWindow(UIView):
    def __init__(self):
        super().__init__()
        self.player_list = None
        self.player_sprite = None

    def setup(self):
        self.background_color = arcade.color.WHITE
        self.player_list = arcade.SpriteList()
        self.resource_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        wood = Resource("sprites/wood.png", "wood")
        wood.center_x = 800
        wood.center_y = 800
        self.resource_list.append(wood)

        metal = Resource("sprites/metal.png", "metal")
        metal.center_x = 400
        metal.center_y = 400
        self.resource_list.append(metal)

        food = Resource("sprites/meat.png", "food")
        food.center_x = 600
        food.center_y = 600
        self.resource_list.append(food)

    def on_update(self, delta_time):
        self.player_list.update(delta_time)
        self.resource_list.update(delta_time)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.resource_list)
        for resource in hit_list:
            if resource.resource_type == "wood":
                self.player_sprite.wood_values += 1
                self.player_sprite.player_weight += resource.weight
            elif resource.resource_type == "metal":
                self.player_sprite.metal_values += 1
                self.player_sprite.player_weight += resource.weight
            elif resource.resource_type == "food":
                self.player_sprite.food_values += 1
                self.player_sprite.player_weight += resource.weight
            resource.remove_from_sprite_lists()

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.resource_list.draw()
        arcade.draw_text(f"Wood: {self.player_sprite.wood_values}", 10, self.window.height - 20, arcade.color.BLACK, 14)
        arcade.draw_text(f"Metal: {self.player_sprite.metal_values}", 10, self.window.height - 40, arcade.color.BLACK, 14)
        arcade.draw_text(f"Food: {self.player_sprite.food_values}", 10, self.window.height - 60, arcade.color.BLACK, 14)
        arcade.draw_text(f"Weight: {self.player_sprite.player_weight}", 10, self.window.height - 80, arcade.color.BLACK, 14)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            from windows.main_menu_window import MainMenu
            self.window.show_view(MainMenu())
        elif key == arcade.key.W:
            self.player_sprite.change_y = self.player_sprite.movement_speed
            self.player_sprite.texture = self.player_sprite.textures_dict["up"]
        elif key == arcade.key.S:
            self.player_sprite.change_y = -self.player_sprite.movement_speed
            self.player_sprite.texture = self.player_sprite.textures_dict["down"]
        elif key == arcade.key.A:
            self.player_sprite.change_x = -self.player_sprite.movement_speed
            self.player_sprite.texture = self.player_sprite.textures_dict["left"]
        elif key == arcade.key.D:
            self.player_sprite.change_x = self.player_sprite.movement_speed
            self.player_sprite.texture = self.player_sprite.textures_dict["right"]
        elif key == arcade.key.LSHIFT:
            if self.player_sprite.stamina >= 5:
                self.player_sprite.is_running = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.LSHIFT:
            self.player_sprite.is_running = False
