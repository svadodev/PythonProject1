import pygame


def is_empty_frame(surface):
    return surface.get_bounding_rect().width == 0
#yes

def GetFrames(originalImage, frame_width, frame_height):
    frames = []
    sheet_width = originalImage.get_width()
    sheet_height = originalImage.get_height()

    columns = sheet_width // frame_width
    rows = sheet_height // frame_height

    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(
                col * frame_width,
                row * frame_height,
                frame_width,
                frame_height
            )

            frame = originalImage.subsurface(rect).copy()
            if not is_empty_frame(frame):
                frames.append(frame)

    return frames