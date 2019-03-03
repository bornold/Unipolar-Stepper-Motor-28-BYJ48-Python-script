import motor2

frac = .17

try:
    setup()
    forwardBy(frac)
    sleep(2)
    backBy(frac)
finally:
    cleanup()