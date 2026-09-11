def check_blasts_items(blasts, items):
    """Retorna lista de (blast, item) que colisionaron este frame."""
    hits = []
    for blast in blasts:
        if not blast.alive:
            continue
        for item in items:
            if not item.alive:
                continue
            dist_sq = (blast.x - item.x) ** 2 + (blast.y - item.y) ** 2
            if dist_sq < (blast.radius + item.radius) ** 2:
                hits.append((blast, item))
    return hits
