def cat_and_mouse(x: int, y: int, z: int) -> str:
    cat_distance = abs(x - z)
    mouse_distance = abs(y - z)
    
    if cat_distance < mouse_distance:
        return "Cat A"
    elif cat_distance > mouse_distance:
        return "Cat B"
    return "Mouse C"