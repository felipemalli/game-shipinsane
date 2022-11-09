import pygame


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
