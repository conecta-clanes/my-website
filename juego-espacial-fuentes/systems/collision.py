def circles_overlap(ax, ay, ar, bx, by, br):
    return (ax - bx) ** 2 + (ay - by) ** 2 < (ar + br) ** 2


def check_bullet_enemy(bullets, enemies, score_ref):
    for bullet in bullets:
        if not bullet.alive:
            continue
        for enemy in enemies:
            if not enemy.alive:
                continue
            if circles_overlap(bullet.x, bullet.y, bullet.radius,
                               enemy.x, enemy.y, enemy.radius):
                bullet.alive = False
                if enemy.hit():
                    score_ref[0] += enemy.points


def check_player_enemy(player, enemies):
    if not player.alive or player.invulnerable > 0:
        return False
    for enemy in enemies:
        if not enemy.alive:
            continue
        if circles_overlap(player.x, player.y, player.radius,
                           enemy.x, enemy.y, enemy.radius):
            return True
    return False
