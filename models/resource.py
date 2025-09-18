import arcade


class Resource(arcade.Sprite):
    def __init__(self, image_path, resource_type, scale=0.5):
        super().__init__(image_path, scale)

        self.resource_type = resource_type
        self.weight = 2