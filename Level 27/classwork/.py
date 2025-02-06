def check_alive(health):
    if health > 0:
        return True
    elif health == 0:
        return False
    else:
        return False

print(check_alive(0))