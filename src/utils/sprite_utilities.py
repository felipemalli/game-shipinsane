import pygame
from PPlay.sprite import Sprite


class Sprite_utils:
    
    @classmethod
    def sprite_direction(relative_path, png_name, direction, x = None, y = None):
        sprite_path = relative_path + png_name + '_' + direction + '.png'
        sprite = Sprite(sprite_path)
        if x and y:
            sprite.x = x
            sprite.y = y

        return sprite

    @classmethod
    def collide_mask_rect(left, right):
        xoffset = right.rect[0] - left.x
        yoffset = right.rect[1] - left.y
        try:
            leftmask = left.mask
        except AttributeError:
            leftmask = pygame.mask.Mask(left.size, True)
        try:
            rightmask = right.mask
        except AttributeError:
            rightmask = pygame.mask.from_surface(right.image)
        return leftmask.overlap(rightmask, (xoffset, yoffset))

    @classmethod
    def sprite_collide_obj_list(sprite, list):
        for list_object in list:
            if sprite.rect.colliderect(list_object.sprite.rect):
                return True
        return False
