import argparse
import pygame
import sys
from scenes.menu_scene import MenuScene


def parse_args():
    parser = argparse.ArgumentParser(description="Guardianes del Reciclaje")
    parser.add_argument(
        "--grabar", dest="record", action="store_true", default=False,
        help="Grabar la sesión en video (guarda en recordings/)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guardianes del Reciclaje")
    clock = pygame.time.Clock()

    scene = MenuScene(screen, record=args.record)

    while True:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                from scenes.game_scene import GameScene
                if isinstance(scene, GameScene):
                    scene._stop_and_go_menu()
                pygame.quit()
                sys.exit()

        scene = scene.update(dt)

        from scenes.game_scene import GameScene
        if isinstance(scene, GameScene):
            scene.draw(dt)
        else:
            scene.draw()

        pygame.display.flip()


if __name__ == "__main__":
    main()
