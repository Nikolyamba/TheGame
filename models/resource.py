import arcade


class Resource(arcade.Sprite):
    def __init__(self, image_path, resourse_type, scale=0.5):
        super().__init__(image_path, scale)

        self.resourse_type = resourse_type
        self.weight = 2